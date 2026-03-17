"""Execution engine for routing approved trade intents to broker adapters."""

from __future__ import annotations

import logging

from mytradingbot.brokers.base import BaseBroker
from mytradingbot.core.enums import RuntimeMode
from mytradingbot.core.models import ExecutionRequest, ExecutionResult, RiskDecision

logger = logging.getLogger(__name__)


class ExecutionEngine:
    """Translate risk-approved intents into broker execution requests."""

    def __init__(self, *, broker: BaseBroker) -> None:
        self.broker = broker

    def execute(self, decision: RiskDecision, *, mode: RuntimeMode) -> ExecutionResult:
        if not decision.approved or decision.intent is None:
            return ExecutionResult(
                execution_skipped=True,
                reason=decision.reason or "risk_rejected",
            )

        request = ExecutionRequest.from_intent(decision.intent, mode)
        if mode is RuntimeMode.DRY_RUN:
            return ExecutionResult.skipped(request=request, reason="dry_run_mode")

        if mode is RuntimeMode.LIVE:
            return ExecutionResult.skipped(
                request=request,
                reason="live_execution_disabled",
            )

        return self.broker.submit_order(request)
