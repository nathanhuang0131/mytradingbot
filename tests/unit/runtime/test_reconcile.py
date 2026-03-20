from __future__ import annotations

from datetime import datetime, timezone
from types import SimpleNamespace

from mytradingbot.core.paths import RepoPaths
from mytradingbot.core.settings import AppSettings
from mytradingbot.runtime.store import RuntimeStateStore


def test_ownership_classifier_marks_repo_client_order_ids_as_bot_owned() -> None:
    from mytradingbot.runtime.reconcile import OwnershipClassifier

    classifier = OwnershipClassifier(known_client_order_ids=set(), known_order_ids=set())
    order = SimpleNamespace(
        id="alpaca-order-1",
        client_order_id="SCALPING-AAPL-BUY-202603201030",
        symbol="AAPL",
        legs=[],
    )

    assert classifier.classify_order(order) == "bot_owned"


def test_ownership_classifier_treats_unmatched_orders_as_foreign_or_unknown() -> None:
    from mytradingbot.runtime.reconcile import OwnershipClassifier

    classifier = OwnershipClassifier(known_client_order_ids=set(), known_order_ids=set())
    foreign_order = SimpleNamespace(
        id="manual-order-1",
        client_order_id="MANUAL-AAPL-1",
        symbol="AAPL",
        legs=[],
    )
    unknown_order = SimpleNamespace(
        id="unknown-order-1",
        client_order_id=None,
        symbol="AAPL",
        legs=[],
    )

    assert classifier.classify_order(foreign_order) == "foreign"
    assert classifier.classify_order(unknown_order) == "unknown"
    assert classifier.management_class("unknown") == "foreign"


def test_runtime_store_records_foreign_position_observations_for_risk_context(tmp_path) -> None:
    from mytradingbot.runtime.models import ObservedPositionRecord

    settings = AppSettings(paths=RepoPaths.for_root(tmp_path))
    store = RuntimeStateStore(settings=settings)
    store.replace_observed_positions(
        [
            ObservedPositionRecord(
                symbol="AAPL",
                broker_mode="alpaca_paper_api",
                ownership_class="foreign",
                quantity=3.0,
                average_price=100.0,
                market_price=101.0,
                observed_at=datetime.now(timezone.utc),
                source="alpaca_paper_account",
            )
        ]
    )

    records = store.list_observed_positions()

    assert len(records) == 1
    assert records[0].ownership_class == "foreign"
    assert store.foreign_position_symbols() == {"AAPL"}
