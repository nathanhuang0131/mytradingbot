from __future__ import annotations

from datetime import datetime, timedelta, timezone

from mytradingbot.brokers.paper import PaperBroker
from mytradingbot.core.enums import RuntimeMode
from mytradingbot.core.models import PositionSnapshot
from mytradingbot.core.paths import RepoPaths
from mytradingbot.core.settings import AppSettings
from mytradingbot.runtime.service import RuntimeStateService


def test_runtime_service_enriches_cooldown_and_position_metadata(signal_bundle_factory, tmp_path) -> None:
    settings = AppSettings(paths=RepoPaths.for_root(tmp_path))
    runtime_service = RuntimeStateService(settings=settings)
    runtime_service.store.set_cooldown(
        symbol="AAPL",
        strategy="scalping",
        expires_at=datetime.now(timezone.utc) + timedelta(minutes=15),
    )
    runtime_service.store.record_position(
        PositionSnapshot(
            symbol="AAPL",
            quantity=5,
            average_price=100.0,
            market_price=101.0,
        )
    )

    signals = runtime_service.enrich_signal_metadata(
        strategy_name="scalping",
        signals=[signal_bundle_factory(symbol="AAPL")],
    )

    assert signals[0].metadata["cooldown_active"] is True
    assert signals[0].metadata["position_exists"] is True
    assert isinstance(signals[0].metadata["minutes_to_close"], int)


def test_paper_broker_restores_brackets_from_runtime_store(approved_trade_intent, tmp_path) -> None:
    settings = AppSettings(paths=RepoPaths.for_root(tmp_path))
    runtime_service = RuntimeStateService(settings=settings)
    broker = PaperBroker(runtime_store=runtime_service.store)
    from mytradingbot.core.models import ExecutionRequest

    broker.submit_order(
        ExecutionRequest.from_intent(approved_trade_intent, RuntimeMode.PAPER)
    )

    restarted = PaperBroker(runtime_store=runtime_service.store)

    assert restarted.list_brackets()
    assert restarted.list_positions()
