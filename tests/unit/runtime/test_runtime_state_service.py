from __future__ import annotations

from datetime import datetime, timedelta, timezone

from mytradingbot.brokers.paper import PaperBroker
from mytradingbot.core.enums import RuntimeMode
from mytradingbot.core.models import ArtifactStatus, PositionSnapshot, TradeAttemptTrace
from mytradingbot.core.paths import RepoPaths
from mytradingbot.core.settings import AppSettings
from mytradingbot.core.models import StrategyDecision
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


def test_runtime_service_enriches_foreign_position_metadata(signal_bundle_factory, tmp_path) -> None:
    settings = AppSettings(paths=RepoPaths.for_root(tmp_path))
    runtime_service = RuntimeStateService(settings=settings)
    runtime_service.store.replace_observed_positions(
        [
            {
                "symbol": "AAPL",
                "broker_mode": "alpaca_paper_api",
                "ownership_class": "foreign",
                "quantity": 5.0,
                "average_price": 100.0,
                "market_price": 101.0,
                "observed_at": datetime.now(timezone.utc),
                "source": "alpaca_paper_account",
            }
        ]
    )

    signals = runtime_service.enrich_signal_metadata(
        strategy_name="scalping",
        signals=[signal_bundle_factory(symbol="AAPL")],
    )

    assert signals[0].metadata["foreign_position_exists"] is True


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


def test_runtime_service_persists_local_broker_mode_into_ledgers_and_reports(
    signal_bundle_factory,
    tmp_path,
) -> None:
    settings = AppSettings(paths=RepoPaths.for_root(tmp_path))
    runtime_service = RuntimeStateService(settings=settings)
    context = runtime_service.create_session_context(
        strategy="scalping",
        mode=RuntimeMode.PAPER,
    )
    signal = signal_bundle_factory(symbol="AAPL")
    trace = TradeAttemptTrace.for_symbol("AAPL", "scalping")
    trace.signal = signal
    trace.strategy_outcome = StrategyDecision.reject(
        strategy_name="scalping",
        symbol="AAPL",
        reason="predicted_return_threshold",
        failed_filters=["predicted_return_threshold"],
    )

    audit = runtime_service.build_decision_audit(
        context=context,
        signal=signal,
        trace=trace,
        prediction_status=ArtifactStatus.ready("predictions", freshness_minutes=5),
        market_status=ArtifactStatus.ready("market_snapshot", freshness_minutes=1),
    )
    incident = runtime_service.build_incident(
        context=context,
        code="local_paper_test",
        summary="Testing local paper broker mode propagation.",
    )
    report = runtime_service.write_session_artifacts(
        context=context,
        audits=[audit],
        orders=[],
        fills=[],
        positions=[],
        incidents=[incident],
        notes=["using local paper broker"],
    )

    signal_ledger = (settings.paths.ledger_dir / "signal_outcomes.csv").read_text(encoding="utf-8")
    incident_ledger = (settings.paths.ledger_dir / "incidents.csv").read_text(encoding="utf-8")
    session_markdown = (
        settings.paths.reports_paper_trading_dir / f"{context.session_id}_paper_session.md"
    ).read_text(encoding="utf-8")

    assert context.broker_mode == "local_paper"
    assert audit.broker_mode == "local_paper"
    assert incident.broker_mode == "local_paper"
    assert report.broker_mode == "local_paper"
    assert "local_paper" in signal_ledger
    assert "local_paper" in incident_ledger
    assert "local simulated paper broker" in session_markdown.lower()


def test_runtime_service_resolves_configured_alpaca_broker_mode(tmp_path) -> None:
    settings = AppSettings(paths=RepoPaths.for_root(tmp_path))
    settings.broker.broker_mode = "alpaca_paper_api"

    runtime_service = RuntimeStateService(settings=settings)

    assert runtime_service.resolve_broker_mode(mode=RuntimeMode.PAPER) == "alpaca_paper_api"
