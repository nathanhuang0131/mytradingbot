"""Strategy interfaces and shared helpers."""

from __future__ import annotations

import logging
from abc import ABC, abstractmethod

from mytradingbot.core.models import ExitPlan, SignalBundle, StrategyDecision, TradeIntent

logger = logging.getLogger(__name__)


class BaseStrategy(ABC):
    """Base contract for all strategies."""

    name: str

    @abstractmethod
    def evaluate(self, signal: SignalBundle) -> StrategyDecision:
        """Evaluate a single signal and return a typed decision."""

    def evaluate_many(self, signals: list[SignalBundle]) -> list[StrategyDecision]:
        """Evaluate multiple signals using the single-signal entrypoint."""

        return [self.evaluate(signal) for signal in signals]

    def _intent_from_signal(
        self,
        signal: SignalBundle,
        *,
        quantity: int,
        metadata: dict[str, float | str | bool] | None = None,
    ) -> TradeIntent:
        side = "buy" if signal.prediction.direction == "long" else "sell"
        return TradeIntent(
            symbol=signal.symbol,
            strategy_name=self.name,
            side=side,
            quantity=quantity,
            limit_price=signal.market.last_price,
            predicted_return=signal.prediction.predicted_return,
            confidence=signal.prediction.confidence,
            exit_plan=ExitPlan(),
            metadata=metadata or {},
        )
