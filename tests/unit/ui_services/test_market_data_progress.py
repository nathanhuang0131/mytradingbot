from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path

from mytradingbot.core.paths import RepoPaths
from mytradingbot.core.settings import AppSettings
from mytradingbot.data.models import (
    MarketDataPipelineResult,
    MarketDataProgressEvent,
    RawDownloadRunSummary,
    RawDownloadTimeframeSummary,
)
from mytradingbot.orchestration.service import TradingPlatformService
from mytradingbot.ui_services.data_training import DataTrainingService


def _build_settings(repo_root: Path) -> AppSettings:
    settings = AppSettings(paths=RepoPaths.for_root(repo_root))
    settings.ensure_runtime_directories()
    return settings


def test_market_data_progress_tracker_persists_timeframe_and_step_status(tmp_path: Path) -> None:
    settings = _build_settings(tmp_path)
    service = DataTrainingService(TradingPlatformService(settings=settings))
    progress_updates = []
    tracker = service.create_market_data_progress_tracker(
        operation="download",
        requested_symbols=["AAPL", "MSFT"],
        requested_timeframes=["1m", "5m"],
        on_update=lambda payload: progress_updates.append(payload.model_copy(deep=True)),
    )

    tracker.handle_event(
        MarketDataProgressEvent(
            event_type="run_started",
            operation="download",
            message="Starting market data download.",
        )
    )
    tracker.handle_event(
        MarketDataProgressEvent(
            event_type="timeframe_started",
            operation="download",
            timeframe="1m",
            stage="download",
            message="Downloading 1m bars.",
        )
    )
    tracker.handle_event(
        MarketDataProgressEvent(
            event_type="timeframe_raw_completed",
            operation="download",
            timeframe="1m",
            stage="download",
            message="1m raw download complete.",
            symbols_with_data=["AAPL"],
            symbols_without_data=["MSFT"],
            total_rows_downloaded=120,
            raw_folder=str(settings.paths.raw_data_dir / "fake" / "bars" / "1m"),
            resolved_start_at=datetime(2026, 3, 1, tzinfo=timezone.utc),
            resolved_end_at=datetime(2026, 3, 25, tzinfo=timezone.utc),
        )
    )
    tracker.handle_event(
        MarketDataProgressEvent(
            event_type="timeframe_normalized",
            operation="download",
            timeframe="1m",
            stage="normalize",
            message="1m normalization complete.",
            normalized_folder=str(settings.paths.normalized_data_dir / "bars" / "1m"),
        )
    )
    tracker.finalize(
        MarketDataPipelineResult(
            ok=True,
            message="Repo-local market data download, normalization, and snapshot build completed.",
            artifacts=[],
            raw_download_summary=RawDownloadRunSummary(
                generated_at=datetime(2026, 3, 25, tzinfo=timezone.utc),
                mode="download",
                provider="fake",
                timeframe_summaries=[
                    RawDownloadTimeframeSummary(
                        timeframe="1m",
                        requested_symbols=["AAPL", "MSFT"],
                        attempted_symbols=["AAPL", "MSFT"],
                        symbols_with_data=["AAPL"],
                        symbols_without_data=["MSFT"],
                        total_rows_downloaded=120,
                        raw_files_written=[],
                        resolved_start_at=datetime(2026, 3, 1, tzinfo=timezone.utc),
                        resolved_end_at=datetime(2026, 3, 25, tzinfo=timezone.utc),
                    ),
                    RawDownloadTimeframeSummary(
                        timeframe="5m",
                        requested_symbols=["AAPL", "MSFT"],
                        attempted_symbols=["AAPL", "MSFT"],
                        symbols_with_data=["AAPL", "MSFT"],
                        symbols_without_data=[],
                        total_rows_downloaded=240,
                        raw_files_written=[],
                        resolved_start_at=datetime(2026, 3, 1, tzinfo=timezone.utc),
                        resolved_end_at=datetime(2026, 3, 25, tzinfo=timezone.utc),
                    ),
                ],
            ),
        )
    )

    latest = service.get_market_data_progress()

    assert latest is not None
    assert latest.operation == "download"
    assert latest.status == "completed"
    assert latest.requested_symbol_count == 2
    assert latest.current_step == "Completed"
    assert latest.raw_output_root.endswith("data\\raw\\fake\\bars")
    assert latest.normalized_output_root.endswith("data\\normalized\\bars")
    assert latest.snapshot_output_path.endswith("data\\snapshots\\market_snapshot.json")
    assert latest.completed_steps
    assert latest.remaining_steps == []
    one_minute = next(row for row in latest.timeframe_progress if row.timeframe == "1m")
    assert one_minute.status == "completed"
    assert one_minute.symbols_with_data == 1
    assert one_minute.symbols_without_data == 1
    assert one_minute.rows_downloaded == 120
    five_minute = next(row for row in latest.timeframe_progress if row.timeframe == "5m")
    assert five_minute.status == "completed"
    assert five_minute.symbols_with_data == 2
    assert progress_updates
