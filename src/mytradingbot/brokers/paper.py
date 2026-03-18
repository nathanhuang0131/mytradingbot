"""In-memory paper broker for the phase-1 operational path."""

from __future__ import annotations

import logging

from mytradingbot.brokers.base import BaseBroker
from mytradingbot.core.enums import RuntimeMode
from mytradingbot.core.models import (
    BrokerBracketState,
    BrokerOrder,
    ExecutionConstraints,
    ExecutionRequest,
    ExecutionResult,
    FillEvent,
    MarketSnapshot,
    PositionSnapshot,
)

logger = logging.getLogger(__name__)


class PaperBroker(BaseBroker):
    """Simple in-memory paper broker with immediate simulated fills."""

    def __init__(self) -> None:
        self._orders: list[BrokerOrder] = []
        self._fills: list[FillEvent] = []
        self._positions: dict[str, PositionSnapshot] = {}
        self._brackets: dict[str, BrokerBracketState] = {}

    def submit_order(self, request: ExecutionRequest) -> ExecutionResult:
        fill_price = request.limit_price or 0.0
        order = BrokerOrder(
            symbol=request.symbol,
            side=request.side,
            quantity=request.quantity,
            mode=request.mode,
            status="filled",
            avg_fill_price=fill_price,
            metadata={"strategy_name": request.strategy_name},
        )
        fill = FillEvent(
            order_id=order.order_id,
            symbol=request.symbol,
            quantity=request.quantity,
            price=fill_price,
        )
        position = self._update_position(request, fill_price)
        bracket_state = None
        if request.bracket_plan is not None and request.side == "buy":
            bracket_state = BrokerBracketState(
                symbol=request.symbol,
                entry_order_id=order.order_id,
                bracket_plan=request.bracket_plan.with_quantity(request.quantity),
            )
            self._brackets[request.symbol] = bracket_state

        self._orders.append(order)
        self._fills.append(fill)

        return ExecutionResult(
            request=request,
            order=order,
            fills=[fill],
            position=position,
            bracket_state=bracket_state,
        )

    def list_orders(self) -> list[BrokerOrder]:
        return list(self._orders)

    def list_positions(self) -> list[PositionSnapshot]:
        return list(self._positions.values())

    def list_fills(self) -> list[FillEvent]:
        return list(self._fills)

    def get_execution_constraints(self) -> ExecutionConstraints:
        return ExecutionConstraints(whole_shares_only_for_brackets=True, minimum_quantity=1.0)

    def process_market_snapshot(self, snapshot: MarketSnapshot) -> list[ExecutionResult]:
        bracket = self._brackets.get(snapshot.symbol)
        if bracket is None or bracket.status != "armed":
            return []

        plan = bracket.bracket_plan
        if snapshot.last_price >= plan.planned_take_profit_price:
            return [self._close_bracket(snapshot.symbol, price=snapshot.last_price, reason="take_profit")]
        if snapshot.last_price <= plan.planned_stop_loss_price:
            return [self._close_bracket(snapshot.symbol, price=snapshot.last_price, reason="stop_loss")]
        return []

    def flatten_open_brackets(self, *, reason: str) -> list[ExecutionResult]:
        results: list[ExecutionResult] = []
        for symbol, bracket in list(self._brackets.items()):
            if bracket.status != "armed":
                continue
            market_price = self._positions.get(symbol).market_price if symbol in self._positions else bracket.bracket_plan.planned_entry_price
            results.append(self._close_bracket(symbol, price=market_price, reason=reason))
        return results

    def list_brackets(self) -> list[BrokerBracketState]:
        return list(self._brackets.values())

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

    def _close_bracket(self, symbol: str, *, price: float, reason: str) -> ExecutionResult:
        bracket = self._brackets[symbol]
        position = self._positions.get(symbol)
        quantity = abs(position.quantity) if position else bracket.bracket_plan.planned_quantity
        mode = self._orders[-1].mode if self._orders else RuntimeMode.PAPER
        request = ExecutionRequest(
            symbol=symbol,
            side="sell",
            quantity=quantity,
            strategy_name="scalping",
            mode=mode,
            limit_price=price,
            metadata={"exit_reason": reason},
        )
        order = BrokerOrder(
            symbol=symbol,
            side="sell",
            quantity=quantity,
            mode=mode,
            status="filled",
            avg_fill_price=price,
            metadata={"exit_reason": reason},
        )
        fill = FillEvent(
            order_id=order.order_id,
            symbol=symbol,
            quantity=quantity,
            price=price,
            metadata={"exit_reason": reason},
        )
        updated_position = self._update_position(request, price)
        realized_pnl = (price - bracket.bracket_plan.planned_entry_price) * quantity
        bracket.status = "closed"
        bracket.closed_at = fill.filled_at
        bracket.exit_reason = reason
        bracket.exit_order_id = order.order_id
        bracket.realized_pnl = realized_pnl

        self._orders.append(order)
        self._fills.append(fill)
        return ExecutionResult(
            reason=reason,
            request=request,
            order=order,
            fills=[fill],
            position=updated_position,
            bracket_state=bracket,
            realized_pnl=realized_pnl,
        )
