"""Short-term strategy implementation."""

from __future__ import annotations

import logging

from mytradingbot.core.models import SignalBundle, StrategyDecision
from mytradingbot.strategies.base import BaseStrategy

logger = logging.getLogger(__name__)


class ShortTermStrategy(BaseStrategy):
    """Short-term swing style threshold strategy."""

    name = "short_term"

    def evaluate(self, signal: SignalBundle) -> StrategyDecision:
        if signal.prediction.confidence < 0.5 or abs(signal.prediction.predicted_return) < 0.006:
            return StrategyDecision.reject(
                strategy_name=self.name,
                symbol=signal.symbol,
                reason="short_term_thresholds_not_met",
                failed_filters=["predicted_return_threshold", "confidence_threshold"],
            )

        return StrategyDecision.approve(
            strategy_name=self.name,
            symbol=signal.symbol,
            intent=self._intent_from_signal(signal, quantity=2),
            passed_filters=["predicted_return_threshold", "confidence_threshold"],
        )
