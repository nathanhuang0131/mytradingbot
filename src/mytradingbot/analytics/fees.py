"""Broker-aware fee calculations for realized trade analytics."""

from __future__ import annotations

from pydantic import BaseModel

from mytradingbot.analytics.costs import allocate_monthly_data_cost


class BrokerFeeSchedule(BaseModel):
    fee_schedule_version: str
    fee_schedule_effective_date: str
    commission_per_order: float
    sec_sell_rate_per_dollar: float
    taf_sell_per_share: float
    taf_cap_per_trade: float
    cat_per_share: float
    monthly_data_plan_usd: float
    margin_rate_annual: float


class FeeCalculationInput(BaseModel):
    quantity: float
    entry_price: float
    exit_price: float
    holding_days: int = 0
    is_short: bool = False


class TradeFeeBreakdown(BaseModel):
    fee_schedule_version: str
    fee_schedule_effective_date: str
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


def calculate_trade_fees(
    trade: FeeCalculationInput,
    *,
    schedule: BrokerFeeSchedule,
    allocation_mode: str,
    monthly_trade_count: int | None = None,
) -> TradeFeeBreakdown:
    quantity = float(trade.quantity)
    gross_pnl = (
        (trade.entry_price - trade.exit_price) * quantity
        if trade.is_short
        else (trade.exit_price - trade.entry_price) * quantity
    )
    sell_principal = (
        trade.entry_price * quantity
        if trade.is_short
        else trade.exit_price * quantity
    )
    commission_fee = schedule.commission_per_order * 2
    sec_fee = sell_principal * schedule.sec_sell_rate_per_dollar
    taf_fee = min(quantity * schedule.taf_sell_per_share, schedule.taf_cap_per_trade)
    cat_fee = quantity * schedule.cat_per_share
    borrow_fee = 0.0
    margin_interest = 0.0
    if trade.is_short and trade.holding_days > 0:
        borrow_fee = (sell_principal * schedule.margin_rate_annual / 360.0) * trade.holding_days
    direct_fees = commission_fee + sec_fee + taf_fee + cat_fee + borrow_fee + margin_interest
    allocated_data_cost = allocate_monthly_data_cost(
        monthly_data_plan_usd=schedule.monthly_data_plan_usd,
        allocation_mode=allocation_mode,
        monthly_trade_count=monthly_trade_count,
    )
    net_pnl_after_fees = gross_pnl - direct_fees
    net_pnl_after_fees_and_platform_cost = net_pnl_after_fees - allocated_data_cost
    return TradeFeeBreakdown(
        fee_schedule_version=schedule.fee_schedule_version,
        fee_schedule_effective_date=schedule.fee_schedule_effective_date,
        gross_pnl=gross_pnl,
        commission_fee=commission_fee,
        sec_fee=sec_fee,
        taf_fee=taf_fee,
        cat_fee=cat_fee,
        borrow_fee=borrow_fee,
        margin_interest=margin_interest,
        allocated_data_cost=allocated_data_cost,
        net_pnl_after_fees=net_pnl_after_fees,
        net_pnl_after_fees_and_platform_cost=net_pnl_after_fees_and_platform_cost,
    )
