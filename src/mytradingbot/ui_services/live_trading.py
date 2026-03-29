"""Live trading UI services."""

from __future__ import annotations

import json
import os
import platform
import signal
import subprocess
from pathlib import Path
from typing import Callable

from pydantic import BaseModel, Field

from mytradingbot.brokers.alpaca import AlpacaBrokerScaffold
from mytradingbot.orchestration.service import TradingPlatformService


def _default_process_exists(pid: int) -> bool:
    if pid <= 0:
        return False
    if platform.system() == "Windows":
        result = subprocess.run(  # noqa: S603
            ["tasklist", "/FI", f"PID eq {pid}"],
            capture_output=True,
            text=True,
            check=False,
        )
        return str(pid) in result.stdout
    try:
        os.kill(pid, 0)
    except OSError:
        return False
    return True


def _default_terminate_process(pid: int) -> None:
    if platform.system() == "Windows":
        result = subprocess.run(  # noqa: S603
            ["taskkill", "/PID", str(pid), "/T", "/F"],
            capture_output=True,
            text=True,
            check=False,
        )
        if result.returncode != 0:
            message = result.stderr.strip() or result.stdout.strip() or "taskkill failed"
            raise RuntimeError(message)
        return
    os.kill(pid, signal.SIGTERM)


class RunningSessionPayload(BaseModel):
    """Visible summary for a PID-managed background session."""

    profile_slug: str
    profile_name: str
    pid: int
    is_running: bool
    strategy_name: str | None = None
    broker_mode: str | None = None
    session_mode: str | None = None
    active_symbols_path: str | None = None
    active_symbol_count: int | None = None
    session_config_path: str | None = None
    stdout_log_path: str | None = None
    stderr_log_path: str | None = None
    shared_loop_log_path: str | None = None
    latest_session_report_path: str | None = None
    latest_decision_audit_path: str | None = None
    stdout_log_tail: list[str] = Field(default_factory=list)
    stderr_log_tail: list[str] = Field(default_factory=list)
    shared_loop_log_tail: list[str] = Field(default_factory=list)


class TerminateSessionResult(BaseModel):
    """Result of a user-triggered PID termination action."""

    ok: bool
    message: str
    profile_slug: str
    pid: int | None = None


class LiveTradingPayload(BaseModel):
    """Payload for the live trading page."""

    enabled: bool
    message: str
    validation_only: bool = True
    running_sessions: list[RunningSessionPayload] = Field(default_factory=list)


