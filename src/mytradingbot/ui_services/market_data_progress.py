"""Market-data progress tracking models and storage."""

from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path
from typing import Callable, Literal

from pydantic import BaseModel, Field

from mytradingbot.core.settings import AppSettings
from mytradingbot.data.models import MarketDataPipelineResult, MarketDataProgressEvent


class TimeframeProgressPayload(BaseModel):
    timeframe: str
    status: Literal["waiting", "in_progress", "completed", "failed"] = "waiting"
    stage: str = "waiting"
    symbols_requested: int = 0
    symbols_with_data: int = 0
    symbols_without_data: int = 0
    rows_downloaded: int = 0
    raw_folder: str
    normalized_folder: str
    resolved_start_at: datetime | None = None
    resolved_end_at: datetime | None = None


class MarketDataProgressPayload(BaseModel):
    run_id: str
    operation: Literal["download", "update", "normalize_only"]
    status: Literal["running", "completed", "failed"] = "running"
    message: str | None = None
    current_step: str = "Waiting to start"
    requested_symbol_count: int = 0
    requested_symbols_preview: list[str] = Field(default_factory=list)
    requested_timeframes: list[str] = Field(default_factory=list)
    raw_output_root: str
    normalized_output_root: str
    snapshot_output_path: str
    completed_steps: list[str] = Field(default_factory=list)
    remaining_steps: list[str] = Field(default_factory=list)
    timeframe_progress: list[TimeframeProgressPayload] = Field(default_factory=list)
    started_at: datetime
    updated_at: datetime
    finished_at: datetime | None = None


