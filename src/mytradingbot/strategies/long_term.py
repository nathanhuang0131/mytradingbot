"""Long-term strategy implementation."""

from __future__ import annotations

import logging

from mytradingbot.core.models import SignalBundle, StrategyDecision
from mytradingbot.strategies.base import BaseStrategy

logger = logging.getLogger(__name__)


class LongTermStrategy(BaseStrategy):
    """Long-term position strategy."""

    name = "long_term"

    def evaluate(self, signal: SignalBundle) -> StrategyDecision:
        if signal.prediction.confidence < 0.45 or abs(signal.prediction.predicted_return) < 0.01:
            return StrategyDecision.reject(
                strategy_name=self.name,
                symbol=signal.symbol,
                reason="long_term_thresholds_not_met",
                failed_filters=["predicted_return_threshold", "confidence_threshold"],
            )

        return StrategyDecision.approve(
            strategy_name=self.name,
            symbol=signal.symbol,
            intent=self._intent_from_signal(signal, quantity=3),
            passed_filters=["predicted_return_threshold", "confidence_threshold"],
        )