class LiveTradingService:
    """Expose visible but gated live trading status and running-session controls."""

    def __init__(
        self,
        platform_service: TradingPlatformService,
        *,
        scaffold: AlpacaBrokerScaffold | None = None,
        process_exists: Callable[[int], bool] | None = None,
        terminate_process: Callable[[int], None] | None = None,
    ) -> None:
        self.platform_service = platform_service
        self.scaffold = scaffold or AlpacaBrokerScaffold()
        self._process_exists = process_exists or _default_process_exists
        self._terminate_process = terminate_process or _default_terminate_process

    def get_payload(self) -> LiveTradingPayload:
        capability = self.scaffold.get_live_capability_status()
        return LiveTradingPayload(
            enabled=capability.is_enabled,
            message=capability.message,
            validation_only=True,
            running_sessions=self.list_running_sessions(),
        )

    def list_running_sessions(self) -> list[RunningSessionPayload]:
        runtime_dir = self.platform_service.settings.paths.runtime_dir
        sessions: list[RunningSessionPayload] = []
        for pid_path in sorted(runtime_dir.glob("*_wizard_session.pid")):
            session = self._load_running_session(pid_path)
            if session is not None:
                sessions.append(session)
        return sessions

    def terminate_session(self, profile_slug: str) -> TerminateSessionResult:
        pid_path = self.platform_service.settings.paths.runtime_dir / f"{profile_slug}_wizard_session.pid"
        if not pid_path.exists():
            return TerminateSessionResult(
                ok=False,
                message="No PID file exists for the selected session.",
                profile_slug=profile_slug,
            )
        raw_pid = pid_path.read_text(encoding="utf-8").strip()
        try:
            pid = int(raw_pid)
        except ValueError:
            pid_path.unlink(missing_ok=True)
            return TerminateSessionResult(
                ok=False,
                message="The PID file was invalid and has been cleared.",
                profile_slug=profile_slug,
            )
        if not self._process_exists(pid):
            pid_path.unlink(missing_ok=True)
            return TerminateSessionResult(
                ok=False,
                message="No running process was found for the recorded PID. The stale PID file was cleared.",
                profile_slug=profile_slug,
                pid=pid,
            )
        self._terminate_process(pid)
        if self._process_exists(pid):
            return TerminateSessionResult(
                ok=False,
                message="The process termination request returned, but the session still appears to be running.",
                profile_slug=profile_slug,
                pid=pid,
            )
        pid_path.unlink(missing_ok=True)
        return TerminateSessionResult(
            ok=True,
            message="The background trading session was terminated successfully.",
            profile_slug=profile_slug,
            pid=pid,
        )

    def _load_running_session(self, pid_path: Path) -> RunningSessionPayload | None:
        raw_pid = pid_path.read_text(encoding="utf-8").strip()
        try:
            pid = int(raw_pid)
        except ValueError:
            return None
        profile_slug = pid_path.name.removesuffix("_wizard_session.pid")
        session_config_path = (
            self.platform_service.settings.paths.session_profiles_dir / f"{profile_slug}_latest.json"
        )
        config = self._read_json(session_config_path)
        strategy = config.get("strategy", {}) if isinstance(config, dict) else {}
        universe = config.get("universe", {}) if isinstance(config, dict) else {}
        active_symbols_path = (
            config.get("active_symbols_path")
            or universe.get("active_symbols_path")
            or str(
                self.platform_service.settings.paths.active_universes_dir
                / f"{profile_slug}_active_symbols.json"
            )
        )
        active_symbol_count = universe.get("active_symbol_count")
        if active_symbol_count is None:
            active_symbol_count = self._count_active_symbols(Path(active_symbols_path))
        stdout_log = self.platform_service.settings.paths.logs_dir / f"{profile_slug}_wizard_stdout.log"
        stderr_log = self.platform_service.settings.paths.logs_dir / f"{profile_slug}_wizard_stderr.log"
        shared_loop_log = self.platform_service.settings.paths.logs_dir / "paper_trading_loop.log"
        latest_session_report = self._latest_path(
            self.platform_service.settings.paths.reports_paper_trading_dir,
            "*_paper_session.md",
        )
        latest_decision_audit = self._latest_path(
            self.platform_service.settings.paths.reports_signals_dir,
            "*_decision_audit.md",
        )
        return RunningSessionPayload(
            profile_slug=profile_slug,
            profile_name=str(config.get("profile_name") or profile_slug),
            pid=pid,
            is_running=self._process_exists(pid),
            strategy_name=strategy.get("strategy_name"),
            broker_mode=strategy.get("broker_mode"),
            session_mode=strategy.get("session_mode"),
            active_symbols_path=str(active_symbols_path),
            active_symbol_count=active_symbol_count,
            session_config_path=str(session_config_path),
            stdout_log_path=str(stdout_log),
            stderr_log_path=str(stderr_log),
            shared_loop_log_path=str(shared_loop_log),
            latest_session_report_path=str(latest_session_report) if latest_session_report else None,
            latest_decision_audit_path=str(latest_decision_audit) if latest_decision_audit else None,
            stdout_log_tail=self._tail_lines(stdout_log),
            stderr_log_tail=self._tail_lines(stderr_log),
            shared_loop_log_tail=self._tail_lines(shared_loop_log),
        )

    @staticmethod
    def _read_json(path: Path) -> dict:
        if not path.exists():
            return {}
        try:
            payload = json.loads(path.read_text(encoding="utf-8-sig"))
        except (json.JSONDecodeError, OSError):
            return {}
        return payload if isinstance(payload, dict) else {}

    @staticmethod
    def _tail_lines(path: Path, *, line_count: int = 20) -> list[str]:
        if not path.exists():
            return []
        lines = path.read_text(encoding="utf-8", errors="ignore").splitlines()
        return lines[-line_count:]

    @staticmethod
    def _latest_path(directory: Path, pattern: str) -> Path | None:
        matches = sorted(directory.glob(pattern), key=lambda item: item.stat().st_mtime, reverse=True)
        return matches[0] if matches else None

    @staticmethod
    def _count_active_symbols(path: Path) -> int | None:
        if not path.exists():
            return None
        try:
            payload = json.loads(path.read_text(encoding="utf-8-sig"))
        except (json.JSONDecodeError, OSError):
            return None
        if isinstance(payload, list):
            return len(payload)
        if isinstance(payload, dict) and isinstance(payload.get("symbols"), list):
            return len(payload["symbols"])
        return None
