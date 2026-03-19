"""Data and training UI services."""

from __future__ import annotations

import logging

from pydantic import BaseModel

from mytradingbot.core.capabilities import CapabilitySnapshot
from mytradingbot.orchestration.service import TradingPlatformService
from mytradingbot.qlib_engine.models import QlibOperationResult
from mytradingbot.data.models import MarketDataPipelineResult
from mytradingbot.training.models import AlphaTrainingRunResult, TrainingDataQualityReport
from mytradingbot.training.service import AlphaRobustTrainingService
from mytradingbot.universe.models import TopLiquidityUniverseResult
from mytradingbot.universe.service import TopLiquidityUniverseService

logger = logging.getLogger(__name__)


class DataTrainingPayload(BaseModel):
    """Operator payload for phase-2/3 maintenance pages."""

    capabilities: CapabilitySnapshot
    default_strategy: str
    default_timeframes: list[str]
    works_without_pyqlib: list[str]
    works_without_alpaca_credentials: list[str]


class DataTrainingService:
    """Thin UI service around qlib maintenance operations."""

    def __init__(self, platform_service: TradingPlatformService) -> None:
        self.platform_service = platform_service
        self.universe_service = TopLiquidityUniverseService(
            settings=self.platform_service.settings
        )
        self.training_service = AlphaRobustTrainingService(
            settings=self.platform_service.settings
        )

    def get_payload(self) -> DataTrainingPayload:
        settings = self.platform_service.settings
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
        )

    def generate_top_liquidity_universe(self) -> TopLiquidityUniverseResult:
        return self.universe_service.generate_top_liquidity_universe()

    def download_market_data(
        self,
        *,
        symbols: list[str] | None = None,
        timeframes: list[str] | None = None,
    ) -> MarketDataPipelineResult:
        return self.platform_service.download_market_data(
            symbols=symbols,
            timeframes=timeframes,
            full_refresh=True,
        )

    def update_market_data(
        self,
        *,
        symbols: list[str] | None = None,
        timeframes: list[str] | None = None,
    ) -> MarketDataPipelineResult:
        return self.platform_service.download_market_data(
            symbols=symbols,
            timeframes=timeframes,
            full_refresh=False,
        )

    def build_dataset(self, *, strategy_name: str | None = None) -> QlibOperationResult:
        return self.platform_service.build_dataset(strategy_name=strategy_name)

    def train_models(self, *, strategy_name: str | None = None) -> QlibOperationResult:
        return self.platform_service.train_models(strategy_name=strategy_name)

    def refresh_predictions(self, *, strategy_name: str | None = None) -> QlibOperationResult:
        return self.platform_service.refresh_predictions(strategy_name=strategy_name)

    def check_training_data_quality(
        self,
        *,
        strategy_name: str | None = None,
    ) -> TrainingDataQualityReport:
        del strategy_name
        symbols = self.training_service.ensure_universe()
        return self.training_service.run_quality_check(
            symbols=symbols,
            timeframes=self.platform_service.settings.data.default_timeframes,
        )

    def run_alpha_robust_training(
        self,
        *,
        strategy_name: str | None = None,
    ) -> AlphaTrainingRunResult:
        return self.training_service.run_alpha_robust_training(
            strategy_name=strategy_name
            or self.platform_service.settings.strategies.default_strategy.value,
        )
