from mytradingbot.core.enums import RuntimeMode
from mytradingbot.core.models import BracketPlan, ExecutionRequest, MarketSnapshot


def test_paper_broker_records_order_and_position() -> None:
    from mytradingbot.brokers.paper import PaperBroker

    broker = PaperBroker()
    request = ExecutionRequest(
        symbol="AAPL",
        side="buy",
        quantity=2,
        strategy_name="scalping",
        mode=RuntimeMode.PAPER,
        limit_price=100.0,
    )

    result = broker.submit_order(request)

    assert result.order is not None
    assert broker.list_positions()
    assert broker.list_orders()


def test_paper_broker_triggers_synthetic_take_profit_exit_once() -> None:
    from mytradingbot.brokers.paper import PaperBroker

    broker = PaperBroker()
    bracket = BracketPlan(
        planned_entry_price=100.0,
        planned_stop_loss_price=99.0,
        planned_take_profit_price=102.0,
        planned_quantity=2.0,
        risk_per_share=1.0,
        gross_reward_per_share=2.0,
        estimated_fees=0.0,
        estimated_slippage=0.0,
        estimated_fee_per_share=0.0,
        estimated_slippage_per_share=0.0,
        estimated_fixed_fees=0.0,
        net_reward_per_share=2.0,
        reward_risk_ratio=2.0,
        expected_net_profit=4.0,
        time_in_force="day",
        exit_reason_metadata={"take_profit": "target_exit"},
    )
    request = ExecutionRequest(
        symbol="AAPL",
        side="buy",
        quantity=2,
        strategy_name="scalping",
        mode=RuntimeMode.PAPER,
        limit_price=100.0,
        bracket_plan=bracket,
    )

    broker.submit_order(request)
    exits = broker.process_market_snapshot(
        MarketSnapshot(
            symbol="AAPL",
            last_price=102.1,
            vwap=101.5,
            spread_bps=1.0,
            volume=1_000_000,
            liquidity_score=0.8,
            liquidity_stress=0.2,
            order_book_imbalance=0.3,
            liquidity_sweep_detected=False,
            volatility_regime="normal",
        )
    )
    duplicate = broker.process_market_snapshot(
        MarketSnapshot(
            symbol="AAPL",
            last_price=102.2,
            vwap=101.6,
            spread_bps=1.0,
            volume=1_100_000,
            liquidity_score=0.8,
            liquidity_stress=0.2,
            order_book_imbalance=0.3,
            liquidity_sweep_detected=False,
            volatility_regime="normal",
        )
    )

    assert len(exits) == 1
    assert exits[0].reason == "take_profit"
    assert duplicate == []


def test_paper_broker_flattens_open_brackets_near_close() -> None:
    from mytradingbot.brokers.paper import PaperBroker

    broker = PaperBroker()
    request = ExecutionRequest(
        symbol="AAPL",
        side="buy",
        quantity=2,
        strategy_name="scalping",
        mode=RuntimeMode.PAPER,
        limit_price=100.0,
        bracket_plan=BracketPlan(
            planned_entry_price=100.0,
            planned_stop_loss_price=99.0,
            planned_take_profit_price=102.0,
            planned_quantity=2.0,
            risk_per_share=1.0,
            gross_reward_per_share=2.0,
            estimated_fees=0.0,
            estimated_slippage=0.0,
            estimated_fee_per_share=0.0,
            estimated_slippage_per_share=0.0,
            estimated_fixed_fees=0.0,
            net_reward_per_share=2.0,
            reward_risk_ratio=2.0,
            expected_net_profit=4.0,
            time_in_force="day",
            exit_reason_metadata={"near_close_flatten": "session_exit"},
        ),
    )

    broker.submit_order(request)
    exits = broker.flatten_open_brackets(reason="near_close_flatten")

    assert len(exits) == 1
    assert exits[0].reason == "near_close_flatten"
