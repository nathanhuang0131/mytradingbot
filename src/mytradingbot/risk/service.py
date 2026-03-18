"""Risk engine for intent approval and phase-1 live gating."""

from __future__ import annotations

import logging

from mytradingbot.core.enums import RuntimeMode
from mytradingbot.core.models import RiskDecision, TradeIntent

logger = logging.getLogger(__name__)


class RiskEngine:
    """Evaluate trade intents before they reach execution."""

    def __init__(self, *, max_position_size: int = 10) -> None:
        self.max_position_size = max_position_size

    def evaluate(self, *, intent: TradeIntent, mode: RuntimeMode) -> RiskDecision:
        checks: list[str] = []

        if mode is RuntimeMode.LIVE:
            checks.append("live_mode_guard")
            return RiskDecision.reject(reason="live_mode_disabled", checks=checks)

        if intent.quantity <= 0:
            checks.append("positive_quantity_required")
            return RiskDecision.reject(reason="invalid_quantity", checks=checks)

        if intent.strategy_name == "scalping" and intent.side == "buy" and intent.bracket_plan is None:
            checks.append("bracket_plan_required")
            return RiskDecision.reject(reason="missing_bracket_plan", checks=checks)

        if intent.quantity > self.max_position_size:
            checks.append("max_position_size")
            return RiskDecision.reject(
                reason="max_position_size_exceeded",
                checks=checks,
            )

        checks.extend(["mode_allowed", "position_limit_ok"])
        if intent.bracket_plan is not None:
            checks.append("bracket_plan_present")
        return RiskDecision.approve(intent=intent, checks=checks)
