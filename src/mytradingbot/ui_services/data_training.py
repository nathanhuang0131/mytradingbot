"""Data and training UI services."""

from __future__ import annotations

import logging
from pathlib import Path

from pydantic import BaseModel, Field

from mytradingbot.core.capabilities import CapabilitySnapshot
from mytradingbot.orchestration.service import TradingPlatformService
from mytradingbot.qlib_engine.models import QlibOperationResult
from mytradingbot.data.models import MarketDataPipelineResult
from mytradingbot.session_setup.models import slugify_profile_name
from mytradingbot.session_setup.service import SetupWizardService
from mytradingbot.training.models import AlphaTrainingRunResult, TrainingDataQualityReport
from mytradingbot.training.service import AlphaRobustTrainingService
from mytradingbot.ui_services.market_data_progress import (
    MarketDataProgressPayload,
    MarketDataProgressTracker,
)
from mytradingbot.universe.models import TopLiquidityUniverseResult
from mytradingbot.universe.service import TopLiquidityUniverseService
from mytradingbot.universe.storage import UniverseStorage

logger = logging.getLogger(__name__)


class DataTrainingPayload(BaseModel):
    """Operator payload for phase-2/3 maintenance pages."""

    capabilities: CapabilitySnapshot
    default_strategy: str
    default_timeframes: list[str]
    works_without_pyqlib: list[str]
    works_without_alpaca_credentials: list[str]
    profile_names: list[str] = Field(default_factory=list)
    default_profile_name: str | None = None


class UniverseSourcePayload(BaseModel):
    selected_profile_name: str | None = None
    default_universe_file_path: str
    selected_universe_file_path: str
    alternate_universe_file_path: str
    symbols: list[str] = Field(default_factory=list)
    symbol_count: int = 0
    is_ready: bool = False
    validation_message: str | None = None


