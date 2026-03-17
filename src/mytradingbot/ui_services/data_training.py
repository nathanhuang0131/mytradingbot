"""Data and training UI services."""

from __future__ import annotations

import logging

from mytradingbot.orchestration.service import TradingPlatformService
from mytradingbot.qlib_engine.models import QlibOperationResult

logger = logging.getLogger(__name__)


class DataTrainingService:
    """Thin UI service around qlib maintenance operations."""

    def __init__(self, platform_service: TradingPlatformService) -> None:
        self.platform_service = platform_service

    def build_dataset(self) -> QlibOperationResult:
        return self.platform_service.build_dataset()

    def train_models(self) -> QlibOperationResult:
        return self.platform_service.train_models()

    def refresh_predictions(self) -> QlibOperationResult:
        return self.platform_service.refresh_predictions()
