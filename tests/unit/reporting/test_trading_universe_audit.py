from __future__ import annotations

import json
from pathlib import Path

from mytradingbot.core.paths import RepoPaths
from mytradingbot.core.settings import AppSettings
from mytradingbot.reporting.trading_universe_audit import TradingUniverseAuditService


def _write_json(path: Path, payload: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2), encoding="utf-8")


def test_trading_universe_audit_service_generates_loop_markdown(tmp_path) -> None:
    settings = AppSettings(paths=RepoPaths.for_root(tmp_path))
    settings.ensure_runtime_directories()

    active_symbols_path = settings.paths.active_universes_dir / "overnight_test_active_symbols.json"
    _write_json(active_symbols_path, ["AAPL", "MSFT", "NVDA"])

    profile_path = settings.paths.session_profiles_dir / "overnight_test_latest.json"
    _write_json(
        profile_path,
        {
            "profile_name": "Overnight_Test",
            "profile_slug": "overnight_test",
            "active_symbols_path": str(active_symbols_path),
            "strategy": {
                "strategy_name": "scalping",
                "broker_mode": "alpaca_paper_api",
                "session_mode": "loop",
            },
        },
    )

    _write_json(
        settings.paths.reports_paper_trading_dir / "session-a_paper_session.json",
        {
            "session_id": "session-a",
            "run_id": "run-a",
            "strategy": "scalping",
            "mode": "paper",
            "broker_mode": "alpaca_paper_api",
            "started_at": "2026-03-26T19:00:00Z",
            "completed_at": "2026-03-26T19:05:00Z",
            "order_count": 1,
            "accepted_count": 1,
            "rejected_count": 1,
            "skipped_count": 0,
            "notes": ["Health summary: Session completed."],
        },
    )
    _write_json(
        settings.paths.reports_paper_trading_dir / "session-b_paper_session.json",
        {
            "session_id": "session-b",
            "run_id": "run-b",
            "strategy": "scalping",
            "mode": "paper",
            "broker_mode": "alpaca_paper_api",
            "started_at": "2026-03-26T20:00:00Z",
            "completed_at": "2026-03-26T20:05:00Z",
            "order_count": 0,
            "accepted_count": 0,
            "rejected_count": 1,
            "skipped_count": 0,
            "notes": ["Health summary: Session completed."],
        },
    )

    _write_json(
        settings.paths.reports_signals_dir / "session-a_decision_audit.json",
        [
            {
                "event_id": "event-aapl",
                "session_id": "session-a",
                "run_id": "run-a",
                "symbol": "AAPL",
                "signal_source": "qlib_plus_rules",
                "qlib_raw_score": 0.91,
                "predicted_return": 0.012,
                "expected_edge_after_cost": 0.0108,
                "quality_score": 0.88,
                "higher_timeframe_state": "bullish",
                "rule_checks": [
                    {"stage": "freshness", "name": "predictions_fresh", "passed": True},
                    {"stage": "strategy", "name": "predicted_return_threshold", "passed": True},
                    {"stage": "strategy", "name": "confidence_threshold", "passed": True},
                    {"stage": "risk", "name": "position_limit", "passed": True},
                    {"stage": "execution", "name": "execution_result", "passed": True},
                ],
                "final_decision_status": "accepted_bracket_buy",
                "final_rejection_reason_code": None,
                "final_rejection_reason_detail": None,
            },
            {
                "event_id": "event-msft",
                "session_id": "session-a",
                "run_id": "run-a",
                "symbol": "MSFT",
                "signal_source": "qlib_candidate_only",
                "qlib_raw_score": 0.41,
                "predicted_return": 0.004,
                "expected_edge_after_cost": 0.0001,
                "quality_score": 0.51,
                "higher_timeframe_state": "bullish",
                "rule_checks": [
                    {"stage": "freshness", "name": "predictions_fresh", "passed": True},
                    {"stage": "strategy", "name": "predicted_return_threshold", "passed": True},
                    {"stage": "strategy", "name": "spread_filter", "passed": False},
                ],
                "final_decision_status": "rejected",
                "final_rejection_reason_code": "spread_too_wide",
                "final_rejection_reason_detail": "spread_filter",
            },
        ],
    )
    _write_json(
        settings.paths.reports_signals_dir / "session-b_decision_audit.json",
        [
            {
                "event_id": "event-nvda",
                "session_id": "session-b",
                "run_id": "run-b",
                "symbol": "NVDA",
                "signal_source": "qlib_candidate_only",
                "qlib_raw_score": 0.18,
                "predicted_return": 0.0005,
                "expected_edge_after_cost": -0.0001,
                "quality_score": 0.2,
                "higher_timeframe_state": "neutral",
                "rule_checks": [
                    {"stage": "freshness", "name": "predictions_fresh", "passed": True},
                    {"stage": "strategy", "name": "predicted_return_threshold", "passed": False},
                ],
                "final_decision_status": "rejected",
                "final_rejection_reason_code": "target_return_below_threshold",
                "final_rejection_reason_detail": "predicted_return_threshold",
            }
        ],
    )

    report_path = TradingUniverseAuditService(settings=settings).generate(
        profile_slug="overnight_test",
        lookback_hours=12,
    )

    assert report_path.parent == settings.paths.reports_dir / "overnight"
    assert report_path.exists()

    text = report_path.read_text(encoding="utf-8")
    assert "# Trading Universe Audit" in text
    assert "Overnight_Test" in text
    assert "Configured overnight universe" in text
    assert "session-a" in text
    assert "session-b" in text
    assert "Qlib candidate universe" in text
    assert "Trade-approved symbols" in text
    assert "AAPL" in text
    assert "accepted_bracket_buy" in text
    assert "MSFT" in text
    assert "spread_too_wide" in text
    assert "spread_filter" in text
    assert "NVDA" in text
    assert "target_return_below_threshold" in text
    assert "predicted_return_threshold" in text
    assert "Edge After Cost" in text
    assert "HTF Trend" in text
