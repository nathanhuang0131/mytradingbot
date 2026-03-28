from __future__ import annotations

import csv
from pathlib import Path

from mytradingbot.core.enums import RuntimeMode
from mytradingbot.core.models import ArtifactStatus, HealthStatus, SessionResult, SessionSummary
from mytradingbot.core.paths import RepoPaths
from mytradingbot.core.settings import AppSettings
from mytradingbot.orchestration.service import TradingPlatformService
from mytradingbot.runtime.models import PaperTradingSessionReport
from mytradingbot.session_setup.service import SetupWizardService
from mytradingbot.ui_services.status_reference import StatusReferenceService


def _build_settings(repo_root: Path) -> AppSettings:
    settings = AppSettings(paths=RepoPaths.for_root(repo_root))
    settings.ensure_runtime_directories()
    return settings


def _write_saved_session_artifacts(settings: AppSettings) -> None:
    report = PaperTradingSessionReport(
        session_id="saved-session",
        run_id="saved-run",
        strategy="scalping",
        mode=RuntimeMode.PAPER,
        broker_mode="alpaca_paper_api",
        started_at="2026-03-27T09:30:00Z",
        completed_at="2026-03-27T09:35:00Z",
        order_count=1,
        fill_count=1,
        accepted_count=1,
        rejected_count=4,
        skipped_count=0,
        no_trade_success=False,
        notes=["latest repo session"],
    )
    report_path = settings.paths.reports_paper_trading_dir / "saved-session_paper_session.json"
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(report.model_dump_json(indent=2), encoding="utf-8")

    ledger_path = settings.paths.ledger_dir / "signal_outcomes.csv"
    ledger_path.parent.mkdir(parents=True, exist_ok=True)
    with ledger_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=[
                "event_id",
                "session_id",
                "run_id",
                "timestamp",
                "strategy",
                "broker_mode",
                "ownership_class",
                "symbol",
                "signal_source",
                "final_decision_status",
                "rejection_reason_code",
                "predicted_return",
                "qlib_raw_score",
                "candidate_rank",
                "actual_exit_reason",
                "realized_pnl",
            ],
        )
        writer.writeheader()
        writer.writerow(
            {
                "event_id": "event-1",
                "session_id": "saved-session",
                "run_id": "saved-run",
                "timestamp": "2026-03-27T09:31:00Z",
                "strategy": "scalping",
                "broker_mode": "alpaca_paper_api",
                "ownership_class": "bot_owned",
                "symbol": "TSLA",
                "signal_source": "qlib_plus_rules",
                "final_decision_status": "accepted_bracket_short",
                "rejection_reason_code": "",
                "predicted_return": "-0.007",
                "qlib_raw_score": "-0.007",
                "candidate_rank": "1",
                "actual_exit_reason": "",
                "realized_pnl": "",
            }
        )


def test_status_reference_service_builds_profile_sections_and_saved_trading_track(
    tmp_path: Path,
) -> None:
    settings = _build_settings(tmp_path)
    wizard_service = SetupWizardService(settings=settings)
    state = wizard_service.initialize_wizard(profile_name="Alice Trader", source_mode="create_new")
    state.universe.selection_mode = "replace_with_new"
    wizard_service.finalize_setup(state, generated_symbols=["AAPL", "MSFT"])
    _write_saved_session_artifacts(settings)

    service = StatusReferenceService(TradingPlatformService(settings=settings))

    payload = service.get_payload()

    assert payload.default_profile_name == "Alice Trader"
    assert payload.selected_profile_name == "Alice Trader"
    assert any(section.title == "Alpha & Model" for section in payload.sections)
    assert any(section.title == "Artifact Readiness" for section in payload.sections)
    assert payload.trading_track.latest_saved_session is not None
    assert payload.trading_track.latest_saved_session.session_id == "saved-session"
    assert payload.trading_track.recent_activity
    assert payload.trading_track.recent_activity[0].symbol == "TSLA"
    assert payload.trading_track.description


def test_status_reference_service_prefers_current_session_when_available(tmp_path: Path) -> None:
    settings = _build_settings(tmp_path)
    wizard_service = SetupWizardService(settings=settings)
    state = wizard_service.initialize_wizard(profile_name="Alice Trader", source_mode="create_new")
    wizard_service.finalize_setup(state, generated_symbols=["AAPL", "MSFT"])

    platform_service = TradingPlatformService(settings=settings)
    platform_service.last_session_result = SessionResult(
        session_summary=SessionSummary(
            session_id="current-session",
            strategy_name="scalping",
            mode=RuntimeMode.PAPER,
            trade_count=2,
            rejected_trade_count=3,
        ),
        prediction_status=ArtifactStatus.ready("predictions", freshness_minutes=5),
        health_status=HealthStatus(summary="Session completed.", ok=True),
    )

    payload = StatusReferenceService(platform_service).get_payload(profile_name="Alice Trader")

    assert payload.trading_track.current_session is not None
    assert payload.trading_track.current_session.session_id == "current-session"
