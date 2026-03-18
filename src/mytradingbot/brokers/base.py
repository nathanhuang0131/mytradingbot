"""Broker interfaces and shared broker result models."""

from __future__ import annotations

import logging
from abc import ABC, abstractmethod

from mytradingbot.core.models import (
    BrokerBracketState,
    ExecutionConstraints,
    ExecutionRequest,
    ExecutionResult,
    FillEvent,
    MarketSnapshot,
    PositionSnapshot,
)

logger = logging.getLogger(__name__)


class BaseBroker(ABC):
    """Common broker adapter contract."""

    @abstractmethod
    def submit_order(self, request: ExecutionRequest) -> ExecutionResult:
        """Submit an execution request and return the resulting broker state."""

    @abstractmethod
    def list_orders(self) -> list:
        """Return tracked orders."""

    @abstractmethod
    def list_positions(self) -> list[PositionSnapshot]:
        """Return tracked positions."""

    @abstractmethod
    def list_fills(self) -> list[FillEvent]:
        """Return tracked fill events."""

    def get_execution_constraints(self) -> ExecutionConstraints:
        """Return broker-specific execution constraints."""

        return ExecutionConstraints()

    def process_market_snapshot(self, snapshot: MarketSnapshot) -> list[ExecutionResult]:
        """Process a market snapshot for managed synthetic orders."""

        return []

    def flatten_open_brackets(self, *, reason: str) -> list[ExecutionResult]:
        """Force-close managed synthetic bracket positions."""

        return []

    def list_brackets(self) -> list[BrokerBracketState]:
        """Return active or historical bracket state."""

        return []
