"""Broker interfaces and shared broker result models."""

from __future__ import annotations

import logging
from abc import ABC, abstractmethod

from mytradingbot.core.models import ExecutionRequest, ExecutionResult, FillEvent, PositionSnapshot

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
