from __future__ import annotations

import csv
from datetime import datetime, timedelta, timezone

from mytradingbot.core.enums import RuntimeMode
from mytradingbot.core.paths import RepoPaths
from mytradingbot.core.settings import AppSettings
from mytradingbot.reporting.analytics import RealizedAnalyticsExporter
from mytradingbot.runtime.models import DecisionAuditRecord, FillLifecycleRecord, OrderLifecycleRecord
from mytradingbot.runtime.service import RuntimeStateService


def test_realized_analytics_materializes_closed_trades_and_attribution(tmp_path) -> None:
    settings = AppSettings(paths=RepoPaths.for_root(tmp_path))
    runtime_service = RuntimeStateService(settings=settings)
    entry_ts = datetime.now(timezone.utc) - timedelta(minutes=10)
    exit_ts = entry_ts + timedelta(minutes=5)

    runtime_service.store.record_decision(
        DecisionAuditRecord(
            session_id="entry-session",
            run_id="entry-run",
            correlation_id="attempt-1",
            timestamp=entry_ts,
            strategy="scalping",
            strategy_version="v2",
            mode=RuntimeMode.PAPER,
            symbol="AAPL",
            side_considered="buy",
            bracket_considered=True,
            signal_source="qlib_plus_rules",
            prediction_artifact_path="predictions.json",
            model_artifact_path="model.pkl",
            dataset_artifact_path="dataset.parquet",
            final_decision_status="accepted_bracket_buy",
        )
    )
    runtime_service.store.record_order(
        OrderLifecycleRecord(
            order_id="entry-order",
            session_id="entry-session",
            run_id="entry-run",
            strategy="scalping",
            mode=RuntimeMode.PAPER,
            broker_mode="alpaca_paper_api",
            ownership_class="bot_owned",
            symbol="AAPL",
            side="buy",
            quantity=2,
            client_order_id="SCALPING-AAPL-BUY-1",
            status="filled",
            submitted_at=entry_ts,
            avg_fill_price=100.0,
            metadata={"signal_source": "qlib_plus_rules"},
        )
    )
    runtime_service.store.record_fill(
        FillLifecycleRecord(
            fill_id="entry-fill",
            order_id="entry-order",
            session_id="entry-session",
            run_id="entry-run",
            strategy="scalping",
            mode=RuntimeMode.PAPER,
            broker_mode="alpaca_paper_api",
            ownership_class="bot_owned",
            symbol="AAPL",
            quantity=2,
            price=100.0,
            filled_at=entry_ts,
            metadata={"signal_source": "qlib_plus_rules"},
        )
    )
    runtime_service.store.record_order(
        OrderLifecycleRecord(
            order_id="exit-order",
            session_id="exit-session",
            run_id="exit-run",
            strategy="scalping",
            mode=RuntimeMode.PAPER,
            broker_mode="alpaca_paper_api",
            ownership_class="bot_owned",
            symbol="AAPL",
            side="sell",
            quantity=2,
            status="filled",
            submitted_at=exit_ts,
            avg_fill_price=105.0,
            metadata={"exit_reason": "take_profit"},
        )
    )
    runtime_service.store.record_fill(
        FillLifecycleRecord(
            fill_id="exit-fill",
            order_id="exit-order",
            session_id="exit-session",
            run_id="exit-run",
            strategy="scalping",
            mode=RuntimeMode.PAPER,
            broker_mode="alpaca_paper_api",
            ownership_class="bot_owned",
            symbol="AAPL",
            quantity=2,
            price=105.0,
            filled_at=exit_ts,
            metadata={"exit_reason": "take_profit"},
        )
    )
    runtime_service.store.replace_observed_positions(
        [
            {
                "symbol": "MSFT",
                "broker_mode": "alpaca_paper_api",
                "ownership_class": "foreign",
                "quantity": 5.0,
                "average_price": 250.0,
                "market_price": 251.0,
                "observed_at": exit_ts,
                "source": "alpaca_paper_account",
            }
        ]
    )

    artifacts = RealizedAnalyticsExporter(settings=settings, store=runtime_service.store).write()

    closed_trades_path = settings.paths.reports_analytics_dir / "closed_trades.csv"
    attribution_path = settings.paths.reports_analytics_dir / "pnl_attribution.csv"
    summary_path = settings.paths.reports_analytics_dir / "pnl_summary.md"

    assert str(closed_trades_path) in artifacts
    assert str(attribution_path) in artifacts
    assert str(summary_path) in artifacts

    with closed_trades_path.open("r", encoding="utf-8", newline="") as handle:
        closed_rows = list(csv.DictReader(handle))
    assert len(closed_rows) == 1
    assert closed_rows[0]["symbol"] == "AAPL"
    assert closed_rows[0]["strategy"] == "scalping"
    assert closed_rows[0]["signal_source"] == "qlib_plus_rules"
    assert closed_rows[0]["broker_mode"] == "alpaca_paper_api"
    assert closed_rows[0]["ownership_class"] == "bot_owned"
    assert float(closed_rows[0]["gross_pnl"]) == 10.0
    assert closed_rows[0]["fee_schedule_version"]
    assert float(closed_rows[0]["qty"]) == 2.0
    assert float(closed_rows[0]["realized_pnl"]) == 10.0
    assert float(closed_rows[0]["realized_return_pct"]) == 5.0
    assert closed_rows[0]["win_loss_flag"] == "win"
    assert closed_rows[0]["session_id"] == "entry-session"
    assert closed_rows[0]["run_id"] == "entry-run"

    with attribution_path.open("r", encoding="utf-8", newline="") as handle:
        attribution_rows = list(csv.DictReader(handle))
    symbol_row = next(row for row in attribution_rows if row["dimension"] == "symbol" and row["value"] == "AAPL")
    strategy_row = next(row for row in attribution_rows if row["dimension"] == "strategy" and row["value"] == "scalping")
    source_row = next(row for row in attribution_rows if row["dimension"] == "signal_source" and row["value"] == "qlib_plus_rules")
    broker_row = next(row for row in attribution_rows if row["dimension"] == "broker_mode" and row["value"] == "alpaca_paper_api")

    assert symbol_row["broker_mode"] == "alpaca_paper_api"
    assert float(symbol_row["total_realized_pnl"]) == 10.0
    assert float(symbol_row["excluded_foreign_position_count"]) == 1.0
    assert float(symbol_row["win_rate"]) == 1.0
    assert float(strategy_row["total_realized_pnl"]) == 10.0
    assert float(source_row["total_realized_pnl"]) == 10.0
    assert float(broker_row["total_realized_pnl"]) == 10.0

    summary_text = summary_path.read_text(encoding="utf-8")
    assert "AAPL" in summary_text
    assert "qlib_plus_rules" in summary_text
    assert "foreign exposure" in summary_text.lower()
    assert "alpaca paper api broker" in summary_text.lower()


