"""Institutional alpha-robust training orchestration."""

from __future__ import annotations

from datetime import datetime, timezone

from pandas.tseries.offsets import BDay

from mytradingbot.core.settings import AppSettings
from mytradingbot.data.pipeline import MarketDataPipeline
from mytradingbot.qlib_engine.service import QlibWorkflowService
from mytradingbot.training.data_quality import TrainingDataQualityChecker
from mytradingbot.training.models import AlphaTrainingRunResult, TrainingDataQualityReport
from mytradingbot.training.storage import TrainingArtifactStore
from mytradingbot.universe.service import TopLiquidityUniverseService
from mytradingbot.universe.storage import UniverseStorage


class AlphaRobustTrainingService:
    """Run the stricter v2 data-quality and training workflow."""

    def __init__(
        self,
        settings: AppSettings | None = None,
        *,
        data_pipeline: MarketDataPipeline | None = None,
        qlib_service: QlibWorkflowService | None = None,
        quality_checker: TrainingDataQualityChecker | None = None,
        artifact_store: TrainingArtifactStore | None = None,
        universe_service: TopLiquidityUniverseService | None = None,
        universe_storage: UniverseStorage | None = None,
    ) -> None:
        self.settings = settings or AppSettings()
        self.data_pipeline = data_pipeline or MarketDataPipeline(settings=self.settings)
        self.qlib_service = qlib_service or QlibWorkflowService(settings=self.settings)
        self.quality_checker = quality_checker or TrainingDataQualityChecker(settings=self.settings)
        self.artifact_store = artifact_store or TrainingArtifactStore(settings=self.settings)
        self.universe_service = universe_service or TopLiquidityUniverseService(settings=self.settings)
        self.universe_storage = universe_storage or UniverseStorage(settings=self.settings)

    def ensure_universe(
        self,
        *,
        symbols: list[str] | None = None,
        symbols_file=None,
        top_n: int | None = None,
    ) -> list[str]:
        if symbols:
            return sorted({symbol.strip().upper() for symbol in symbols if symbol and symbol.strip()})
        if symbols_file is not None:
            return self.universe_storage.load_symbols(symbols_file)
        latest = self.settings.paths.universe_dir / "latest_top_liquidity_universe.json"
        if latest.exists():
            return self.universe_storage.load_symbols(latest)
        universe = self.universe_service.generate_top_liquidity_universe(top_n=top_n)
        if not universe.ok:
            raise ValueError(universe.message)
        return [row.symbol for row in universe.rows]

    def run_quality_check(
        self,
        *,
        symbols: list[str],
        timeframes: list[str],
    ) -> TrainingDataQualityReport:
        report = self.quality_checker.evaluate(symbols=symbols, timeframes=timeframes)
        report.artifacts = self.artifact_store.write_quality_report(report)
        return report

    def run_alpha_robust_training(
        self,
        *,
        strategy_name: str,
        symbols: list[str] | None = None,
        symbols_file=None,
        top_n: int | None = None,
        timeframes: list[str] | None = None,
        lookback_days: dict[str, int] | None = None,
        min_eligible_symbols: int | None = None,
        skip_download: bool = False,
        skip_train: bool = False,
    ) -> AlphaTrainingRunResult:
        timeframes = timeframes or ["1m", "5m", "15m", "1d"]
        resolved_symbols = self.ensure_universe(
            symbols=symbols,
            symbols_file=symbols_file,
            top_n=top_n,
        )
        reports: list[str] = []
        artifacts: list[str] = []
        now = datetime.now(timezone.utc)
        if not skip_download:
            for timeframe in timeframes:
                lookback = (lookback_days or {}).get(
                    timeframe,
                    self.settings.data.default_full_refresh_lookback(timeframe),
                )
                start_at = (now - BDay(lookback)).to_pydatetime()
                result = self.data_pipeline.download_update_normalize_and_snapshot(
                    symbols=resolved_symbols,
                    timeframes=[timeframe],
                    start_at=start_at,
                    end_at=now,
                    full_refresh=True,
                )
                artifacts.extend(result.artifacts)
                reports.extend(result.report_paths)
                if not result.ok:
                    return AlphaTrainingRunResult(
                        ok=False,
                        message=result.message,
                        eligible_symbols=[],
                        artifacts=artifacts,
                        reports=reports,
                    )

        quality_report = self.run_quality_check(
            symbols=resolved_symbols,
            timeframes=timeframes,
        )
        reports.extend(quality_report.artifacts)
        eligible_symbols = quality_report.eligible_symbols
        minimum_symbols = min_eligible_symbols or self.settings.training.minimum_eligible_symbols
        if not quality_report.ok or len(eligible_symbols) < minimum_symbols:
            return AlphaTrainingRunResult(
                ok=False,
                message=quality_report.message,
                eligible_symbols=eligible_symbols,
                artifacts=artifacts,
                reports=reports,
            )

        build_result = self.qlib_service.build_dataset(
            strategy_name=strategy_name,
            symbols=eligible_symbols,
        )
        artifacts.extend(build_result.artifacts)
        if not build_result.ok:
            return AlphaTrainingRunResult(
                ok=False,
                message=build_result.message,
                eligible_symbols=eligible_symbols,
                artifacts=artifacts,
                reports=reports,
                build_ok=False,
            )

        train_ok = False
        if not skip_train:
            train_result = self.qlib_service.train_models(strategy_name=strategy_name)
            artifacts.extend(train_result.artifacts)
            train_ok = train_result.ok
            if not train_result.ok:
                return AlphaTrainingRunResult(
                    ok=False,
                    message=train_result.message,
                    eligible_symbols=eligible_symbols,
                    artifacts=artifacts,
                    reports=reports,
                    build_ok=True,
                    train_ok=False,
                )
        refresh_result = self.qlib_service.refresh_predictions(strategy_name=strategy_name)
        artifacts.extend(refresh_result.artifacts)
        result = AlphaTrainingRunResult(
            ok=refresh_result.ok,
            message=refresh_result.message,
            eligible_symbols=eligible_symbols,
            artifacts=artifacts,
            reports=reports,
            build_ok=build_result.ok,
            train_ok=train_ok or skip_train,
            refresh_ok=refresh_result.ok,
        )
        result.reports.extend(self.artifact_store.write_run_summary(result))
        return result
