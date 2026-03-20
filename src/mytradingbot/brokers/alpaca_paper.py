"""Real Alpaca paper Trading API broker adapter with bot-owned-only reconciliation."""

from __future__ import annotations

from datetime import datetime, timezone
from decimal import Decimal, ROUND_HALF_UP
from types import SimpleNamespace
from typing import Any, Callable

from mytradingbot.brokers.base import BaseBroker
from mytradingbot.core.enums import RuntimeMode
from mytradingbot.core.models import (
    BrokerBracketState,
    BrokerOrder,
    ExecutionConstraints,
    ExecutionRequest,
    ExecutionResult,
    FillEvent,
    PositionSnapshot,
)
from mytradingbot.core.settings import AppSettings
from mytradingbot.runtime.models import (
    BrokerPreflightResult,
    BrokerReconciliationSnapshot,
    OwnershipClass,
    ObservedOrderRecord,
    ObservedPositionRecord,
    FillLifecycleRecord,
    OrderLifecycleRecord,
)
from mytradingbot.runtime.reconcile import OwnershipClassifier
from mytradingbot.runtime.store import RuntimeStateStore


class AlpacaPaperBroker(BaseBroker):
    """Broker adapter that submits real orders to Alpaca's paper Trading API."""

    def __init__(
        self,
        settings: AppSettings | None = None,
        *,
        runtime_store: RuntimeStateStore | None = None,
        trading_client_factory: Callable[[AppSettings], Any] | None = None,
    ) -> None:
        self.settings = settings or AppSettings()
        self.runtime_store = runtime_store or RuntimeStateStore(settings=self.settings)
        self._trading_client_factory = trading_client_factory or self._default_trading_client_factory
        self._client = None

    def preflight(self) -> BrokerPreflightResult:
        if not (self.settings.broker.alpaca_api_key and self.settings.broker.alpaca_secret_key):
            return BrokerPreflightResult(
                ok=False,
                message="Alpaca paper broker preflight failed because credentials are missing.",
                broker_mode="alpaca_paper_api",
                metadata={"api_base_url": self.settings.broker.alpaca_base_url},
            )
        if not self.settings.broker.resolved_external_submission_enabled():
            return BrokerPreflightResult(
                ok=False,
                message="Alpaca paper broker preflight failed because external broker submission is disabled.",
                broker_mode="alpaca_paper_api",
                metadata={"api_base_url": self.settings.broker.alpaca_base_url},
            )
        try:
            account = self.client.get_account()
        except Exception as exc:
            return BrokerPreflightResult(
                ok=False,
                message=f"Alpaca paper broker preflight failed: {exc}",
                broker_mode="alpaca_paper_api",
                metadata={"api_base_url": self.settings.broker.alpaca_base_url},
            )
        return BrokerPreflightResult(
            ok=True,
            message="Alpaca paper broker preflight passed.",
            broker_mode="alpaca_paper_api",
            metadata={
                "api_base_url": self.settings.broker.alpaca_base_url,
                "account_status": str(getattr(account, "status", "")),
                "buying_power": str(getattr(account, "buying_power", "")),
            },
        )

    @property
    def client(self):
        if self._client is None:
            self._client = self._trading_client_factory(self.settings)
        return self._client

    def get_execution_constraints(self) -> ExecutionConstraints:
        return ExecutionConstraints(whole_shares_only_for_brackets=True, minimum_quantity=1.0)

    def submit_order(self, request: ExecutionRequest) -> ExecutionResult:
        order_request = self._build_order_request(request)
        broker_order = self.client.submit_order(order_request)
        order_record = self._record_from_alpaca_order(broker_order, request=request)
        self.runtime_store.record_order(order_record)
        order = BrokerOrder(
            order_id=order_record.order_id,
            symbol=order_record.symbol,
            side=order_record.side,  # type: ignore[arg-type]
            quantity=order_record.quantity,
            mode=order_record.mode,
            client_order_id=order_record.client_order_id,
            status=self._broker_order_status(order_record.status),
            avg_fill_price=order_record.avg_fill_price,
            metadata=order_record.metadata,
            submitted_at=order_record.submitted_at,
        )
        fills: list[FillEvent] = []
        position = None
        if order_record.status == "filled" and order_record.avg_fill_price is not None:
            fill = FillEvent(
                order_id=order.order_id,
                symbol=order.symbol,
                quantity=order.quantity,
                price=order.avg_fill_price,
                metadata=order.metadata,
                filled_at=order_record.submitted_at,
            )
            fills.append(fill)
            self.runtime_store.record_fill(
                FillLifecycleRecord(
                    fill_id=fill.fill_id,
                    order_id=fill.order_id,
                    session_id=str(request.metadata.get("session_id", "")),
                    run_id=str(request.metadata.get("run_id", "")),
                    strategy=request.strategy_name,
                    mode=request.mode,
                    broker_mode="alpaca_paper_api",
                    ownership_class="bot_owned",
                    symbol=request.symbol,
                    quantity=request.quantity,
                    price=fill.price,
                    filled_at=fill.filled_at,
                    metadata=fill.metadata,
                )
            )
            position = PositionSnapshot(
                symbol=request.symbol,
                quantity=request.quantity if request.side == "buy" else -request.quantity,
                average_price=fill.price,
                market_price=fill.price,
                unrealized_pnl=0.0,
            )
            self.runtime_store.record_position(position)

        return ExecutionResult(
            request=request,
            order=order,
            fills=fills,
            position=position,
        )

    def list_orders(self) -> list:
        return self.runtime_store.list_orders()

    def list_positions(self) -> list[PositionSnapshot]:
        return self.runtime_store.list_positions()

    def list_fills(self) -> list[FillEvent]:
        return self.runtime_store.list_fills()

    def list_brackets(self) -> list[BrokerBracketState]:
        brackets: list[BrokerBracketState] = []
        active_positions = {
            position.symbol: position
            for position in self.runtime_store.list_positions()
            if abs(position.quantity) > 0
        }
        for order in self.runtime_store.list_order_records():
            if (
                order.broker_mode != "alpaca_paper_api"
                or order.ownership_class != "bot_owned"
                or order.side != "buy"
                or order.metadata.get("broker_order_class") != "bracket"
                or order.symbol not in active_positions
            ):
                continue
            bracket_payload = order.metadata.get("bracket_plan")
            if not isinstance(bracket_payload, dict):
                continue
            try:
                brackets.append(
                    BrokerBracketState(
                        symbol=order.symbol,
                        entry_order_id=order.order_id,
                        bracket_plan=ExecutionRequest(
                            symbol=order.symbol,
                            side="buy",
                            quantity=order.quantity,
                            strategy_name=order.strategy,
                            mode=order.mode,
                            limit_price=order.avg_fill_price,
                            bracket_plan=bracket_payload,
                        ).bracket_plan,
                    )
                )
            except Exception:
                continue
        return brackets

    def flatten_open_brackets(self, *, reason: str) -> list[ExecutionResult]:
        results: list[ExecutionResult] = []
        for position in self.runtime_store.list_positions():
            if abs(position.quantity) <= 0:
                continue
            close_order = self.client.close_position(position.symbol)
            order_record = self._record_from_alpaca_order(close_order)
            order_record.metadata["exit_reason"] = reason
            order_record.metadata["close_position_api"] = True
            self.runtime_store.record_order(order_record)
            results.append(
                ExecutionResult(
                    reason=reason,
                    order=BrokerOrder(
                        order_id=order_record.order_id,
                        symbol=order_record.symbol,
                        side=order_record.side,  # type: ignore[arg-type]
                        quantity=order_record.quantity,
                        mode=order_record.mode,
                        client_order_id=order_record.client_order_id,
                        status=self._broker_order_status(order_record.status),
                        avg_fill_price=order_record.avg_fill_price,
                        metadata=order_record.metadata,
                        submitted_at=order_record.submitted_at,
                    ),
                )
            )
        return results

    def reconcile_runtime_state(self, *, strategy_name: str) -> BrokerReconciliationSnapshot:
        from alpaca.trading.enums import QueryOrderStatus
        from alpaca.trading.requests import GetOrdersRequest

        known_orders = self.runtime_store.list_order_records()
        known_orders_by_id = {record.order_id: record for record in known_orders}
        classifier = OwnershipClassifier(
            known_client_order_ids={
                record.client_order_id
                for record in known_orders
                if record.client_order_id
            },
            known_order_ids={record.order_id for record in known_orders},
        )

        response_orders = self.client.get_orders(
            GetOrdersRequest(status=QueryOrderStatus.ALL, limit=200, nested=True)
        )
        flattened_orders = self._flatten_orders(response_orders)
        ownership_by_order_id: dict[str, OwnershipClass] = {}

        observed_orders: list[ObservedOrderRecord] = []
        bot_owned_symbols: set[str] = set()
        bot_owned_order_count = 0
        for item in flattened_orders:
            parent_order_id = item.get("parent_order_id")
            ownership_class = classifier.classify_order(
                item["order"],
                parent_ownership=ownership_by_order_id.get(parent_order_id) if parent_order_id else None,
            )
            order = item["order"]
            order_id = str(getattr(order, "id"))
            ownership_by_order_id[order_id] = ownership_class
            if ownership_class == "bot_owned":
                bot_owned_order_count += 1
                order_record = self._record_from_alpaca_order(
                    order,
                    existing_record=known_orders_by_id.get(order_id),
                )
                self.runtime_store.record_order(order_record)
                bot_owned_symbols.add(order_record.symbol)
                filled_qty = _float_or_zero(getattr(order, "filled_qty", None))
                avg_fill_price = _float_or_none(getattr(order, "filled_avg_price", None))
                filled_at = _datetime_or_none(getattr(order, "filled_at", None))
                if filled_qty > 0 and avg_fill_price is not None and filled_at is not None:
                    self.runtime_store.record_fill(
                        FillLifecycleRecord(
                            fill_id=f"{order_record.order_id}:{filled_at.isoformat()}",
                            order_id=order_record.order_id,
                            session_id=order_record.session_id,
                            run_id=order_record.run_id,
                            strategy=order_record.strategy,
                            mode=order_record.mode,
                            broker_mode="alpaca_paper_api",
                            ownership_class="bot_owned",
                            symbol=order_record.symbol,
                            quantity=filled_qty,
                            price=avg_fill_price,
                            filled_at=filled_at,
                            metadata=order_record.metadata,
                        )
                    )
                continue
            observed_orders.append(
                ObservedOrderRecord(
                    order_id=order_id,
                    broker_mode="alpaca_paper_api",
                    ownership_class=ownership_class,
                    symbol=str(getattr(order, "symbol", "")),
                    side=_enum_or_text(getattr(order, "side", None)),
                    quantity=_float_or_none(getattr(order, "qty", None)),
                    status=_enum_or_text(getattr(order, "status", None)),
                    client_order_id=(str(getattr(order, "client_order_id")) if getattr(order, "client_order_id", None) else None),
                    observed_at=_datetime_or_none(getattr(order, "submitted_at", None)) or datetime.now(timezone.utc),
                    source="alpaca_paper_account",
                    metadata={"ownership_management_class": classifier.management_class(ownership_class)},
                )
            )

        positions = self.client.get_all_positions()
        observed_positions: list[ObservedPositionRecord] = []
        bot_owned_position_count = 0
        foreign_position_count = 0
        for position in positions:
            symbol = str(getattr(position, "symbol"))
            ownership_class = classifier.classify_position(symbol=symbol, bot_owned_symbols=bot_owned_symbols)
            snapshot = PositionSnapshot(
                symbol=symbol,
                quantity=_float_or_zero(getattr(position, "qty", None)),
                average_price=_float_or_zero(getattr(position, "avg_entry_price", None)),
                market_price=_float_or_zero(getattr(position, "current_price", None)),
                unrealized_pnl=_float_or_zero(getattr(position, "unrealized_pl", None)),
            )
            if ownership_class == "bot_owned":
                bot_owned_position_count += 1
                self.runtime_store.record_position(snapshot)
                continue
            foreign_position_count += 1
            observed_positions.append(
                ObservedPositionRecord(
                    symbol=symbol,
                    broker_mode="alpaca_paper_api",
                    ownership_class=ownership_class,
                    quantity=snapshot.quantity,
                    average_price=snapshot.average_price,
                    market_price=snapshot.market_price,
                    observed_at=datetime.now(timezone.utc),
                    source="alpaca_paper_account",
                    metadata={"unrealized_pnl": snapshot.unrealized_pnl},
                )
            )

        self.runtime_store.replace_observed_orders(observed_orders)
        self.runtime_store.replace_observed_positions(observed_positions)
        return BrokerReconciliationSnapshot(
            broker_mode="alpaca_paper_api",
            ownership_policy=self.settings.broker.ownership_policy,
            bot_owned_order_count=bot_owned_order_count,
            bot_owned_position_count=bot_owned_position_count,
            foreign_order_count=len(observed_orders),
            foreign_position_count=foreign_position_count,
        )

    def _build_order_request(self, request: ExecutionRequest):
        from alpaca.trading.enums import OrderClass, OrderSide, TimeInForce
        from alpaca.trading.requests import MarketOrderRequest, StopLossRequest, TakeProfitRequest

        if request.bracket_plan is not None:
            if request.bracket_plan.planned_stop_loss_price >= request.bracket_plan.planned_entry_price:
                raise ValueError("Invalid long bracket: stop loss must be below entry for Alpaca paper bracket orders.")
            if request.bracket_plan.planned_take_profit_price <= request.bracket_plan.planned_entry_price:
                raise ValueError("Invalid long bracket: take profit must be above entry for Alpaca paper bracket orders.")
            take_profit_price = _normalize_price_for_alpaca(request.bracket_plan.planned_take_profit_price)
            stop_loss_price = _normalize_price_for_alpaca(request.bracket_plan.planned_stop_loss_price)
        else:
            take_profit_price = None
            stop_loss_price = None
        return MarketOrderRequest(
            symbol=request.symbol,
            qty=request.quantity,
            side=OrderSide.BUY if request.side == "buy" else OrderSide.SELL,
            time_in_force=TimeInForce.DAY,
            order_class=OrderClass.BRACKET if request.bracket_plan is not None else None,
            client_order_id=request.client_order_id,
            take_profit=(
                TakeProfitRequest(limit_price=take_profit_price)
                if request.bracket_plan is not None
                else None
            ),
            stop_loss=(
                StopLossRequest(stop_price=stop_loss_price)
                if request.bracket_plan is not None
                else None
            ),
        )

    def _record_from_alpaca_order(
        self,
        order,
        *,
        request: ExecutionRequest | None = None,
        existing_record: OrderLifecycleRecord | None = None,
    ) -> OrderLifecycleRecord:
        strategy_name = (
            request.strategy_name
            if request is not None
            else existing_record.strategy
            if existing_record is not None
            else str(getattr(order, "client_order_id", "scalping")).split("-")[0].lower()
        )
        submitted_at = _datetime_or_none(getattr(order, "submitted_at", None)) or datetime.now(timezone.utc)
        metadata = dict(existing_record.metadata) if existing_record is not None else {}
        if request is not None:
            metadata.update(request.metadata)
            if request.bracket_plan is not None:
                metadata["bracket_plan"] = request.bracket_plan.model_dump(mode="json")
        metadata.update(
            {
                "signal_source": (
                    str(getattr(request, "metadata", {}).get("signal_source"))
                    if request is not None and getattr(request, "metadata", {}).get("signal_source") is not None
                    else metadata.get("signal_source", "qlib_plus_rules")
                ),
                "broker_order_class": _enum_or_text(getattr(order, "order_class", None)),
            }
        )
        return OrderLifecycleRecord(
            order_id=str(getattr(order, "id")),
            session_id=(
                str(getattr(request, "metadata", {}).get("session_id", ""))
                if request is not None
                else (existing_record.session_id if existing_record is not None else "")
            ),
            run_id=(
                str(getattr(request, "metadata", {}).get("run_id", ""))
                if request is not None
                else (existing_record.run_id if existing_record is not None else "")
            ),
            strategy=strategy_name,
            mode=request.mode if request is not None else (existing_record.mode if existing_record is not None else RuntimeMode.PAPER),
            broker_mode="alpaca_paper_api",
            ownership_class="bot_owned",
            symbol=str(getattr(order, "symbol")),
            side=_enum_or_text(getattr(order, "side", None)) or "buy",
            quantity=_float_or_zero(getattr(order, "qty", None)),
            client_order_id=(str(getattr(order, "client_order_id")) if getattr(order, "client_order_id", None) else None),
            status=_enum_or_text(getattr(order, "status", None)) or "accepted",
            submitted_at=submitted_at,
            avg_fill_price=_float_or_none(getattr(order, "filled_avg_price", None)),
            metadata=metadata,
        )

    def _flatten_orders(self, orders: list[Any]) -> list[dict[str, Any]]:
        flattened: list[dict[str, Any]] = []

        def visit(order: Any, parent_order_id: str | None = None) -> None:
            flattened.append({"order": order, "parent_order_id": parent_order_id})
            for leg in list(getattr(order, "legs", []) or []):
                visit(leg, parent_order_id=str(getattr(order, "id", "")))

        for order in orders:
            visit(order)
        return flattened

    def _default_trading_client_factory(self, settings: AppSettings):
        from alpaca.trading.client import TradingClient

        return TradingClient(
            api_key=settings.broker.alpaca_api_key,
            secret_key=settings.broker.alpaca_secret_key,
            paper=True,
            url_override=settings.broker.alpaca_base_url,
        )

    @staticmethod
    def _broker_order_status(status: str) -> str:
        normalized = status.lower()
        if normalized == "filled":
            return "filled"
        if normalized in {"rejected", "canceled", "cancelled", "expired", "failed"}:
            return "rejected"
        return "accepted"


def _enum_or_text(value: Any) -> str | None:
    if value is None:
        return None
    if hasattr(value, "value"):
        return str(value.value)
    return str(value)


def _float_or_none(value: Any) -> float | None:
    if value in (None, ""):
        return None
    return float(value)


def _float_or_zero(value: Any) -> float:
    return float(value) if value not in (None, "") else 0.0


def _datetime_or_none(value: Any) -> datetime | None:
    if value is None:
        return None
    if isinstance(value, datetime):
        return value if value.tzinfo is not None else value.replace(tzinfo=timezone.utc)
    try:
        parsed = datetime.fromisoformat(str(value).replace("Z", "+00:00"))
    except ValueError:
        return None
    return parsed if parsed.tzinfo is not None else parsed.replace(tzinfo=timezone.utc)


def _normalize_price_for_alpaca(value: float) -> float:
    precision = Decimal("0.01") if abs(value) >= 1 else Decimal("0.0001")
    return float(Decimal(str(value)).quantize(precision, rounding=ROUND_HALF_UP))
