from __future__ import annotations


def test_fee_model_calculates_alpaca_style_direct_fees_for_closed_trade() -> None:
    from mytradingbot.analytics.fees import BrokerFeeSchedule, FeeCalculationInput, calculate_trade_fees

    schedule = BrokerFeeSchedule(
        fee_schedule_version="alpaca_public_schedule_test",
        fee_schedule_effective_date="2026-03-20",
        commission_per_order=0.0,
        sec_sell_rate_per_dollar=0.0,
        taf_sell_per_share=0.000166,
        taf_cap_per_trade=8.30,
        cat_per_share=0.0000265,
        monthly_data_plan_usd=99.0,
        margin_rate_annual=0.0625,
    )

    fees = calculate_trade_fees(
        FeeCalculationInput(
            quantity=100,
            entry_price=100.0,
            exit_price=101.0,
            holding_days=0,
            is_short=False,
        ),
        schedule=schedule,
        allocation_mode="trading_fees_only",
    )

    assert fees.commission_fee == 0.0
    assert fees.taf_fee > 0
    assert fees.cat_fee > 0
    assert fees.allocated_data_cost == 0.0
    assert fees.fee_schedule_version == "alpaca_public_schedule_test"


def test_fee_model_supports_fully_loaded_monthly_data_cost_allocation() -> None:
    from mytradingbot.analytics.fees import BrokerFeeSchedule, FeeCalculationInput, calculate_trade_fees

    schedule = BrokerFeeSchedule(
        fee_schedule_version="alpaca_public_schedule_test",
        fee_schedule_effective_date="2026-03-20",
        commission_per_order=0.0,
        sec_sell_rate_per_dollar=0.0,
        taf_sell_per_share=0.000166,
        taf_cap_per_trade=8.30,
        cat_per_share=0.0000265,
        monthly_data_plan_usd=99.0,
        margin_rate_annual=0.0625,
    )

    fees = calculate_trade_fees(
        FeeCalculationInput(
            quantity=100,
            entry_price=100.0,
            exit_price=101.0,
            holding_days=1,
            is_short=False,
        ),
        schedule=schedule,
        allocation_mode="fully_loaded_with_allocated_monthly_data_cost",
        monthly_trade_count=99,
    )

    assert fees.allocated_data_cost == 1.0
    assert fees.net_pnl_after_fees_and_platform_cost < fees.net_pnl_after_fees
