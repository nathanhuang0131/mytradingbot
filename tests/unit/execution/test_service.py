from mytradingbot.core.enums import RuntimeMode
from mytradingbot.risk.service import RiskEngine


def test_execution_engine_skips_broker_mutation_in_dry_run(
    approved_trade_intent,
) -> None:
    from mytradingbot.brokers.paper import PaperBroker
    from mytradingbot.execution.service import ExecutionEngine

    decision = RiskEngine().evaluate(intent=approved_trade_intent, mode=RuntimeMode.PAPER)
    broker = PaperBroker()
    engine = ExecutionEngine(broker=broker)

    result = engine.execute(decision, mode=RuntimeMode.DRY_RUN)

    assert result.execution_skipped
    assert result.order is None
    assert broker.list_orders() == []


def test_execution_engine_routes_paper_order_to_broker(
    approved_trade_intent,
) -> None:
    from mytradingbot.brokers.paper import PaperBroker
    from mytradingbot.execution.service import ExecutionEngine

    decision = RiskEngine().evaluate(intent=approved_trade_intent, mode=RuntimeMode.PAPER)
    broker = PaperBroker()
    engine = ExecutionEngine(broker=broker)

    result = engine.execute(decision, mode=RuntimeMode.PAPER)

    assert result.order is not None
    assert broker.list_orders()


def test_execution_engine_rounds_down_fractional_bracket_quantity_before_submission(
    approved_trade_intent,
) -> None:
    from mytradingbot.brokers.paper import PaperBroker
    from mytradingbot.execution.service import ExecutionEngine

    approved_trade_intent.quantity = 2.8
    approved_trade_intent.bracket_plan.planned_quantity = 2.8

    decision = RiskEngine().evaluate(intent=approved_trade_intent, mode=RuntimeMode.PAPER)
    broker = PaperBroker()
    engine = ExecutionEngine(broker=broker)

    result = engine.execute(decision, mode=RuntimeMode.PAPER)

    assert result.order is not None
    assert result.order.quantity == 2


def test_execution_engine_skips_trade_when_whole_share_quantity_rounds_to_zero(
    approved_trade_intent,
) -> None:
    from mytradingbot.brokers.paper import PaperBroker
    from mytradingbot.execution.service import ExecutionEngine

    approved_trade_intent.quantity = 0.8
    approved_trade_intent.bracket_plan.planned_quantity = 0.8

    decision = RiskEngine().evaluate(intent=approved_trade_intent, mode=RuntimeMode.PAPER)
    broker = PaperBroker()
    engine = ExecutionEngine(broker=broker)

    result = engine.execute(decision, mode=RuntimeMode.PAPER)

    assert result.execution_skipped
    assert result.reason == "invalid_broker_quantity"


def test_execution_engine_rejects_trade_when_rounding_breaks_bracket_expectancy(
    approved_trade_intent,
) -> None:
    from mytradingbot.brokers.paper import PaperBroker
    from mytradingbot.execution.service import ExecutionEngine

    approved_trade_intent.quantity = 1.6
    approved_trade_intent.bracket_plan.planned_quantity = 1.6
    approved_trade_intent.bracket_plan.estimated_fixed_fees = 1.5
    approved_trade_intent.bracket_plan.reward_risk_ratio = 1.6

    decision = RiskEngine().evaluate(intent=approved_trade_intent, mode=RuntimeMode.PAPER)
    broker = PaperBroker()
    engine = ExecutionEngine(broker=broker, minimum_bracket_reward_risk=1.5)

    result = engine.execute(decision, mode=RuntimeMode.PAPER)

    assert result.execution_skipped
    assert result.reason == "bracket_plan_invalid_after_rounding"
