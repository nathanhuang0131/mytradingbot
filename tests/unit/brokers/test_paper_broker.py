from mytradingbot.core.enums import RuntimeMode
from mytradingbot.core.models import ExecutionRequest


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
