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
