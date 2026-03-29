from __future__ import annotations

from datetime import datetime, timezone

from mytradingbot.core.enums import RuntimeMode
from mytradingbot.core.paths import RepoPaths
from mytradingbot.core.settings import AppSettings
from mytradingbot.runtime.models import OrderLifecycleRecord
from mytradingbot.runtime.store import RuntimeStateStore


def test_runtime_store_list_orders_normalizes_non_terminal_broker_statuses(tmp_path) -> None:
    settings = AppSettings(paths=RepoPaths.for_root(tmp_path))
    store = RuntimeStateStore(settings=settings)
    store.record_order(
        OrderLifecycleRecord(
            order_id="alpaca-held-order",
            session_id="session-1",
            run_id="run-1",
            strategy="scalping",
            mode=RuntimeMode.PAPER,
            broker_mode="alpaca_paper_api",
            symbol="AMZN",
            side="buy",
            quantity=8.0,
            client_order_id="SCALPING-AMZN-BUY-202603192210",
            status="held",
            submitted_at=datetime.now(timezone.utc),
            metadata={},
        )
    )

    orders = store.list_orders()

    assert len(orders) == 1
    assert orders[0].status == "accepted"