class DataTrainingService:
    """Thin UI service around qlib maintenance operations."""

    def __init__(self, platform_service: TradingPlatformService) -> None:
        self.platform_service = platform_service
        self.universe_service = TopLiquidityUniverseService(
            settings=self.platform_service.settings
        )
        self.universe_storage = UniverseStorage(settings=self.platform_service.settings)
        self.training_service = AlphaRobustTrainingService(
            settings=self.platform_service.settings
        )
        self.wizard_service = SetupWizardService(settings=self.platform_service.settings)

    def get_payload(self) -> DataTrainingPayload:
        settings = self.platform_service.settings
        profiles = self.wizard_service.list_profiles()
        profile_names = [profile.profile_name for profile in profiles]
        return DataTrainingPayload(
            capabilities=self.platform_service.get_capabilities(),
            default_strategy=settings.strategies.default_strategy.value,
            default_timeframes=settings.data.default_timeframes,
            works_without_pyqlib=[
                "download_market_data",
                "update_market_data",
                "build_market_snapshot",
                "paper_trading_with_explicit_artifacts",
            ],
            works_without_alpaca_credentials=[
                "dashboard",
                "paper_trading_with_explicit_artifacts",
                "qlib_artifact_inspection",
            ],
            profile_names=profile_names,
            default_profile_name=profile_names[0] if profile_names else None,
        )

    def resolve_universe_source(
        self,
        *,
        profile_name: str | None,
        universe_file_path: str | None = None,
    ) -> UniverseSourcePayload:
        selected_profile_name = profile_name or self.get_payload().default_profile_name
        default_path = self._default_universe_file_path(selected_profile_name)
        selected_path = Path(universe_file_path.strip()) if universe_file_path and universe_file_path.strip() else default_path
        alternate_path = self.platform_service.settings.paths.universe_dir / "latest_top_liquidity_universe.json"
        if not selected_path.exists():
            return UniverseSourcePayload(
                selected_profile_name=selected_profile_name,
                default_universe_file_path=str(default_path),
                selected_universe_file_path=str(selected_path),
                alternate_universe_file_path=str(alternate_path),
                validation_message=f"Universe file not found: {selected_path}",
            )
        try:
            symbols = self.universe_storage.load_symbols(selected_path)
        except (OSError, ValueError) as exc:
            return UniverseSourcePayload(
                selected_profile_name=selected_profile_name,
                default_universe_file_path=str(default_path),
                selected_universe_file_path=str(selected_path),
                alternate_universe_file_path=str(alternate_path),
                validation_message=str(exc),
            )
        return UniverseSourcePayload(
            selected_profile_name=selected_profile_name,
            default_universe_file_path=str(default_path),
            selected_universe_file_path=str(selected_path),
            alternate_universe_file_path=str(alternate_path),
            symbols=symbols,
            symbol_count=len(symbols),
            is_ready=True,
        )

    def generate_top_liquidity_universe(self) -> TopLiquidityUniverseResult:
        return self.universe_service.generate_top_liquidity_universe()

    def download_market_data(
        self,
        *,
        symbols: list[str] | None = None,
        symbols_file: Path | None = None,
        timeframes: list[str] | None = None,
        progress_callback=None,
    ) -> MarketDataPipelineResult:
        kwargs = {
            "symbols": symbols,
            "symbols_file": symbols_file,
            "timeframes": timeframes,
            "full_refresh": True,
        }
        if progress_callback is not None:
            kwargs["progress_callback"] = progress_callback
        return self.platform_service.download_market_data(
            **kwargs,
        )

    def update_market_data(
        self,
        *,
        symbols: list[str] | None = None,
        symbols_file: Path | None = None,
        timeframes: list[str] | None = None,
        progress_callback=None,
    ) -> MarketDataPipelineResult:
        kwargs = {
            "symbols": symbols,
            "symbols_file": symbols_file,
            "timeframes": timeframes,
            "full_refresh": False,
        }
        if progress_callback is not None:
            kwargs["progress_callback"] = progress_callback
        return self.platform_service.download_market_data(**kwargs)

    def build_dataset(
        self,
        *,
        strategy_name: str | None = None,
        symbols: list[str] | None = None,
        symbols_file: Path | None = None,
    ) -> QlibOperationResult:
        return self.platform_service.build_dataset(
            strategy_name=strategy_name,
            symbols=symbols,
            symbols_file=symbols_file,
        )

    def train_models(self, *, strategy_name: str | None = None) -> QlibOperationResult:
        return self.platform_service.train_models(strategy_name=strategy_name)

    def refresh_predictions(self, *, strategy_name: str | None = None) -> QlibOperationResult:
        return self.platform_service.refresh_predictions(strategy_name=strategy_name)

    def check_training_data_quality(
        self,
        *,
        strategy_name: str | None = None,
        symbols: list[str] | None = None,
        symbols_file: Path | None = None,
        timeframes: list[str] | None = None,
    ) -> TrainingDataQualityReport:
        del strategy_name
        resolved_symbols = self.training_service.ensure_universe(
            symbols=symbols,
            symbols_file=symbols_file,
        )
        return self.training_service.run_quality_check(
            symbols=resolved_symbols,
            timeframes=timeframes or self.platform_service.settings.data.default_timeframes,
        )

    def run_alpha_robust_training(
        self,
        *,
        strategy_name: str | None = None,
        symbols: list[str] | None = None,
        symbols_file: Path | None = None,
        timeframes: list[str] | None = None,
    ) -> AlphaTrainingRunResult:
        return self.training_service.run_alpha_robust_training(
            strategy_name=strategy_name
            or self.platform_service.settings.strategies.default_strategy.value,
            symbols=symbols,
            symbols_file=symbols_file,
            timeframes=timeframes,
        )

    def create_market_data_progress_tracker(
        self,
        *,
        operation: str,
        requested_symbols: list[str],
        requested_timeframes: list[str],
        on_update=None,
    ) -> MarketDataProgressTracker:
        return MarketDataProgressTracker(
            settings=self.platform_service.settings,
            operation=operation,
            requested_symbols=requested_symbols,
            requested_timeframes=requested_timeframes,
            provider_name=self.platform_service.data_pipeline.provider_name,
            on_update=on_update,
        )

    def get_market_data_progress(self) -> MarketDataProgressPayload | None:
        return MarketDataProgressTracker.load(self.platform_service.settings)

    def _default_universe_file_path(self, profile_name: str | None) -> Path:
        if profile_name:
            return self.platform_service.settings.paths.active_universes_dir / (
                f"{slugify_profile_name(profile_name)}_active_symbols.json"
            )
        return self.platform_service.settings.paths.universe_dir / "latest_top_liquidity_universe.json"
