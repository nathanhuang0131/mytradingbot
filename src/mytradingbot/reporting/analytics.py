"""Closed-trade analytics exports derived from persisted truthful fills."""

from __future__ import annotations

import csv
from collections import defaultdict, deque
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path

from pydantic import BaseModel

from mytradingbot.analytics.fees import BrokerFeeSchedule, FeeCalculationInput, calculate_trade_fees
from mytradingbot.core.settings import AppSettings
from mytradingbot.runtime.models import (
    BrokerMode,
    DecisionAuditRecord,
    FillLifecycleRecord,
    OwnershipClass,
    OrderLifecycleRecord,
    broker_mode_description,
)
from mytradingbot.runtime.store import RuntimeStateStore


class ClosedTradeRow(BaseModel):
    symbol: str
    strategy: str
    broker_mode: BrokerMode = "local_paper"
    ownership_class: OwnershipClass = "bot_owned"
    signal_source: str
    entry_ts: datetime
    exit_ts: datetime
    entry_price: float
    exit_price: float
    qty: float
    gross_pnl: float
    commission_fee: float
    sec_fee: float
    taf_fee: float
    cat_fee: float
    borrow_fee: float
    margin_interest: float
    allocated_data_cost: float
    net_pnl_after_fees: float
    net_pnl_after_fees_and_platform_cost: float
    fee_schedule_version: str
    fee_schedule_effective_date: str
    realized_pnl: float
    realized_return_pct: float
    win_loss_flag: str
    session_id: str
    run_id: str
    exit_session_id: str | None = None
    exit_run_id: str | None = None
    entry_order_id: str
    exit_order_id: str
    exit_reason: str | None = None


class PnLAttributionRow(BaseModel):
    broker_mode: BrokerMode = "local_paper"
    dimension: str
    value: str
    closed_trade_count: int
    win_count: int
    loss_count: int
    flat_count: int
    total_realized_pnl: float
    total_net_pnl_after_fees: float
    total_net_pnl_after_fees_and_platform_cost: float
    average_realized_pnl: float
    average_realized_return_pct: float
    win_rate: float
    ownership_class: OwnershipClass = "bot_owned"
    fee_schedule_version: str = ""
    excluded_foreign_position_count: int = 0


@dataclass
class _OpenLot:
    symbol: str
    strategy: str
    broker_mode: BrokerMode
    ownership_class: OwnershipClass
    signal_source: str
    session_id: str
    run_id: str
    entry_order_id: str
    entry_ts: datetime
    entry_price: float
    remaining_qty: float


