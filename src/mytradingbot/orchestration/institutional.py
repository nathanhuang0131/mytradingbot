"""Institutional pipeline orchestration for v2 operational runs."""

from __future__ import annotations

import json
from pathlib import Path

from pydantic import BaseModel, Field

from mytradingbot.core.enums import RuntimeMode
from mytradingbot.core.settings import AppSettings
from mytradingbot.orchestration.service import TradingPlatformService
from mytradingbot.training.service import AlphaRobustTrainingService
from mytradingbot.universe.service import TopLiquidityUniverseService
from mytradingbot.universe.storage import UniverseStorage


class InstitutionalPipelineResult(BaseModel):
    ok: bool
    message: str
    artifacts: list[str] = Field(default_factory=list)
    reports: list[str] = Field(default_factory=list)
    session_id: str | None = None
    trade_count: int = 0
    rejection_reasons: list[str] = Field(default_factory=list)


class InstitutionalPipelineService:
    """Run the canonical v2 institutional pipeline in a shared service graph."""

    def __init__(
        self,
        settings: AppSettings | None = None,
        *,
        platform_service: TradingPlatformService | None = None,
        training_service: AlphaRobustTrainingService | None = None,
        universe_service: TopLiquidityUniverseService | None = None,
        universe_storage: UniverseStorage | None = None,
    ) -> None:
        self.settings = settings or AppSettings()
        self.platform_service = platform_service or TradingPlatformService(settings=self.settings)
        self.training_service = training_service or AlphaRobustTrainingService(settings=self.settings)
        self.universe_service = universe_service or TopLiquidityUniverseService(settings=self.settings)
        self.universe_storage = universe_storage or UniverseStorage(settings=self.settings)

    def run(
        self,
        *,
        strategy_name: str,
        mode: RuntimeMode,
        symbols: list[str] | None = None,
        symbols_file: Path | None = None,
        timeframes: list[str] | None = None,
        use_top_liquidity_universe: bool = False,
        top_n: int | None = None,
        min_eligible_symbols: int | None = None,
        skip_train: bool = False,
        skip_maintenance: bool = False,
        skip_validation: bool = False,
    ) -> InstitutionalPipelineResult:
        artifacts: list[str] = []
        reports: list[str] = []
        resolved_symbols = symbols
        if use_top_liquidity_universe and resolved_symbols is None and symbols_file is None:
            universe_result = self.universe_service.generate_top_liquidity_universe(top_n=top_n)
            reports.extend(universe_result.artifacts)
            if not universe_result.ok:
                return InstitutionalPipelineResult(
                    ok=False,
                    message=universe_result.message,
                    reports=reports,
                )
            resolved_symbols = [row.symbol for row in universe_result.rows]
            symbols_file = self.settings.paths.universe_dir / "latest_top_liquidity_universe.json"

        training_result = self.training_service.run_alpha_robust_training(
            strategy_name=strategy_name,
            symbols=resolved_symbols,
            symbols_file=symbols_file,
            top_n=top_n,
            timeframes=timeframes,
            min_eligible_symbols=min_eligible_symbols,
            skip_download=skip_maintenance,
            skip_train=skip_train,
        )
        artifacts.extend(training_result.artifacts)
        reports.extend(training_result.reports)
        if not training_result.ok:
            summary = InstitutionalPipelineResult(
                ok=False,
                message=training_result.message,
                artifacts=artifacts,
                reports=reports,
            )
            reports.extend(self._write_summary(summary))
            summary.reports = reports
            return summary

        session = self.platform_service.run_session(
            strategy_name=strategy_name,
            mode=mode,
        )
        summary = InstitutionalPipelineResult(
            ok=session.session_summary.status == "completed",
            message="Institutional pipeline completed." if session.session_summary.status == "completed" else "Institutional pipeline failed during session execution.",
            artifacts=artifacts,
            reports=reports,
            session_id=session.session_summary.session_id,
            trade_count=session.session_summary.trade_count,
            rejection_reasons=session.rejection_reasons,
        )
        if not skip_validation:
            reports.extend(self._write_summary(summary))
        summary.reports = reports
        return summary

    def _write_summary(self, result: InstitutionalPipelineResult) -> list[str]:
        reports_dir = self.settings.paths.reports_pipeline_dir
        reports_dir.mkdir(parents=True, exist_ok=True)
        summary_json = reports_dir / "institutional_pipeline_summary.json"
        summary_md = reports_dir / "institutional_pipeline_summary.md"
        summary_json.write_text(result.model_dump_json(indent=2), encoding="utf-8")
        rejection_lines = [f"- {reason}" for reason in result.rejection_reasons] or ["- none"]
        summary_md.write_text(
            "\n".join(
                [
                    "# Institutional Pipeline Summary",
                    "",
                    f"- ok: `{result.ok}`",
                    f"- message: `{result.message}`",
                    f"- session_id: `{result.session_id}`",
                    f"- trade_count: `{result.trade_count}`",
                    "",
                    "## Rejection Reasons",
                    "",
                    *rejection_lines,
                ]
            )
            + "\n",
            encoding="utf-8",
        )
        return [str(summary_json), str(summary_md)]
