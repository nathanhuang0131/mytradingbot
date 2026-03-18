"""Execution engine for routing approved trade intents to broker adapters."""

from __future__ import annotations

import logging
import math

from mytradingbot.brokers.base import BaseBroker
from mytradingbot.core.enums import RuntimeMode
from mytradingbot.core.models import ExecutionRequest, ExecutionResult, RiskDecision

logger = logging.getLogger(__name__)


class ExecutionEngine:
    """Translate risk-approved intents into broker execution requests."""

    def __init__(self, *, broker: BaseBroker, minimum_bracket_reward_risk: float = 1.4) -> None:
        self.broker = broker
        self.minimum_bracket_reward_risk = minimum_bracket_reward_risk

    def execute(self, decision: RiskDecision, *, mode: RuntimeMode) -> ExecutionResult:
        if not decision.approved or decision.intent is None:
            return ExecutionResult(
                execution_skipped=True,
                reason=decision.reason or "risk_rejected",
            )

        intent = decision.intent.model_copy(deep=True)
        adjusted_intent, rejection_reason = self._apply_execution_constraints(intent)
        request = ExecutionRequest.from_intent(adjusted_intent or intent, mode)
        if rejection_reason is not None or adjusted_intent is None:
            return ExecutionResult.skipped(request=request, reason=rejection_reason or "execution_constraints_failed")
        if mode is RuntimeMode.DRY_RUN:
            return ExecutionResult.skipped(request=request, reason="dry_run_mode")

        if mode is RuntimeMode.LIVE:
            return ExecutionResult.skipped(
                request=request,
                reason="live_execution_disabled",
            )

        return self.broker.submit_order(request)

    def _apply_execution_constraints(self, intent):
        constraints = self.broker.get_execution_constraints()
        if intent.bracket_plan is None:
            return intent, None

        raw_quantity = float(intent.quantity)
        quantity = raw_quantity
        if constraints.whole_shares_only_for_brackets:
            quantity = float(math.floor(quantity))

        if quantity < constraints.minimum_quantity:
            return None, "invalid_broker_quantity"

        adjusted_plan = intent.bracket_plan.with_quantity(quantity)
        if (
            adjusted_plan.reward_risk_ratio < self.minimum_bracket_reward_risk
            or adjusted_plan.expected_net_profit <= 0
        ):
            return None, "bracket_plan_invalid_after_rounding"

        intent.quantity = quantity
        intent.bracket_plan = adjusted_plan
        intent.metadata["raw_quantity"] = raw_quantity
        intent.metadata["broker_quantity"] = quantity
        return intent, None
