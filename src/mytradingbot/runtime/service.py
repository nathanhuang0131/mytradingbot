"""Runtime-state coordination, freshness gates, and audit/report writing."""

from __future__ import annotations

import csv
import json
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

from mytradingbot.core.enums import RuntimeMode
from mytradingbot.core.models import (
    ArtifactStatus,
    BrokerOrder,
    FillEvent,
    PositionSnapshot,
    TradeAttemptTrace,
    utc_now,
)
from mytradingbot.core.settings import AppSettings
from mytradingbot.runtime.models import (
    DecisionAuditRecord,
    FillLifecycleRecord,
    OrderLifecycleRecord,
    PaperTradingSessionReport,
    RejectionReasonCode,
    RuleCheckRecord,
    RuntimeIncidentRecord,
    RuntimeSessionContext,
    SignalOutcomeLedgerRow,
    SignalSource,
)
from mytradingbot.runtime.store import RuntimeStateStore


FILTER_REASON_MAP: dict[str, RejectionReasonCode] = {
    "predicted_return_threshold": "target_return_below_threshold",
    "confidence_threshold": "score_below_threshold",
    "spread_filter": "spread_too_wide",
    "liquidity_filter": "liquidity_too_low",
    "intraday_volatility_regime": "volatility_regime_blocked",
    "order_book_imbalance": "imbalance_not_confirmed",
    "liquidity_sweep_detection": "liquidity_sweep_not_confirmed",
    "cooldown_logic": "cooldown_active",
    "duplicate_position": "position_exists",
    "missing_market_data": "missing_market_data",
    "fee_adjusted_expectancy": "bracket_invalid",
    "invalid_broker_quantity": "bracket_invalid",
    "bracket_plan_invalid_after_rounding": "bracket_invalid",
    "live_mode_disabled": "execution_guard_blocked",
    "position_exists": "position_exists",
    "execution_guard_blocked": "execution_guard_blocked",
    "stale_predictions": "stale_predictions",
    "stale_market_snapshot": "stale_market_snapshot",
}


