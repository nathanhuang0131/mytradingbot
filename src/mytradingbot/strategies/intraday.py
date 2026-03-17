"""Intraday strategy implementation."""

from __future__ import annotations

import logging

from mytradingbot.core.models import SignalBundle, StrategyDecision
from mytradingbot.strategies.base import BaseStrategy

logger = logging.getLogger(__name__)


class IntradayStrategy(BaseStrategy):
    """Simple intraday threshold strategy."""

    name = "intraday"

    def evaluate(self, signal: SignalBundle) -> StrategyDecision:
        if signal.prediction.confidence < 0.55 or abs(signal.prediction.predicted_return) < 0.004:
            return StrategyDecision.reject(
                strategy_name=self.name,
                symbol=signal.symbol,
                reason="intraday_thresholds_not_met",
                failed_filters=["predicted_return_threshold", "confidence_threshold"],
            )

        return StrategyDecision.approve(
            strategy_name=self.name,
            symbol=signal.symbol,
            intent=self._intent_from_signal(signal, quantity=1),
            passed_filters=["predicted_return_threshold", "confidence_threshold"],
        )