def test_realized_analytics_excludes_foreign_closed_trades_from_attribution(tmp_path) -> None:
    settings = AppSettings(paths=RepoPaths.for_root(tmp_path))
    runtime_service = RuntimeStateService(settings=settings)
    entry_ts = datetime.now(timezone.utc) - timedelta(minutes=10)
    exit_ts = entry_ts + timedelta(minutes=5)

    runtime_service.store.record_order(
        OrderLifecycleRecord(
            order_id="foreign-entry-order",
            session_id="foreign-entry-session",
            run_id="foreign-entry-run",
            strategy="manual",
            mode=RuntimeMode.PAPER,
            broker_mode="alpaca_paper_api",
            ownership_class="foreign",
            symbol="MSFT",
            side="buy",
            quantity=1,
            status="filled",
            submitted_at=entry_ts,
            avg_fill_price=200.0,
            metadata={"signal_source": "no_valid_signal"},
        )
    )
    runtime_service.store.record_fill(
        FillLifecycleRecord(
            fill_id="foreign-entry-fill",
            order_id="foreign-entry-order",
            session_id="foreign-entry-session",
            run_id="foreign-entry-run",
            strategy="manual",
            mode=RuntimeMode.PAPER,
            broker_mode="alpaca_paper_api",
            ownership_class="foreign",
            symbol="MSFT",
            quantity=1,
            price=200.0,
            filled_at=entry_ts,
            metadata={"signal_source": "no_valid_signal"},
        )
    )
    runtime_service.store.record_order(
        OrderLifecycleRecord(
            order_id="foreign-exit-order",
            session_id="foreign-exit-session",
            run_id="foreign-exit-run",
            strategy="manual",
            mode=RuntimeMode.PAPER,
            broker_mode="alpaca_paper_api",
            ownership_class="foreign",
            symbol="MSFT",
            side="sell",
            quantity=1,
            status="filled",
            submitted_at=exit_ts,
            avg_fill_price=210.0,
            metadata={"exit_reason": "manual_close"},
        )
    )
    runtime_service.store.record_fill(
        FillLifecycleRecord(
            fill_id="foreign-exit-fill",
            order_id="foreign-exit-order",
            session_id="foreign-exit-session",
            run_id="foreign-exit-run",
            strategy="manual",
            mode=RuntimeMode.PAPER,
            broker_mode="alpaca_paper_api",
            ownership_class="foreign",
            symbol="MSFT",
            quantity=1,
            price=210.0,
            filled_at=exit_ts,
            metadata={"exit_reason": "manual_close"},
        )
    )

    attribution_rows = RealizedAnalyticsExporter(
        settings=settings,
        store=runtime_service.store,
    ).build_attribution_rows(
        RealizedAnalyticsExporter(settings=settings, store=runtime_service.store).build_closed_trades()
    )

    assert attribution_rows == []