class RuntimeStateService:
    """Persist runtime truth and write audit/report artifacts."""

    def __init__(
        self,
        settings: AppSettings | None = None,
        *,
        store: RuntimeStateStore | None = None,
    ) -> None:
        self.settings = settings or AppSettings()
        self.store = store or RuntimeStateStore(settings=self.settings)

    def create_session_context(self, *, strategy: str, mode: RuntimeMode) -> RuntimeSessionContext:
        context = RuntimeSessionContext(
            started_at=utc_now(),
            strategy=strategy,
            mode=mode,
            prediction_artifact_path=str(self.settings.prediction_artifact_path()),
            model_artifact_path=str(self.settings.qlib_model_artifact_path()),
            dataset_artifact_path=str(self.settings.qlib_dataset_artifact_path()),
            market_snapshot_artifact_path=str(self.settings.market_snapshot_artifact_path()),
        )
        self.store.record_session_start(context)
        return context

    def market_snapshot_status(self, *, market_snapshot_path: Path | None = None) -> ArtifactStatus:
        path = market_snapshot_path or self.settings.market_snapshot_artifact_path()
        if not path.exists():
            return ArtifactStatus.missing(
                "market_snapshot",
                guidance=["Run repo-local maintenance to build a fresh market snapshot artifact."],
            )
        freshness_minutes = int((utc_now().timestamp() - path.stat().st_mtime) / 60)
        if freshness_minutes > self.settings.freshness.market_snapshot_max_age_minutes:
            return ArtifactStatus.stale(
                "market_snapshot",
                freshness_minutes=freshness_minutes,
                guidance=["Refresh market snapshot artifacts before running a new paper session."],
            )
        return ArtifactStatus.ready("market_snapshot", freshness_minutes=freshness_minutes)

    def enrich_signal_metadata(self, *, strategy_name: str, signals: list) -> list:
        cooldowns = self.store.active_cooldowns(strategy=strategy_name, now=utc_now())
        open_positions = self.store.active_position_symbols()
        for signal in signals:
            signal.metadata["cooldown_active"] = signal.symbol in cooldowns
            signal.metadata["position_exists"] = signal.symbol in open_positions
            signal.metadata["minutes_to_close"] = self.minutes_to_close(signal.market.timestamp)
        return signals

    @staticmethod
    def minutes_to_close(timestamp: datetime) -> int:
        eastern = ZoneInfo("America/New_York")
        localized = timestamp.astimezone(eastern)
        open_time = localized.replace(hour=9, minute=30, second=0, microsecond=0)
        close_time = localized.replace(hour=16, minute=0, second=0, microsecond=0)
        if localized < open_time or localized > close_time:
            return 999
        delta = close_time - localized
        return max(0, int(delta.total_seconds() // 60))

    def has_circuit_breaker_block(self) -> bool:
        broker_rejects = self.store.consecutive_incident_count(codes={"broker_rejected"})
        execution_failures = self.store.consecutive_incident_count(codes={"execution_failure"})
        replace_stop_failures = self.store.consecutive_incident_count(codes={"replace_stop_failure"})
        return (
            broker_rejects >= self.settings.runtime_safety.max_consecutive_broker_rejects
            or execution_failures >= self.settings.runtime_safety.max_consecutive_execution_failures
            or replace_stop_failures >= self.settings.runtime_safety.max_consecutive_replace_stop_failures
        )

    def deterministic_client_order_id(self, *, strategy_name: str, signal, side: str) -> str:
        source_ts = signal.market.timestamp.strftime("%Y%m%d%H%M")
        return f"{strategy_name}-{signal.symbol}-{side}-{source_ts}".upper()

    def build_decision_audit(
        self,
        *,
        context: RuntimeSessionContext,
        signal,
        trace: TradeAttemptTrace,
        prediction_status: ArtifactStatus,
        market_status: ArtifactStatus,
    ) -> DecisionAuditRecord:
        strategy_outcome = trace.strategy_outcome
        risk_outcome = trace.risk_outcome
        execution_outcome = trace.execution_outcome
        signal_source: SignalSource = "qlib_candidate_only"
        final_status = "no_action"
        rejection_detail: str | None = None

        if strategy_outcome and strategy_outcome.should_trade:
            signal_source = "qlib_plus_rules"
        if strategy_outcome and not strategy_outcome.should_trade:
            final_status = "rejected"
            rejection_detail = strategy_outcome.reason
        elif risk_outcome and not risk_outcome.approved:
            final_status = "rejected"
            rejection_detail = risk_outcome.reason
        elif execution_outcome and execution_outcome.execution_skipped:
            final_status = "skipped"
            rejection_detail = execution_outcome.reason
        elif execution_outcome and execution_outcome.order is not None:
            if execution_outcome.order.side == "buy" and execution_outcome.request and execution_outcome.request.bracket_plan:
                final_status = "accepted_bracket_buy"
            elif execution_outcome.order.side == "buy":
                final_status = "accepted_buy"
            elif execution_outcome.request and execution_outcome.request.bracket_plan:
                final_status = "accepted_bracket_short"
            else:
                final_status = "accepted_short"

        audit = DecisionAuditRecord(
            session_id=context.session_id,
            run_id=context.run_id,
            correlation_id=trace.attempt_id,
            timestamp=signal.market.timestamp,
            strategy=context.strategy,
            strategy_version=context.strategy_version,
            mode=context.mode,
            symbol=signal.symbol,
            side_considered="buy" if signal.prediction.direction == "long" else "sell",
            bracket_considered=bool(strategy_outcome and strategy_outcome.intent and strategy_outcome.intent.bracket_plan),
            signal_source=signal_source,
            qlib_raw_score=signal.prediction.score,
            predicted_return=signal.prediction.predicted_return,
            target_return=signal.prediction.predicted_return,
            candidate_rank=signal.prediction.rank,
            prediction_artifact_path=context.prediction_artifact_path,
            model_artifact_path=context.model_artifact_path,
            dataset_artifact_path=context.dataset_artifact_path,
            source_data_timestamp=signal.market.timestamp,
            source_data_freshness_minutes=market_status.freshness_minutes,
            rule_checks=self._build_rule_checks(
                signal=signal,
                trace=trace,
                prediction_status=prediction_status,
                market_status=market_status,
            ),
            final_decision_status=final_status,
            final_rejection_reason_code=self.map_rejection_reason(rejection_detail),
            final_rejection_reason_detail=rejection_detail,
            notes=list(trace.notes),
        )
        self.store.record_decision(audit)
        self._append_signal_ledger(audit)
        return audit

    def record_execution_result(
        self,
        *,
        context: RuntimeSessionContext,
        strategy_name: str,
        result,
    ) -> None:
        if result.order is not None:
            self.store.record_order(
                OrderLifecycleRecord(
                    order_id=result.order.order_id,
                    session_id=context.session_id,
                    run_id=context.run_id,
                    strategy=strategy_name,
                    mode=context.mode,
                    symbol=result.order.symbol,
                    side=result.order.side,
                    quantity=result.order.quantity,
                    client_order_id=result.order.client_order_id,
                    status=result.order.status,
                    submitted_at=result.order.submitted_at,
                    avg_fill_price=result.order.avg_fill_price,
                    metadata=result.order.metadata,
                )
            )
        for fill in result.fills:
            self.store.record_fill(
                FillLifecycleRecord(
                    fill_id=fill.fill_id,
                    order_id=fill.order_id,
                    session_id=context.session_id,
                    run_id=context.run_id,
                    strategy=strategy_name,
                    mode=context.mode,
                    symbol=fill.symbol,
                    quantity=fill.quantity,
                    price=fill.price,
                    filled_at=fill.filled_at,
                    metadata=fill.metadata,
                )
            )
        if result.position is not None:
            self.store.record_position(result.position)
        if result.bracket_state is not None:
            self.store.record_bracket(result.bracket_state)
            if result.bracket_state.status == "closed" and result.bracket_state.closed_at is not None:
                self.store.set_cooldown(
                    symbol=result.bracket_state.symbol,
                    strategy=strategy_name,
                    expires_at=result.bracket_state.closed_at,
                )

    def build_incident(
        self,
        *,
        context: RuntimeSessionContext | None,
        code: str,
        summary: str,
        detail: str | None = None,
        severity: str = "warning",
        metadata: dict | None = None,
    ) -> RuntimeIncidentRecord:
        incident = RuntimeIncidentRecord(
            session_id=context.session_id if context else None,
            run_id=context.run_id if context else None,
            timestamp=utc_now(),
            code=code,
            severity=severity,  # type: ignore[arg-type]
            summary=summary,
            detail=detail,
            metadata=metadata or {},
        )
        self.store.record_incident(incident)
        self._append_incident_ledger(incident)
        return incident

    def write_session_artifacts(
        self,
        *,
        context: RuntimeSessionContext,
        audits: list[DecisionAuditRecord],
        orders: list[BrokerOrder],
        fills: list[FillEvent],
        positions: list[PositionSnapshot],
        incidents: list[RuntimeIncidentRecord],
        notes: list[str],
    ) -> PaperTradingSessionReport:
        paths = self._paths(context)
        paths["audit_json"].write_text(
            json.dumps([audit.model_dump(mode="json") for audit in audits], indent=2),
            encoding="utf-8",
        )
        self._write_csv(
            paths["audit_csv"],
            [
                {
                    "event_id": audit.event_id,
                    "symbol": audit.symbol,
                    "signal_source": audit.signal_source,
                    "final_decision_status": audit.final_decision_status,
                    "rejection_reason_code": audit.final_rejection_reason_code,
                    "predicted_return": audit.predicted_return,
                    "qlib_raw_score": audit.qlib_raw_score,
                    "candidate_rank": audit.candidate_rank,
                }
                for audit in audits
            ],
        )
        paths["audit_md"].write_text(self._render_audit_markdown(audits), encoding="utf-8")

        accepted_count = len([audit for audit in audits if audit.final_decision_status.startswith("accepted")])
        rejected_count = len([audit for audit in audits if audit.final_decision_status == "rejected"])
        skipped_count = len([audit for audit in audits if audit.final_decision_status == "skipped"])
        report = PaperTradingSessionReport(
            session_id=context.session_id,
            run_id=context.run_id,
            strategy=context.strategy,
            mode=context.mode,
            started_at=context.started_at,
            completed_at=utc_now(),
            order_count=len(orders),
            fill_count=len(fills),
            accepted_count=accepted_count,
            rejected_count=rejected_count,
            skipped_count=skipped_count,
            no_trade_success=len(orders) == 0,
            artifact_paths=[
                context.prediction_artifact_path,
                context.model_artifact_path,
                context.dataset_artifact_path,
                context.market_snapshot_artifact_path,
            ],
            report_paths=[str(paths[key]) for key in ("audit_json", "audit_csv", "audit_md", "session_json", "session_md", "analytics_md")],
            incident_count=len(incidents),
            notes=notes,
        )
        paths["session_json"].write_text(report.model_dump_json(indent=2), encoding="utf-8")
        paths["session_md"].write_text(self._render_session_markdown(report, orders, fills, positions, incidents), encoding="utf-8")
        paths["analytics_md"].write_text(self._render_analytics_markdown(audits), encoding="utf-8")
        self.store.record_session_complete(report)
        return report

    def map_rejection_reason(self, reason: str | None) -> RejectionReasonCode | None:
        if reason is None:
            return None
        return FILTER_REASON_MAP.get(reason, "invalid_signal_payload")

    def _build_rule_checks(
        self,
        *,
        signal,
        trace: TradeAttemptTrace,
        prediction_status: ArtifactStatus,
        market_status: ArtifactStatus,
    ) -> list[RuleCheckRecord]:
        checks = [
            RuleCheckRecord(stage="freshness", name="predictions_fresh", passed=prediction_status.is_ready, detail=prediction_status.reason),
            RuleCheckRecord(stage="freshness", name="market_snapshot_fresh", passed=market_status.is_ready, detail=market_status.reason),
            RuleCheckRecord(stage="strategy", name="duplicate_position_check", passed=not bool(signal.metadata.get("position_exists", False))),
            RuleCheckRecord(stage="strategy", name="cooldown_check", passed=not bool(signal.metadata.get("cooldown_active", False))),
        ]
        if trace.strategy_outcome is not None:
            passed = set(trace.strategy_outcome.passed_filters)
            failed = set(trace.strategy_outcome.failed_filters)
            for filter_name in sorted(passed | failed):
                checks.append(RuleCheckRecord(stage="strategy", name=filter_name, passed=filter_name in passed))
        if trace.risk_outcome is not None:
            for check_name in trace.risk_outcome.checks:
                checks.append(
                    RuleCheckRecord(
                        stage="risk",
                        name=check_name,
                        passed=trace.risk_outcome.approved,
                        detail=trace.risk_outcome.reason,
                    )
                )
        if trace.execution_outcome is not None:
            checks.append(
                RuleCheckRecord(
                    stage="execution",
                    name="execution_result",
                    passed=not trace.execution_outcome.execution_skipped,
                    detail=trace.execution_outcome.reason,
                )
            )
        return checks

    def _append_signal_ledger(self, audit: DecisionAuditRecord) -> None:
        self._append_csv_row(
            self.settings.paths.ledger_dir / "signal_outcomes.csv",
            SignalOutcomeLedgerRow(
                event_id=audit.event_id,
                session_id=audit.session_id,
                run_id=audit.run_id,
                timestamp=audit.timestamp,
                strategy=audit.strategy,
                symbol=audit.symbol,
                signal_source=audit.signal_source,
                final_decision_status=audit.final_decision_status,
                rejection_reason_code=audit.final_rejection_reason_code,
                predicted_return=audit.predicted_return,
                qlib_raw_score=audit.qlib_raw_score,
                candidate_rank=audit.candidate_rank,
            ).model_dump(mode="json"),
        )

    def _append_incident_ledger(self, incident: RuntimeIncidentRecord) -> None:
        self._append_csv_row(
            self.settings.paths.ledger_dir / "incidents.csv",
            incident.model_dump(mode="json"),
        )

    def _paths(self, context: RuntimeSessionContext) -> dict[str, Path]:
        return {
            "audit_json": self.settings.paths.reports_signals_dir / f"{context.session_id}_decision_audit.json",
            "audit_csv": self.settings.paths.reports_signals_dir / f"{context.session_id}_decision_audit.csv",
            "audit_md": self.settings.paths.reports_signals_dir / f"{context.session_id}_decision_audit.md",
            "session_json": self.settings.paths.reports_paper_trading_dir / f"{context.session_id}_paper_session.json",
            "session_md": self.settings.paths.reports_paper_trading_dir / f"{context.session_id}_paper_session.md",
            "analytics_md": self.settings.paths.reports_analytics_dir / f"{context.session_id}_analytics.md",
        }

    @staticmethod
    def _append_csv_row(path: Path, row: dict) -> None:
        path.parent.mkdir(parents=True, exist_ok=True)
        exists = path.exists()
        with path.open("a", encoding="utf-8", newline="") as handle:
            writer = csv.DictWriter(handle, fieldnames=list(row.keys()))
            if not exists:
                writer.writeheader()
            writer.writerow(row)

    @staticmethod
    def _write_csv(path: Path, rows: list[dict]) -> None:
        path.parent.mkdir(parents=True, exist_ok=True)
        fieldnames = list(rows[0].keys()) if rows else ["event_id"]
        with path.open("w", encoding="utf-8", newline="") as handle:
            writer = csv.DictWriter(handle, fieldnames=fieldnames)
            writer.writeheader()
            for row in rows:
                writer.writerow(row)

    @staticmethod
    def _render_audit_markdown(audits: list[DecisionAuditRecord]) -> str:
        lines = [
            "# Decision Audit",
            "",
            f"- candidates audited: `{len(audits)}`",
            "",
            "| Symbol | Source | Status | Rejection | Score | Predicted Return |",
            "| --- | --- | --- | --- | ---: | ---: |",
        ]
        for audit in audits:
            lines.append(
                f"| {audit.symbol} | {audit.signal_source} | {audit.final_decision_status} | "
                f"{audit.final_rejection_reason_code or ''} | {audit.qlib_raw_score or 0:.4f} | "
                f"{audit.predicted_return or 0:.4f} |"
            )
        return "\n".join(lines) + "\n"

    @staticmethod
    def _render_session_markdown(
        report: PaperTradingSessionReport,
        orders: list[BrokerOrder],
        fills: list[FillEvent],
        positions: list[PositionSnapshot],
        incidents: list[RuntimeIncidentRecord],
    ) -> str:
        lines = [
            "# Paper Trading Session",
            "",
            f"- session_id: `{report.session_id}`",
            f"- strategy: `{report.strategy}`",
            f"- mode: `{report.mode.value}`",
            f"- orders: `{len(orders)}`",
            f"- fills: `{len(fills)}`",
            f"- open positions: `{len([position for position in positions if abs(position.quantity) > 0])}`",
            f"- incidents: `{len(incidents)}`",
            f"- no_trade_success: `{report.no_trade_success}`",
            "",
            "## Notes",
            "",
        ]
        lines.extend([f"- {note}" for note in report.notes] or ["- no notes"])
        return "\n".join(lines) + "\n"

    @staticmethod
    def _render_analytics_markdown(audits: list[DecisionAuditRecord]) -> str:
        by_source: dict[str, int] = {}
        for audit in audits:
            by_source[audit.signal_source] = by_source.get(audit.signal_source, 0) + 1
        lines = ["# Analytics Summary", ""]
        for source, count in sorted(by_source.items()):
            lines.append(f"- {source}: `{count}`")
        return "\n".join(lines) + "\n"
