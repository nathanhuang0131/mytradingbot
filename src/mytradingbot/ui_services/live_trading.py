"""Live trading UI services."""

from __future__ import annotations

import logging

from pydantic import BaseModel

from mytradingbot.brokers.alpaca import AlpacaBrokerScaffold
from mytradingbot.orchestration.service import TradingPlatformService

logger = logging.getLogger(__name__)


class LiveTradingPayload(BaseModel):
    """Payload for the live trading page."""

    enabled: bool
    message: str
    validation_only: bool = True


class LiveTradingService:
    """Expose visible but gated live trading status."""

    def __init__(self, platform_service: TradingPlatformService) -> None:
        self.platform_service = platform_service
        self.scaffold = AlpacaBrokerScaffold()

    def get_payload(self) -> LiveTradingPayload:
        capability = self.scaffold.get_live_capability_status()
        return LiveTradingPayload(
            enabled=capability.is_enabled,
            message=capability.message,
            validation_only=True,
        )