class MarketDataProgressTracker:
    """Persist and fan out market-data progress state for the operator UI."""

    def __init__(
        self,
        *,
        settings: AppSettings,
        operation: Literal["download", "update", "normalize_only"],
        requested_symbols: list[str],
        requested_timeframes: list[str],
        provider_name: str,
        on_update: Callable[[MarketDataProgressPayload], None] | None = None,
    ) -> None:
        now = datetime.now(timezone.utc)
        self.settings = settings
        self.provider_name = provider_name
        self.on_update = on_update
        self.progress_path = self.settings.paths.runtime_dir / "market_data_progress.json"
        raw_output_root = self.settings.paths.raw_data_dir / provider_name / "bars"
        normalized_output_root = self.settings.paths.normalized_data_dir / "bars"
        self.all_steps = self._build_all_steps(requested_timeframes)
        self.payload = MarketDataProgressPayload(
            run_id=now.strftime("%Y%m%d%H%M%S"),
            operation=operation,
            requested_symbol_count=len(requested_symbols),
            requested_symbols_preview=requested_symbols[:20],
            requested_timeframes=requested_timeframes,
            raw_output_root=str(raw_output_root),
            normalized_output_root=str(normalized_output_root),
            snapshot_output_path=str(self.settings.market_snapshot_artifact_path()),
            timeframe_progress=[
                TimeframeProgressPayload(
                    timeframe=timeframe,
                    symbols_requested=len(requested_symbols),
                    raw_folder=str(raw_output_root / timeframe),
                    normalized_folder=str(normalized_output_root / timeframe),
                )
                for timeframe in requested_timeframes
            ],
            remaining_steps=self.all_steps.copy(),
            started_at=now,
            updated_at=now,
        )
        self._persist()

    @classmethod
    def load(cls, settings: AppSettings) -> MarketDataProgressPayload | None:
        progress_path = settings.paths.runtime_dir / "market_data_progress.json"
        if not progress_path.exists():
            return None
        return MarketDataProgressPayload.model_validate_json(
            progress_path.read_text(encoding="utf-8")
        )

    def handle_event(self, event: MarketDataProgressEvent) -> None:
        now = datetime.now(timezone.utc)
        self.payload.updated_at = now
        if event.message:
            self.payload.message = event.message
        if event.event_type == "run_started":
            self.payload.status = "running"
            self.payload.current_step = event.message or "Starting market data run"
        elif event.event_type == "timeframe_started" and event.timeframe:
            row = self._row_for(event.timeframe)
            row.status = "in_progress"
            row.stage = event.stage or "download"
            self.payload.current_step = event.message or f"{event.timeframe} in progress"
        elif event.event_type == "timeframe_raw_completed" and event.timeframe:
            row = self._row_for(event.timeframe)
            row.status = "in_progress"
            row.stage = "raw completed"
            row.symbols_with_data = len(event.symbols_with_data)
            row.symbols_without_data = len(event.symbols_without_data)
            row.rows_downloaded = event.total_rows_downloaded
            row.resolved_start_at = event.resolved_start_at
            row.resolved_end_at = event.resolved_end_at
            if event.raw_folder:
                row.raw_folder = event.raw_folder
            self._mark_completed(f"{event.timeframe} download")
            self.payload.current_step = event.message or f"{event.timeframe} raw download completed"
        elif event.event_type == "timeframe_normalized" and event.timeframe:
            row = self._row_for(event.timeframe)
            row.status = "completed"
            row.stage = "normalized"
            if event.normalized_folder:
                row.normalized_folder = event.normalized_folder
            self._mark_completed(f"{event.timeframe} normalize")
            self.payload.current_step = event.message or f"{event.timeframe} normalization completed"
        elif event.event_type == "snapshot_started":
            self.payload.current_step = event.message or "Building market snapshot"
        elif event.event_type == "snapshot_completed":
            self._mark_completed("market snapshot")
            self.payload.current_step = event.message or "Market snapshot completed"
        elif event.event_type == "run_completed":
            self.payload.status = "completed"
            self.payload.current_step = "Completed"
            self.payload.finished_at = now
        elif event.event_type == "run_failed":
            self.payload.status = "failed"
            self.payload.current_step = event.message or "Failed"
            self.payload.finished_at = now
            if event.timeframe:
                row = self._row_for(event.timeframe)
                row.status = "failed"
                row.stage = event.stage or "failed"
        self._persist()

    def finalize(self, result: MarketDataPipelineResult) -> MarketDataProgressPayload:
        self.payload.message = result.message
        if result.raw_download_summary is not None:
            provider_name = result.raw_download_summary.provider
            self.provider_name = provider_name
            self.payload.raw_output_root = str(
                self.settings.paths.raw_data_dir / provider_name / "bars"
            )
            for summary in result.raw_download_summary.timeframe_summaries:
                row = self._row_for(summary.timeframe)
                row.symbols_with_data = len(summary.symbols_with_data)
                row.symbols_without_data = len(summary.symbols_without_data)
                row.rows_downloaded = summary.total_rows_downloaded
                row.resolved_start_at = summary.resolved_start_at
                row.resolved_end_at = summary.resolved_end_at
                row.raw_folder = str(
                    self.settings.paths.raw_data_dir / provider_name / "bars" / summary.timeframe
                )
                row.normalized_folder = str(
                    self.settings.paths.normalized_data_dir / "bars" / summary.timeframe
                )
                row.status = "completed" if result.ok else (
                    "completed" if summary.status == "complete" else "failed"
                )
                row.stage = "normalized" if result.ok else summary.status
                self._mark_completed(f"{summary.timeframe} download")
                self._mark_completed(f"{summary.timeframe} normalize")
        if result.ok:
            self._mark_completed("market snapshot")
        self.payload.status = "completed" if result.ok else "failed"
        self.payload.current_step = "Completed" if result.ok else "Failed"
        self.payload.finished_at = datetime.now(timezone.utc)
        self.payload.updated_at = self.payload.finished_at
        self._persist()
        return self.payload

    def _persist(self) -> None:
        self.payload.remaining_steps = [
            step for step in self.all_steps if step not in self.payload.completed_steps
        ]
        self.progress_path.parent.mkdir(parents=True, exist_ok=True)
        self.progress_path.write_text(
            self.payload.model_dump_json(indent=2),
            encoding="utf-8",
        )
        if self.on_update is not None:
            self.on_update(self.payload.model_copy(deep=True))

    def _row_for(self, timeframe: str) -> TimeframeProgressPayload:
        for row in self.payload.timeframe_progress:
            if row.timeframe == timeframe:
                return row
        raise KeyError(f"Unknown timeframe progress row: {timeframe}")

    def _mark_completed(self, step: str) -> None:
        if step not in self.payload.completed_steps:
            self.payload.completed_steps.append(step)

    @staticmethod
    def _build_all_steps(timeframes: list[str]) -> list[str]:
        steps: list[str] = []
        for timeframe in timeframes:
            steps.append(f"{timeframe} download")
            steps.append(f"{timeframe} normalize")
        steps.append("market snapshot")
        return steps
