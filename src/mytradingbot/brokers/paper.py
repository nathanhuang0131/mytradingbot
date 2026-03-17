"""In-memory paper broker for the phase-1 operational path."""

from __future__ import annotations

import logging

from mytradingbot.brokers.base import BaseBroker
from mytradingbot.core.models import (
    BrokerOrder,
    ExecutionRequest,
    ExecutionResult,
    FillEvent,
    PositionSnapshot,
)

logger = logging.getLogger(__name__)


class PaperBroker(BaseBroker):
    """Simple in-memory paper broker with immediate simulated fills."""

    def __init__(self) -> None:
        self._orders: list[BrokerOrder] = []
        self._fills: list[FillEvent] = []
        self._positions: dict[str, PositionSnapshot] = {}

    def submit_order(self, request: ExecutionRequest) -> ExecutionResult:
        fill_price = request.limit_price or 0.0
        order = BrokerOrder(
            symbol=request.symbol,
            side=request.side,
            quantity=request.quantity,
            mode=request.mode,
            status="filled",
            avg_fill_price=fill_price,
        )
        fill = FillEvent(
            order_id=order.order_id,
            symbol=request.symbol,
            quantity=request.quantity,
            price=fill_price,
        )
        position = self._update_position(request, fill_price)

        self._orders.append(order)
        self._fills.append(fill)

        return ExecutionResult(
            request=request,
            order=order,
            fills=[fill],
            position=position,
        )

    def list_orders(self) -> list[BrokerOrder]:
        return list(self._orders)

    def list_positions(self) -> list[PositionSnapshot]:
        return list(self._positions.values())

    def list_fills(self) -> list[FillEvent]:
        return list(self._fills)

    def _update_position(self, request: ExecutionRequest, fill_price: float) -> PositionSnapshot:
        signed_quantity = request.quantity if request.side == "buy" else -request.quantity
        existing = self._positions.get(request.symbol)
        if existing is None:
            position = PositionSnapshot(
                symbol=request.symbol,
                quantity=signed_quantity,
                average_price=fill_price,
                market_price=fill_price,
                unrealized_pnl=0.0,
            )
        else:
            new_quantity = existing.quantity + signed_quantity
            if new_quantity == 0:
                position = PositionSnapshot(
                    symbol=request.symbol,
                    quantity=0,
                    average_price=fill_price,
                    market_price=fill_price,
                    unrealized_pnl=0.0,
                )
            else:
                weighted_cost = (existing.average_price * existing.quantity) + (
                    fill_price * signed_quantity
                )
                average_price = weighted_cost / new_quantity
                position = PositionSnapshot(
                    symbol=request.symbol,
                    quantity=new_quantity,
                    average_price=average_price,
                    market_price=fill_price,
                    unrealized_pnl=0.0,
                )

        self._positions[request.symbol] = position
        return position
