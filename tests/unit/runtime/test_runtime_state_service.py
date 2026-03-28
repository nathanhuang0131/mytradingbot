from __future__ import annotations

from datetime import datetime, timedelta, timezone

from mytradingbot.brokers.paper import PaperBroker
from mytradingbot.core.enums import RuntimeMode
from mytradingbot.core.models import (
    ArtifactStatus,
    BracketPlan,
    BrokerBracketState,
    BrokerOrder,
    ExecutionResult,
    PositionSnapshot,
    TradeAttemptTrace,
)
from mytradingbot.core.paths import RepoPaths
from mytradingbot.core.settings import AppSettings
from mytradingbot.core.models import StrategyDecision
from mytradingbot.runtime.models import FillLifecycleRecord
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


def test_runtime_service_minutes_to_close_ignores_prior_session_close_timestamp() -> None:
    prior_session_close = datetime(2026, 3, 20, 20, 0, tzinfo=timezone.utc)
    pre_open_reference = datetime(2026, 3, 23, 12, 0, tzinfo=timezone.utc)

    minutes = RuntimeStateService.minutes_to_close(
        prior_session_close,
        reference_time=pre_open_reference,
    )

    assert minutes == 999


def test_runtime_service_records_configured_cooldown_window_for_closed_brackets(tmp_path) -> None:
    settings = AppSettings(paths=RepoPaths.for_root(tmp_path))
    settings.scalping.cooldown_minutes = 10
    runtime_service = RuntimeStateService(settings=settings)
    context = runtime_service.create_session_context(strategy="scalping", mode=RuntimeMode.PAPER)
    closed_at = datetime(2026, 3, 27, 10, 0, tzinfo=timezone.utc)

    runtime_service.record_execution_result(
        context=context,
        strategy_name="scalping",
        result=ExecutionResult(
            bracket_state=BrokerBracketState(
                symbol="AAPL",
                entry_order_id="entry-1",
                status="closed",
                closed_at=closed_at,
                exit_reason="timeout_exit",
                bracket_plan=BracketPlan(
                    planned_entry_price=100.0,
                    planned_stop_loss_price=99.0,
                    planned_take_profit_price=101.5,
                    planned_quantity=1.0,
                    risk_per_share=1.0,
                    gross_reward_per_share=1.5,
                    estimated_fees=0.0,
                    estimated_slippage=0.0,
                    estimated_fee_per_share=0.0,
                    estimated_slippage_per_share=0.0,
                    estimated_fixed_fees=0.0,
                    net_reward_per_share=1.5,
                    reward_risk_ratio=1.5,
                    expected_net_profit=1.5,
                ),
            )
        ),
    )

    assert runtime_service.store.active_cooldowns(
        strategy="scalping",
        now=closed_at + timedelta(minutes=9, seconds=59),
    ) == {"AAPL"}
    assert runtime_service.store.active_cooldowns(
        strategy="scalping",
        now=closed_at + timedelta(minutes=10),
    ) == set()


def test_runtime_service_cooldowns_survive_restart(tmp_path) -> None:
    settings = AppSettings(paths=RepoPaths.for_root(tmp_path))
    settings.scalping.cooldown_minutes = 10
    first = RuntimeStateService(settings=settings)
    context = first.create_session_context(strategy="scalping", mode=RuntimeMode.PAPER)
    closed_at = datetime(2026, 3, 27, 11, 0, tzinfo=timezone.utc)

    first.record_execution_result(
        context=context,
        strategy_name="scalping",
        result=ExecutionResult(
            bracket_state=BrokerBracketState(
                symbol="MSFT",
                entry_order_id="entry-2",
                status="closed",
                closed_at=closed_at,
                exit_reason="take_profit",
                bracket_plan=BracketPlan(
                    planned_entry_price=200.0,
                    planned_stop_loss_price=198.0,
                    planned_take_profit_price=203.0,
                    planned_quantity=1.0,
                    risk_per_share=2.0,
                    gross_reward_per_share=3.0,
                    estimated_fees=0.0,
                    estimated_slippage=0.0,
                    estimated_fee_per_share=0.0,
                    estimated_slippage_per_share=0.0,
                    estimated_fixed_fees=0.0,
                    net_reward_per_share=3.0,
                    reward_risk_ratio=1.5,
                    expected_net_profit=3.0,
                ),
            )
        ),
    )

    restarted = RuntimeStateService(settings=settings)

    assert restarted.store.active_cooldowns(
        strategy="scalping",
        now=closed_at + timedelta(minutes=5),
    ) == {"MSFT"}


def test_runtime_service_maps_strategy_rejections_to_precise_reason_codes(tmp_path) -> None:
    settings = AppSettings(paths=RepoPaths.for_root(tmp_path))
    runtime_service = RuntimeStateService(settings=settings)

    assert runtime_service.map_rejection_reason("vwap_relationship") == "vwap_relationship_blocked"
    assert runtime_service.map_rejection_reason("flatten_near_close_logic") == "near_close_window_blocked"
    assert runtime_service.map_rejection_reason("edge_after_cost_buffer") == "edge_after_cost_below_buffer"
    assert (
        runtime_service.map_rejection_reason("higher_timeframe_trend_alignment")
        == "higher_timeframe_trend_blocked"
    )
    assert runtime_service.map_rejection_reason("top_n_selection_cutoff") == "top_n_selection_cutoff"
    assert runtime_service.map_rejection_reason("invalid_signal_payload:vwap_unavailable") == "invalid_signal_payload"


