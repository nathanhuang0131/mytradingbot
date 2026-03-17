"""Strategy control UI services."""

from __future__ import annotations

import logging

from pydantic import BaseModel

from mytradingbot.orchestration.service import TradingPlatformService

logger = logging.getLogger(__name__)


class StrategyControlPayload(BaseModel):
    """Strategy control form payload."""

    available_strategies: list[str]
    available_modes: list[str]
    default_strategy: str
    live_trading_enabled: bool


class StrategyControlService:
    """Expose strategy and runtime mode choices to the UI."""

    def __init__(self, platform_service: TradingPlatformService) -> None:
        self.platform_service = platform_service

    def get_control_payload(self) -> StrategyControlPayload:
        settings = self.platform_service.settings
        return StrategyControlPayload(
            available_strategies=self.platform_service.get_strategy_names(),
            available_modes=["dry_run", "paper", "live"],
            default_strategy=settings.strategies.default_strategy.value,
            live_trading_enabled=settings.runtime.live_trading_enabled,
        )
