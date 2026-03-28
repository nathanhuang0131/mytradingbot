"""Generate overnight trading universe audit reports from repo-local artifacts."""

from __future__ import annotations

import json
from collections import Counter
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
from pathlib import Path

from mytradingbot.core.settings import AppSettings


@dataclass
class SymbolDecisionTrace:
    symbol: str
    signal_source: str
    qlib_raw_score: float | None
    predicted_return: float | None
    expected_edge_after_cost: float | None
    quality_score: float | None
    higher_timeframe_state: str | None
    passed_filters: list[str]
    failed_filters: list[str]
    final_decision_status: str
    final_rejection_reason_code: str | None
    final_rejection_reason_detail: str | None
    reason: str


@dataclass
class SessionAudit:
    session_id: str
    run_id: str | None
    started_at: datetime
    completed_at: datetime
    candidate_symbols: list[str]
    approved_symbols: list[str]
    blocked_symbols: list[str]
    top_rejection_reasons: list[str]
    traces: list[SymbolDecisionTrace]


class TradingUniverseAuditService:
    """Build a readable overnight trading universe audit from session artifacts."""

    def __init__(self, *, settings: AppSettings | None = None) -> None:
        self.settings = settings or AppSettings()

    def generate(self, *, profile_slug: str | None = None, lookback_hours: int = 12) -> Path:
        self.settings.ensure_runtime_directories()

        profile = self._load_profile(profile_slug=profile_slug)
        resolved_profile_slug = str(
            profile.get("profile_slug")
            or profile_slug
            or "latest_profile"
        )
        profile_name = str(profile.get("profile_name") or resolved_profile_slug)
        active_symbols_path = self._active_symbols_path(profile=profile, profile_slug=resolved_profile_slug)
        active_symbols = self._load_active_symbols(
            active_symbols_path=active_symbols_path,
            embedded_symbols=profile.get("active_symbols"),
        )

        session_payloads = self._load_session_payloads()
        if not session_payloads:
            raise FileNotFoundError("No paper session JSON artifacts were found under reports/paper_trading.")

        anchor_completed_at = max(payload["completed_at"] for payload in session_payloads)
        window_start = anchor_completed_at - timedelta(hours=lookback_hours)
        selected_payloads = [
            payload
            for payload in session_payloads
            if window_start <= payload["completed_at"] <= anchor_completed_at
        ]
        selected_payloads.sort(key=lambda payload: payload["completed_at"])

        session_audits = [
            self._build_session_audit(payload=payload)
            for payload in selected_payloads
        ]

        overnight_dir = self.settings.paths.reports_dir / "overnight"
        overnight_dir.mkdir(parents=True, exist_ok=True)
        filename = f"{anchor_completed_at.strftime('%Y%m%dT%H%M%SZ')}_{resolved_profile_slug}_trading_universe_audit.md"
        report_path = overnight_dir / filename
        report_path.write_text(
            self._render_markdown(
                profile_name=profile_name,
                profile_slug=resolved_profile_slug,
                active_symbols_path=active_symbols_path,
                active_symbols=active_symbols,
                lookback_hours=lookback_hours,
                window_start=window_start,
                anchor_completed_at=anchor_completed_at,
                session_audits=session_audits,
            ),
            encoding="utf-8",
        )
        return report_path

    def _load_profile(self, *, profile_slug: str | None) -> dict:
        if profile_slug:
            path = self.settings.paths.session_profiles_dir / f"{profile_slug}_latest.json"
            if not path.exists():
                raise FileNotFoundError(f"Session profile not found: {path}")
            return self._read_json(path)

        candidates = sorted(
            self.settings.paths.session_profiles_dir.glob("*_latest.json"),
            key=lambda path: path.stat().st_mtime,
            reverse=True,
        )
        if not candidates:
            raise FileNotFoundError("No session profile JSON files were found under data/runtime/session_profiles.")
        return self._read_json(candidates[0])

    def _active_symbols_path(self, *, profile: dict, profile_slug: str) -> Path:
        universe = profile.get("universe", {}) if isinstance(profile.get("universe"), dict) else {}
        raw_path = (
            profile.get("active_symbols_path")
            or universe.get("active_symbols_path")
            or self.settings.paths.active_universes_dir / f"{profile_slug}_active_symbols.json"
        )
        return Path(raw_path)

    def _load_active_symbols(self, *, active_symbols_path: Path, embedded_symbols: object) -> list[str]:
        if active_symbols_path.exists():
            payload = self._read_json(active_symbols_path)
            if isinstance(payload, list):
                return [str(symbol) for symbol in payload]
            if isinstance(payload, dict) and isinstance(payload.get("symbols"), list):
                return [str(symbol) for symbol in payload["symbols"]]
        if isinstance(embedded_symbols, list):
            return [str(symbol) for symbol in embedded_symbols]
        return []

    def _load_session_payloads(self) -> list[dict]:
        payloads: list[dict] = []
        for path in self.settings.paths.reports_paper_trading_dir.glob("*_paper_session.json"):
            payload = self._read_json(path)
            if not isinstance(payload, dict):
                continue
            session_id = payload.get("session_id")
            started_at = self._parse_timestamp(payload.get("started_at"))
            completed_at = self._parse_timestamp(payload.get("completed_at"))
            if not session_id or started_at is None or completed_at is None:
                continue
            payloads.append(
                {
                    "path": path,
                    "session_id": str(session_id),
                    "run_id": payload.get("run_id"),
                    "started_at": started_at,
                    "completed_at": completed_at,
                    "order_count": int(payload.get("order_count", 0) or 0),
                    "accepted_count": int(payload.get("accepted_count", 0) or 0),
                    "rejected_count": int(payload.get("rejected_count", 0) or 0),
                    "skipped_count": int(payload.get("skipped_count", 0) or 0),
                }
            )
        return payloads

    def _build_session_audit(self, *, payload: dict) -> SessionAudit:
        session_id = payload["session_id"]
        audit_path = self.settings.paths.reports_signals_dir / f"{session_id}_decision_audit.json"
        audit_rows = self._read_json(audit_path) if audit_path.exists() else []
        if not isinstance(audit_rows, list):
            audit_rows = []

        traces: list[SymbolDecisionTrace] = []
        rejection_counter: Counter[str] = Counter()
        approved_symbols: list[str] = []
        blocked_symbols: list[str] = []
        candidate_symbols: list[str] = []

        for row in audit_rows:
            if not isinstance(row, dict):
                continue
            symbol = str(row.get("symbol") or "UNKNOWN")
            candidate_symbols.append(symbol)
            passed_filters, failed_filters = self._split_rule_checks(row.get("rule_checks"))
            final_status = str(row.get("final_decision_status") or "unknown")
            rejection_code = self._optional_text(row.get("final_rejection_reason_code"))
            rejection_detail = self._optional_text(row.get("final_rejection_reason_detail"))
            if final_status.startswith("accepted"):
                approved_symbols.append(symbol)
            else:
                blocked_symbols.append(symbol)
                if rejection_code:
                    rejection_counter[rejection_code] += 1
                elif failed_filters:
                    rejection_counter[failed_filters[0]] += 1
                else:
                    rejection_counter[final_status] += 1
            traces.append(
                SymbolDecisionTrace(
                    symbol=symbol,
                    signal_source=str(row.get("signal_source") or "unknown"),
                    qlib_raw_score=self._optional_float(row.get("qlib_raw_score")),
                    predicted_return=self._optional_float(row.get("predicted_return")),
                    expected_edge_after_cost=self._optional_float(
                        row.get("expected_edge_after_cost")
                    ),
                    quality_score=self._optional_float(row.get("quality_score")),
                    higher_timeframe_state=self._optional_text(
                        row.get("higher_timeframe_state")
                    ),
                    passed_filters=passed_filters,
                    failed_filters=failed_filters,
                    final_decision_status=final_status,
                    final_rejection_reason_code=rejection_code,
                    final_rejection_reason_detail=rejection_detail,
                    reason=self._build_reason(
                        final_status=final_status,
                        rejection_code=rejection_code,
                        rejection_detail=rejection_detail,
                        failed_filters=failed_filters,
                    ),
                )
            )

        top_rejection_reasons = [
            f"{reason} ({count})"
            for reason, count in rejection_counter.most_common(5)
        ]
        return SessionAudit(
            session_id=session_id,
            run_id=self._optional_text(payload.get("run_id")),
            started_at=payload["started_at"],
            completed_at=payload["completed_at"],
            candidate_symbols=candidate_symbols,
            approved_symbols=approved_symbols,
            blocked_symbols=blocked_symbols,
            top_rejection_reasons=top_rejection_reasons,
            traces=traces,
        )

    @staticmethod
    def _split_rule_checks(rule_checks: object) -> tuple[list[str], list[str]]:
        passed: list[str] = []
        failed: list[str] = []
        if not isinstance(rule_checks, list):
            return passed, failed
        for check in rule_checks:
            if not isinstance(check, dict):
                continue
            name = check.get("name")
            if not name:
                continue
            if bool(check.get("passed")):
                passed.append(str(name))
            else:
                failed.append(str(name))
        return passed, failed

    @staticmethod
    def _build_reason(
        *,
        final_status: str,
        rejection_code: str | None,
        rejection_detail: str | None,
        failed_filters: list[str],
    ) -> str:
        if final_status.startswith("accepted"):
            return "Traded because the qlib candidate passed all recorded freshness, strategy, risk, and execution checks."
        if rejection_detail and rejection_code:
            return f"Not traded because {rejection_detail} ({rejection_code})."
        if rejection_code:
            return f"Not traded because {rejection_code}."
        if failed_filters:
            return f"Not traded because {', '.join(failed_filters)}."
        return f"Not traded because the final decision ended as {final_status}."

    def _render_markdown(
        self,
        *,
        profile_name: str,
        profile_slug: str,
        active_symbols_path: Path,
        active_symbols: list[str],
        lookback_hours: int,
        window_start: datetime,
        anchor_completed_at: datetime,
        session_audits: list[SessionAudit],
    ) -> str:
        total_candidates = sum(len(session.candidate_symbols) for session in session_audits)
        total_approved = sum(len(session.approved_symbols) for session in session_audits)
        total_blocked = sum(len(session.blocked_symbols) for session in session_audits)

        lines = [
            "# Trading Universe Audit",
            "",
            "## Loop Overview",
            "",
            f"- profile_name: `{profile_name}`",
            f"- profile_slug: `{profile_slug}`",
            f"- Configured overnight universe: `{len(active_symbols)}` symbols",
            f"- active_symbols_path: `{active_symbols_path}`",
            f"- lookback_hours: `{lookback_hours}`",
            f"- session_window_start_utc: `{self._format_timestamp(window_start)}`",
            f"- session_window_end_utc: `{self._format_timestamp(anchor_completed_at)}`",
            f"- sessions_included: `{len(session_audits)}`",
            f"- total_qlib_candidates_audited: `{total_candidates}`",
            f"- total_trade_approved_symbols: `{total_approved}`",
            f"- total_blocked_symbols: `{total_blocked}`",
            "",
            "## Session Summary",
            "",
            "| Session ID | Started (UTC) | Completed (UTC) | Qlib Candidates | Trade-Approved | Blocked | Top Rejection Reasons |",
            "| --- | --- | --- | ---: | ---: | ---: | --- |",
        ]

        for session in session_audits:
            reasons = ", ".join(session.top_rejection_reasons) if session.top_rejection_reasons else "none"
            lines.append(
                f"| {session.session_id} | {self._format_timestamp(session.started_at)} | "
                f"{self._format_timestamp(session.completed_at)} | {len(session.candidate_symbols)} | "
                f"{len(session.approved_symbols)} | {len(session.blocked_symbols)} | {reasons} |"
            )

        for session in session_audits:
            lines.extend(
                [
                    "",
                    f"## Session `{session.session_id}`",
                    "",
                    f"- run_id: `{session.run_id or 'unknown'}`",
                    f"- started_at_utc: `{self._format_timestamp(session.started_at)}`",
                    f"- completed_at_utc: `{self._format_timestamp(session.completed_at)}`",
                    f"- Qlib candidate universe ({len(session.candidate_symbols)}): {self._format_symbol_list(session.candidate_symbols)}",
                    f"- Trade-approved symbols ({len(session.approved_symbols)}): {self._format_symbol_list(session.approved_symbols)}",
                    f"- Blocked symbols ({len(session.blocked_symbols)}): {self._format_symbol_list(session.blocked_symbols)}",
                    f"- top rejection reasons: {', '.join(session.top_rejection_reasons) if session.top_rejection_reasons else 'none'}",
                    "",
                    "| Symbol | Qlib Score | Predicted Return | Edge After Cost | Quality Score | HTF Trend | Signal Source | Passed Filters | Failed Filters | Final Decision | Decision Reason |",
                    "| --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- | --- |",
                ]
            )
            for trace in session.traces:
                passed_filters = ", ".join(trace.passed_filters) if trace.passed_filters else "none"
                failed_filters = ", ".join(trace.failed_filters) if trace.failed_filters else "none"
                score = f"{trace.qlib_raw_score:.4f}" if trace.qlib_raw_score is not None else "n/a"
                predicted_return = (
                    f"{trace.predicted_return:.4f}" if trace.predicted_return is not None else "n/a"
                )
                expected_edge_after_cost = (
                    f"{trace.expected_edge_after_cost:.4f}"
                    if trace.expected_edge_after_cost is not None
                    else "n/a"
                )
                quality_score = (
                    f"{trace.quality_score:.4f}" if trace.quality_score is not None else "n/a"
                )
                lines.append(
                    f"| {trace.symbol} | {score} | {predicted_return} | {expected_edge_after_cost} | "
                    f"{quality_score} | {trace.higher_timeframe_state or 'n/a'} | {trace.signal_source} | "
                    f"{passed_filters} | {failed_filters} | {trace.final_decision_status} | {trace.reason} |"
                )
        lines.append("")
        return "\n".join(lines)

    @staticmethod
    def _format_symbol_list(symbols: list[str]) -> str:
        if not symbols:
            return "none"
        return ", ".join(f"`{symbol}`" for symbol in symbols)

    @staticmethod
    def _format_timestamp(value: datetime) -> str:
        return value.astimezone(timezone.utc).strftime("%Y-%m-%d %H:%M:%SZ")

    @staticmethod
    def _parse_timestamp(value: object) -> datetime | None:
        if not value:
            return None
        text = str(value)
        if text.endswith("Z"):
            text = text[:-1] + "+00:00"
        return datetime.fromisoformat(text).astimezone(timezone.utc)

    @staticmethod
    def _read_json(path: Path) -> object:
        return json.loads(path.read_text(encoding="utf-8-sig"))

    @staticmethod
    def _optional_text(value: object) -> str | None:
        if value is None:
            return None
        text = str(value).strip()
        return text or None

    @staticmethod
    def _optional_float(value: object) -> float | None:
        if value is None:
            return None
        try:
            return float(value)
        except (TypeError, ValueError):
            return None