class RealizedAnalyticsExporter:
    """Materialize rolling realized-PnL exports from persisted runtime state."""

    def __init__(
        self,
        settings: AppSettings | None = None,
        *,
        store: RuntimeStateStore | None = None,
    ) -> None:
        self.settings = settings or AppSettings()
        self.store = store or RuntimeStateStore(settings=self.settings)

    def write(self) -> list[str]:
        closed_trades = self.build_closed_trades()
        attribution_rows = self.build_attribution_rows(closed_trades)
        closed_path = self._write_csv(
            self.settings.paths.reports_analytics_dir / "closed_trades.csv",
            [row.model_dump(mode="json") for row in closed_trades],
            fieldnames=list(ClosedTradeRow.model_fields.keys()),
        )
        attribution_path = self._write_csv(
            self.settings.paths.reports_analytics_dir / "pnl_attribution.csv",
            [row.model_dump(mode="json") for row in attribution_rows],
            fieldnames=list(PnLAttributionRow.model_fields.keys()),
        )
        summary_path = self._write_summary(
            self.settings.paths.reports_analytics_dir / "pnl_summary.md",
            closed_trades=closed_trades,
            attribution_rows=attribution_rows,
        )
        return [str(closed_path), str(attribution_path), str(summary_path)]

    def build_closed_trades(self) -> list[ClosedTradeRow]:
        orders = self.store.list_order_records()
        fills = self.store.list_fill_records()
        decisions = self.store.list_decisions()
        fills_by_order = self._fills_by_order(fills)
        decisions_by_session_symbol = self._decisions_by_session_symbol(decisions)
        open_lots: dict[tuple[str, str], deque[_OpenLot]] = defaultdict(deque)
        closed_trades: list[ClosedTradeRow] = []

        for order in sorted(orders, key=lambda item: item.submitted_at):
            aggregate = fills_by_order.get(order.order_id)
            if aggregate is None or aggregate.quantity <= 0:
                continue

            key = (order.symbol, order.strategy)
            if order.side == "buy":
                open_lots[key].append(
                    _OpenLot(
                        symbol=order.symbol,
                        strategy=order.strategy,
                        broker_mode=order.broker_mode,
                        ownership_class=order.ownership_class,
                        signal_source=self._resolve_signal_source(order, decisions_by_session_symbol),
                        session_id=order.session_id,
                        run_id=order.run_id,
                        entry_order_id=order.order_id,
                        entry_ts=aggregate.filled_at,
                        entry_price=aggregate.price,
                        remaining_qty=aggregate.quantity,
                    )
                )
                continue

            if order.side != "sell":
                continue

            remaining_quantity = aggregate.quantity
            while remaining_quantity > 0 and open_lots[key]:
                lot = open_lots[key][0]
                matched_quantity = min(remaining_quantity, lot.remaining_qty)
                fee_breakdown = calculate_trade_fees(
                    FeeCalculationInput(
                        quantity=matched_quantity,
                        entry_price=lot.entry_price,
                        exit_price=aggregate.price,
                        holding_days=max(0, (aggregate.filled_at.date() - lot.entry_ts.date()).days),
                        is_short=False,
                    ),
                    schedule=self._fee_schedule(),
                    allocation_mode=self.settings.broker_fees.fee_allocation_mode,
                    monthly_trade_count=max(1, len(orders)),
                )
                realized_pnl = fee_breakdown.gross_pnl
                realized_return_pct = (
                    ((aggregate.price - lot.entry_price) / lot.entry_price) * 100
                    if lot.entry_price
                    else 0.0
                )
                win_loss_flag = "flat"
                if realized_pnl > 0:
                    win_loss_flag = "win"
                elif realized_pnl < 0:
                    win_loss_flag = "loss"
                closed_trades.append(
                    ClosedTradeRow(
                        symbol=order.symbol,
                        strategy=order.strategy,
                        broker_mode=lot.broker_mode,
                        ownership_class=lot.ownership_class,
                        signal_source=lot.signal_source,
                        entry_ts=lot.entry_ts,
                        exit_ts=aggregate.filled_at,
                        entry_price=lot.entry_price,
                        exit_price=aggregate.price,
                        qty=matched_quantity,
                        gross_pnl=fee_breakdown.gross_pnl,
                        commission_fee=fee_breakdown.commission_fee,
                        sec_fee=fee_breakdown.sec_fee,
                        taf_fee=fee_breakdown.taf_fee,
                        cat_fee=fee_breakdown.cat_fee,
                        borrow_fee=fee_breakdown.borrow_fee,
                        margin_interest=fee_breakdown.margin_interest,
                        allocated_data_cost=fee_breakdown.allocated_data_cost,
                        net_pnl_after_fees=fee_breakdown.net_pnl_after_fees,
                        net_pnl_after_fees_and_platform_cost=fee_breakdown.net_pnl_after_fees_and_platform_cost,
                        fee_schedule_version=fee_breakdown.fee_schedule_version,
                        fee_schedule_effective_date=fee_breakdown.fee_schedule_effective_date,
                        realized_pnl=realized_pnl,
                        realized_return_pct=realized_return_pct,
                        win_loss_flag=win_loss_flag,
                        session_id=lot.session_id,
                        run_id=lot.run_id,
                        exit_session_id=order.session_id,
                        exit_run_id=order.run_id,
                        entry_order_id=lot.entry_order_id,
                        exit_order_id=order.order_id,
                        exit_reason=str(order.metadata.get("exit_reason")) if order.metadata.get("exit_reason") is not None else None,
                    )
                )
                lot.remaining_qty -= matched_quantity
                remaining_quantity -= matched_quantity
                if lot.remaining_qty <= 0:
                    open_lots[key].popleft()

        return closed_trades

    def build_attribution_rows(self, closed_trades: list[ClosedTradeRow]) -> list[PnLAttributionRow]:
        rows: list[PnLAttributionRow] = []
        bot_owned_trades = [
            trade for trade in closed_trades if trade.ownership_class == "bot_owned"
        ]
        excluded_foreign_position_count = len(
            [
                position
                for position in self.store.list_observed_positions()
                if position.ownership_class in {"foreign", "unknown"}
            ]
        )
        for dimension in ("symbol", "strategy", "signal_source", "broker_mode"):
            grouped: dict[tuple[BrokerMode, str, OwnershipClass], list[ClosedTradeRow]] = defaultdict(list)
            for trade in bot_owned_trades:
                broker_mode = trade.broker_mode
                value = str(getattr(trade, dimension))
                grouped[(broker_mode, value, trade.ownership_class)].append(trade)
            for (broker_mode, value, ownership_class), trades in sorted(grouped.items()):
                win_count = len([trade for trade in trades if trade.win_loss_flag == "win"])
                loss_count = len([trade for trade in trades if trade.win_loss_flag == "loss"])
                flat_count = len([trade for trade in trades if trade.win_loss_flag == "flat"])
                trade_count = len(trades)
                total_pnl = sum(trade.realized_pnl for trade in trades)
                total_net_after_fees = sum(trade.net_pnl_after_fees for trade in trades)
                total_net_after_fees_and_platform_cost = sum(
                    trade.net_pnl_after_fees_and_platform_cost for trade in trades
                )
                average_pnl = total_pnl / trade_count if trade_count else 0.0
                average_return_pct = (
                    sum(trade.realized_return_pct for trade in trades) / trade_count
                    if trade_count
                    else 0.0
                )
                rows.append(
                    PnLAttributionRow(
                        broker_mode=broker_mode,
                        dimension=dimension,
                        value=value,
                        closed_trade_count=trade_count,
                        win_count=win_count,
                        loss_count=loss_count,
                        flat_count=flat_count,
                        total_realized_pnl=total_pnl,
                        total_net_pnl_after_fees=total_net_after_fees,
                        total_net_pnl_after_fees_and_platform_cost=total_net_after_fees_and_platform_cost,
                        average_realized_pnl=average_pnl,
                        average_realized_return_pct=average_return_pct,
                        win_rate=(win_count / trade_count) if trade_count else 0.0,
                        ownership_class=ownership_class,
                        fee_schedule_version=trades[0].fee_schedule_version if trades else "",
                        excluded_foreign_position_count=excluded_foreign_position_count,
                    )
                )
        return rows

    @staticmethod
    def _fills_by_order(
        fills: list[FillLifecycleRecord],
    ) -> dict[str, FillLifecycleRecord]:
        grouped: dict[str, list[FillLifecycleRecord]] = defaultdict(list)
        for fill in fills:
            grouped[fill.order_id].append(fill)

        aggregates: dict[str, FillLifecycleRecord] = {}
        for order_id, order_fills in grouped.items():
            total_quantity = sum(fill.quantity for fill in order_fills)
            if total_quantity <= 0:
                continue
            weighted_price = sum(fill.quantity * fill.price for fill in order_fills) / total_quantity
            aggregates[order_id] = FillLifecycleRecord(
                fill_id=order_fills[-1].fill_id,
                order_id=order_id,
                session_id=order_fills[-1].session_id,
                run_id=order_fills[-1].run_id,
                strategy=order_fills[-1].strategy,
                mode=order_fills[-1].mode,
                symbol=order_fills[-1].symbol,
                quantity=total_quantity,
                price=weighted_price,
                filled_at=max(fill.filled_at for fill in order_fills),
                metadata=order_fills[-1].metadata,
            )
        return aggregates

    @staticmethod
    def _decisions_by_session_symbol(
        decisions: list[DecisionAuditRecord],
    ) -> dict[tuple[str, str], list[DecisionAuditRecord]]:
        grouped: dict[tuple[str, str], list[DecisionAuditRecord]] = defaultdict(list)
        for decision in decisions:
            if not decision.final_decision_status.startswith("accepted"):
                continue
            grouped[(decision.session_id, decision.symbol)].append(decision)
        for items in grouped.values():
            items.sort(key=lambda item: item.timestamp)
        return grouped

    @staticmethod
    def _resolve_signal_source(
        order: OrderLifecycleRecord,
        decisions_by_session_symbol: dict[tuple[str, str], list[DecisionAuditRecord]],
    ) -> str:
        signal_source = order.metadata.get("signal_source")
        if signal_source is not None:
            return str(signal_source)
        candidates = decisions_by_session_symbol.get((order.session_id, order.symbol), [])
        if not candidates:
            return "no_valid_signal"
        closest = min(
            candidates,
            key=lambda candidate: abs((candidate.timestamp - order.submitted_at).total_seconds()),
        )
        return closest.signal_source

    @staticmethod
    def _write_csv(path: Path, rows: list[dict], *, fieldnames: list[str]) -> Path:
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open("w", encoding="utf-8", newline="") as handle:
            writer = csv.DictWriter(handle, fieldnames=fieldnames)
            writer.writeheader()
            for row in rows:
                writer.writerow(row)
        return path

    def _write_summary(
        self,
        path: Path,
        *,
        closed_trades: list[ClosedTradeRow],
        attribution_rows: list[PnLAttributionRow],
    ) -> Path:
        lines = [
            "# Realized PnL Summary",
            "",
            f"- closed trades: `{len(closed_trades)}`",
            f"- total realized pnl: `{sum(trade.realized_pnl for trade in closed_trades):.4f}`",
            f"- total wins: `{len([trade for trade in closed_trades if trade.win_loss_flag == 'win'])}`",
            f"- broker_modes_present: `{', '.join(sorted({trade.broker_mode for trade in closed_trades}) or {'local_paper'})}`",
            f"- fee_schedule_version: `{self.settings.broker_fees.fee_schedule_version}`",
            "",
        ]
        present_modes = sorted({trade.broker_mode for trade in closed_trades}) or ["local_paper"]
        lines.extend(
            [
                f"- {mode}: `{broker_mode_description(mode)}`"
                for mode in present_modes
            ]
        )
        if "local_paper" in present_modes:
            lines.append(
                "- local_paper note: local paper broker analytics come from repo-local SQLite/runtime state, not the Alpaca paper account UI."
            )
        if self.store.list_observed_positions():
            lines.append(
                f"- foreign exposure: `{len(self.store.list_observed_positions())}` observed non-bot position snapshots are excluded from bot profitability attribution."
            )
        if self.store.list_observed_orders():
            lines.append(
                f"- foreign open orders: `{len(self.store.list_observed_orders())}` read-only broker-account orders are excluded from bot trade attribution."
            )
        lines.append(
            "- profitability scope: by default, only bot-owned closed trades are included in strategy, signal-source, and broker-mode profitability tables."
        )
        lines.append("")
        if not closed_trades:
            lines.append("- No closed trades have been materialized from persisted fills yet.")
        else:
            lines.extend(
                self._render_dimension_summary(
                    title="By Symbol",
                    rows=[row for row in attribution_rows if row.dimension == "symbol"],
                )
            )
            lines.extend(
                self._render_dimension_summary(
                    title="By Strategy",
                    rows=[row for row in attribution_rows if row.dimension == "strategy"],
                )
            )
            lines.extend(
                self._render_dimension_summary(
                    title="By Signal Source",
                    rows=[row for row in attribution_rows if row.dimension == "signal_source"],
                )
            )
            lines.extend(
                self._render_dimension_summary(
                    title="By Broker Mode",
                    rows=[row for row in attribution_rows if row.dimension == "broker_mode"],
                )
            )
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text("\n".join(lines) + "\n", encoding="utf-8")
        return path

    @staticmethod
    def _render_dimension_summary(*, title: str, rows: list[PnLAttributionRow]) -> list[str]:
        lines = [
            f"## {title}",
            "",
            "| Broker Mode | Value | Trades | Total PnL | Win Rate | Avg Return % |",
            "| --- | --- | ---: | ---: | ---: | ---: |",
        ]
        for row in rows:
            lines.append(
                f"| {row.broker_mode} | {row.value} | {row.closed_trade_count} | {row.total_realized_pnl:.4f} | "
                f"{row.win_rate:.2%} | {row.average_realized_return_pct:.4f} |"
            )
        lines.append("")
        return lines

    def _fee_schedule(self) -> BrokerFeeSchedule:
        return BrokerFeeSchedule(
            fee_schedule_version=self.settings.broker_fees.fee_schedule_version,
            fee_schedule_effective_date=self.settings.broker_fees.fee_schedule_effective_date,
            commission_per_order=self.settings.broker_fees.commission_per_order,
            sec_sell_rate_per_dollar=self.settings.broker_fees.sec_sell_rate_per_dollar,
            taf_sell_per_share=self.settings.broker_fees.taf_sell_per_share,
            taf_cap_per_trade=self.settings.broker_fees.taf_cap_per_trade,
            cat_per_share=self.settings.broker_fees.cat_per_share,
            monthly_data_plan_usd=self.settings.broker_fees.monthly_data_plan_usd,
            margin_rate_annual=self.settings.broker_fees.margin_rate_annual,
        )
