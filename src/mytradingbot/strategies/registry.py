"""Strategy registry and canonical mapping."""

from __future__ import annotations

import logging

from mytradingbot.core.settings import AppSettings
from mytradingbot.strategies.base import BaseStrategy
from mytradingbot.strategies.intraday import IntradayStrategy
from mytradingbot.strategies.long_term import LongTermStrategy
from mytradingbot.strategies.scalping import ScalpingStrategy
from mytradingbot.strategies.short_term import ShortTermStrategy

logger = logging.getLogger(__name__)


class StrategyRegistry:
    """Lookup table for supported strategy instances."""

    def __init__(self, strategies: dict[str, BaseStrategy]) -> None:
        self._strategies = strategies

    @classmethod
    def build_default(cls, settings: AppSettings | None = None) -> "StrategyRegistry":
        return cls(
            strategies={
                "scalping": ScalpingStrategy(settings=settings),
                "intraday": IntradayStrategy(),
                "short_term": ShortTermStrategy(),
                "long_term": LongTermStrategy(),
            }
        )

    def names(self) -> list[str]:
        return sorted(self._strategies.keys())

    def get(self, strategy_name: str) -> BaseStrategy:
        return self._strategies[strategy_name]
