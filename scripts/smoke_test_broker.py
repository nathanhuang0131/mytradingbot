from __future__ import annotations

from mytradingbot.brokers.paper import PaperBroker
from mytradingbot.core.enums import RuntimeMode
from mytradingbot.core.models import ExecutionRequest


def main() -> int:
    broker = PaperBroker()
    request = ExecutionRequest(
        symbol="AAPL",
        side="buy",
        quantity=1,
        strategy_name="scalping",
        mode=RuntimeMode.PAPER,
        limit_price=100.0,
    )
    result = broker.submit_order(request)
    print(result.model_dump_json(indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
