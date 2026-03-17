"""Paper trading UI services."""

from __future__ import annotations

import logging

from mytradingbot.core.enums import RuntimeMode
from mytradingbot.core.models import SessionResult
from mytradingbot.orchestration.service import TradingPlatformService

logger = logging.getLogger(__name__)


class PaperTradingService:
    """Run and inspect dry-run or paper sessions from the UI."""

    def __init__(self, platform_service: TradingPlatformService) -> None:
        self.platform_service = platform_service

    def run_session(self, *, strategy_name: str, mode: str) -> SessionResult:
        runtime_mode = RuntimeMode(mode)
        if runtime_mode is RuntimeMode.LIVE:
            raise ValueError("Paper trading page only supports dry_run and paper modes.")
        return self.platform_service.run_session(
            strategy_name=strategy_name,
            mode=runtime_mode,
        )
