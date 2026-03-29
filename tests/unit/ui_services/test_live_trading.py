from __future__ import annotations

import json
from pathlib import Path

from mytradingbot.core.paths import RepoPaths
from mytradingbot.core.settings import AppSettings
from mytradingbot.orchestration.service import TradingPlatformService
from mytradingbot.ui_services.live_trading import LiveTradingService


def _build_settings(repo_root: Path) -> AppSettings:
    settings = AppSettings(paths=RepoPaths.for_root(repo_root))
    settings.ensure_runtime_directories()
    return settings


def test_live_trading_service_surfaces_running_wizard_session(tmp_path: Path) -> None:
    settings = _build_settings(tmp_path)
    profile_slug = "nathan_1st_test"
    pid_path = settings.paths.runtime_dir / f"{profile_slug}_wizard_session.pid"
    session_config_path = settings.paths.session_profiles_dir / f"{profile_slug}_latest.json"
    active_symbols_path = settings.paths.active_universes_dir / f"{profile_slug}_active_symbols.json"
    stdout_log_path = settings.paths.logs_dir / f"{profile_slug}_wizard_stdout.log"
    stderr_log_path = settings.paths.logs_dir / f"{profile_slug}_wizard_stderr.log"
    report_path = settings.paths.reports_paper_trading_dir / "abc_paper_session.md"
    audit_path = settings.paths.reports_signals_dir / "abc_decision_audit.md"

    pid_path.write_text("4242", encoding="utf-8")
    session_config_path.write_text(
        json.dumps(
            {
                "profile_name": "Nathan 1st Test",
                "profile_slug": profile_slug,
                "strategy": {
                    "strategy_name": "scalping",
                    "broker_mode": "alpaca_paper_api",
                    "session_mode": "loop",
                },
                "active_symbols_path": str(active_symbols_path),
            }
        ),
        encoding="utf-8",
    )
    active_symbols_path.write_text(json.dumps(["AAPL", "MSFT"]), encoding="utf-8")
    stdout_log_path.write_text("stdout line 1\nstdout line 2\n", encoding="utf-8")
    stderr_log_path.write_text("stderr line 1\nstderr line 2\n", encoding="utf-8")
    report_path.write_text("# latest report\n", encoding="utf-8")
    audit_path.write_text("# latest audit\n", encoding="utf-8")

    service = LiveTradingService(
        TradingPlatformService(settings=settings),
        process_exists=lambda pid: pid == 4242,
    )

    payload = service.get_payload()

    assert payload.running_sessions
    session = payload.running_sessions[0]
    assert session.profile_slug == profile_slug
    assert session.profile_name == "Nathan 1st Test"
    assert session.pid == 4242
    assert session.is_running is True
    assert session.strategy_name == "scalping"
    assert session.broker_mode == "alpaca_paper_api"
    assert session.session_mode == "loop"
    assert session.active_symbols_path == str(active_symbols_path)
    assert session.stdout_log_tail[-1] == "stdout line 2"
    assert session.stderr_log_tail[-1] == "stderr line 2"
    assert session.latest_session_report_path == str(report_path)
    assert session.latest_decision_audit_path == str(audit_path)


def test_live_trading_service_terminates_running_wizard_session_and_clears_pid(tmp_path: Path) -> None:
    settings = _build_settings(tmp_path)
    profile_slug = "nathan_1st_test"
    pid_path = settings.paths.runtime_dir / f"{profile_slug}_wizard_session.pid"
    session_config_path = settings.paths.session_profiles_dir / f"{profile_slug}_latest.json"

    pid_path.write_text("5151", encoding="utf-8")
    session_config_path.write_text(
        json.dumps(
            {
                "profile_name": "Nathan 1st Test",
                "profile_slug": profile_slug,
                "strategy": {
                    "strategy_name": "scalping",
                    "broker_mode": "alpaca_paper_api",
                    "session_mode": "loop",
                },
            }
        ),
        encoding="utf-8",
    )

    running = {5151}
    terminated: list[int] = []

    def process_exists(pid: int) -> bool:
        return pid in running

    def terminate_process(pid: int) -> None:
        terminated.append(pid)
        running.discard(pid)

    service = LiveTradingService(
        TradingPlatformService(settings=settings),
        process_exists=process_exists,
        terminate_process=terminate_process,
    )

    result = service.terminate_session(profile_slug)

    assert result.ok is True
    assert result.pid == 5151
    assert terminated == [5151]
    assert not pid_path.exists()


def test_live_trading_service_handles_missing_or_stale_process_gracefully(tmp_path: Path) -> None:
    settings = _build_settings(tmp_path)
    profile_slug = "nathan_1st_test"
    pid_path = settings.paths.runtime_dir / f"{profile_slug}_wizard_session.pid"
    session_config_path = settings.paths.session_profiles_dir / f"{profile_slug}_latest.json"

    pid_path.write_text("9191", encoding="utf-8")
    session_config_path.write_text(
        json.dumps(
            {
                "profile_name": "Nathan 1st Test",
                "profile_slug": profile_slug,
                "strategy": {
                    "strategy_name": "scalping",
                    "broker_mode": "alpaca_paper_api",
                    "session_mode": "loop",
                },
            }
        ),
        encoding="utf-8",
    )

    service = LiveTradingService(
        TradingPlatformService(settings=settings),
        process_exists=lambda pid: False,
    )

    payload = service.get_payload()
    result = service.terminate_session(profile_slug)

    assert payload.running_sessions[0].is_running is False
    assert result.ok is False
    assert result.pid == 9191