def test_runtime_service_writes_detailed_audit_and_tuning_artifacts(
    signal_bundle_factory,
    tmp_path,
) -> None:
    settings = AppSettings(paths=RepoPaths.for_root(tmp_path))
    runtime_service = RuntimeStateService(settings=settings)
    context = runtime_service.create_session_context(
        strategy="scalping",
        mode=RuntimeMode.PAPER,
    )
    signal = signal_bundle_factory(symbol="AAPL", predicted_return=0.0004, spread_bps=6.2)
    trace = TradeAttemptTrace.for_symbol("AAPL", "scalping")
    trace.signal = signal
    trace.strategy_outcome = StrategyDecision.reject(
        strategy_name="scalping",
        symbol="AAPL",
        reason="predicted_return_threshold",
        failed_filters=["predicted_return_threshold", "spread_filter"],
        passed_filters=["confidence_threshold", "vwap_relationship"],
    )

    audit = runtime_service.build_decision_audit(
        context=context,
        signal=signal,
        trace=trace,
        prediction_status=ArtifactStatus.ready("predictions", freshness_minutes=5),
        market_status=ArtifactStatus.ready("market_snapshot", freshness_minutes=1),
    )
    report = runtime_service.write_session_artifacts(
        context=context,
        audits=[audit],
        orders=[],
        fills=[],
        positions=[],
        incidents=[],
        notes=["overnight tuning artifact check"],
    )

    audit_csv = (
        settings.paths.reports_signals_dir / f"{context.session_id}_decision_audit.csv"
    ).read_text(encoding="utf-8")
    tuning_csv_path = settings.paths.reports_analytics_dir / f"{context.session_id}_analytics.csv"
    tuning_md_path = settings.paths.reports_analytics_dir / f"{context.session_id}_analytics.md"

    assert "confidence" in audit_csv
    assert "spread_bps" in audit_csv
    assert "liquidity_score" in audit_csv
    assert "expected_edge_after_cost" in audit_csv
    assert "quality_score" in audit_csv
    assert "higher_timeframe_state" in audit_csv
    assert "rejection_reasons" in audit_csv
    assert tuning_csv_path.exists()
    assert "top symbols blocked by threshold" in tuning_md_path.read_text(encoding="utf-8").lower()
    assert "symbols blocked by trend alignment" in tuning_md_path.read_text(encoding="utf-8").lower()
    assert "positive return but negative edge after cost" in tuning_md_path.read_text(encoding="utf-8").lower()
    assert str(tuning_csv_path) in report.report_paths


def test_runtime_service_refreshes_session_markdown_counts_after_reconciled_fill(tmp_path) -> None:
    settings = AppSettings(paths=RepoPaths.for_root(tmp_path))
    runtime_service = RuntimeStateService(settings=settings)
    context = runtime_service.create_session_context(strategy="scalping", mode=RuntimeMode.PAPER)
    submitted_at = datetime(2026, 3, 28, 3, 50, tzinfo=timezone.utc)
    order = BrokerOrder(
        order_id="entry-order-1",
        symbol="RDY",
        side="buy",
        quantity=1.0,
        mode=RuntimeMode.PAPER,
        client_order_id="SCALPING-RDY-BUY-202603280350",
        status="accepted",
        submitted_at=submitted_at,
        avg_fill_price=None,
        metadata={"broker_order_class": "bracket"},
    )

    runtime_service.record_execution_result(
        context=context,
        strategy_name="scalping",
        result=ExecutionResult(order=order),
    )
    runtime_service.write_session_artifacts(
        context=context,
        audits=[],
        orders=[order],
        fills=[],
        positions=[],
        incidents=[],
        notes=["delayed fill materialization test"],
    )

    session_markdown_path = (
        settings.paths.reports_paper_trading_dir / f"{context.session_id}_paper_session.md"
    )
    session_json_path = (
        settings.paths.reports_paper_trading_dir / f"{context.session_id}_paper_session.json"
    )

    assert "- fills: `0`" in session_markdown_path.read_text(encoding="utf-8")

    runtime_service.store.record_fill(
        FillLifecycleRecord(
            fill_id="entry-order-1:2026-03-28T03:50:02+00:00",
            order_id="entry-order-1",
            session_id=context.session_id,
            run_id=context.run_id,
            strategy="scalping",
            mode=RuntimeMode.PAPER,
            broker_mode=context.broker_mode,
            ownership_class="bot_owned",
            symbol="RDY",
            quantity=1.0,
            price=13.59,
            filled_at=submitted_at + timedelta(seconds=2),
            metadata={"broker_order_class": "bracket"},
        )
    )

    refreshed_session_ids = runtime_service.refresh_completed_session_artifacts()

    updated_markdown = session_markdown_path.read_text(encoding="utf-8")
    updated_report = session_json_path.read_text(encoding="utf-8")

    assert context.session_id in refreshed_session_ids
    assert "- fills: `1`" in updated_markdown
    assert '"fill_count": 1' in updated_report
