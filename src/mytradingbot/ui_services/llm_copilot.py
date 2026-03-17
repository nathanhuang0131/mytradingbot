"""LLM copilot UI services."""

from __future__ import annotations

import logging
from typing import Any

from mytradingbot.llm.service import AdvisoryLLMService
from mytradingbot.orchestration.service import TradingPlatformService

logger = logging.getLogger(__name__)


class LLMCopilotService:
    """Expose advisory-only LLM workflows to the UI."""

    def __init__(
        self,
        platform_service: TradingPlatformService,
        *,
        client: Any | None = None,
    ) -> None:
        self.platform_service = platform_service
        self.llm_service = AdvisoryLLMService(client=client)

    def explain_last_attempt(self):
        result = self.platform_service.last_session_result
        if not result or not result.trade_attempts:
            return None
        return self.llm_service.explain_signal(result.trade_attempts[0])

    def summarize_last_session(self):
        result = self.platform_service.last_session_result
        if not result:
            return None
        return self.llm_service.summarize_diagnostics(result)

    def compare_last_session_to(self, other_results):
        result = self.platform_service.last_session_result
        results = [item for item in [result, *other_results] if item is not None]
        if not results:
            return None
        return self.llm_service.compare_strategies(results)