def test_realized_analytics_materializes_short_closed_trades(tmp_path) -> None:
    settings = AppSettings(paths=RepoPaths.for_root(tmp_path))
    runtime_service = RuntimeStateService(settings=settings)
    entry_ts = datetime.now(timezone.utc) - timedelta(minutes=10)
    exit_ts = entry_ts + timedelta(minutes=5)

    runtime_service.store.record_order(
        OrderLifecycleRecord(
            order_id="short-entry-order",
            session_id="short-entry-session",
            run_id="short-entry-run",
            strategy="scalping",
            mode=RuntimeMode.PAPER,
            broker_mode="alpaca_paper_api",
            ownership_class="bot_owned",
            symbol="TSLA",
            side="sell",
            quantity=2,
            client_order_id="SCALPING-TSLA-SELL-1",
            status="filled",
            submitted_at=entry_ts,
            avg_fill_price=100.0,
            metadata={"signal_source": "qlib_plus_rules"},
        )
    )
    runtime_service.store.record_fill(
        FillLifecycleRecord(
            fill_id="short-entry-fill",
            order_id="short-entry-order",
            session_id="short-entry-session",
            run_id="short-entry-run",
            strategy="scalping",
            mode=RuntimeMode.PAPER,
            broker_mode="alpaca_paper_api",
            ownership_class="bot_owned",
            symbol="TSLA",
            quantity=2,
            price=100.0,
            filled_at=entry_ts,
            metadata={"signal_source": "qlib_plus_rules"},
        )
    )
    runtime_service.store.record_order(
        OrderLifecycleRecord(
            order_id="short-exit-order",
            session_id="short-exit-session",
            run_id="short-exit-run",
            strategy="scalping",
            mode=RuntimeMode.PAPER,
            broker_mode="alpaca_paper_api",
            ownership_class="bot_owned",
            symbol="TSLA",
            side="buy",
            quantity=2,
            status="filled",
            submitted_at=exit_ts,
            avg_fill_price=95.0,
            metadata={"exit_reason": "take_profit"},
        )
    )
    runtime_service.store.record_fill(
        FillLifecycleRecord(
            fill_id="short-exit-fill",
            order_id="short-exit-order",
            session_id="short-exit-session",
            run_id="short-exit-run",
            strategy="scalping",
            mode=RuntimeMode.PAPER,
            broker_mode="alpaca_paper_api",
            ownership_class="bot_owned",
            symbol="TSLA",
            quantity=2,
            price=95.0,
            filled_at=exit_ts,
            metadata={"exit_reason": "take_profit"},
        )
    )

    closed_trades = RealizedAnalyticsExporter(
        settings=settings,
        store=runtime_service.store,
    ).build_closed_trades()

    assert len(closed_trades) == 1
    assert closed_trades[0].symbol == "TSLA"
    assert closed_trades[0].gross_pnl == 10.0
    assert closed_trades[0].realized_pnl == 10.0
    assert closed_trades[0].realized_return_pct == 5.0
    assert closed_trades[0].win_loss_flag == "win"
