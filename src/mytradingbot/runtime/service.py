"""Runtime-state coordination, freshness gates, and audit/report writing."""

from __future__ import annotations

import csv
import json
from collections import Counter
from datetime import datetime, timedelta
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
from mytradingbot.reporting.analytics import RealizedAnalyticsExporter
from mytradingbot.signals.microstructure import microstructure_relation_for_direction
from mytradingbot.runtime.models import (
    BrokerMode,
    DecisionPipelineReadiness,
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
    broker_mode_description,
)
from mytradingbot.runtime.store import RuntimeStateStore


FILTER_REASON_MAP: dict[str, RejectionReasonCode] = {
    "qlib_signal_gating": "signal_direction_conflict",
    "predicted_return_threshold": "target_return_below_threshold",
    "confidence_threshold": "score_below_threshold",
    "edge_after_cost_buffer": "edge_after_cost_below_buffer",
    "vwap_relationship": "vwap_relationship_blocked",
    "higher_timeframe_trend_alignment": "higher_timeframe_trend_blocked",
    "microstructure_proxy_alignment": "microstructure_proxy_blocked",
    "spread_filter": "spread_too_wide",
    "liquidity_filter": "liquidity_too_low",
    "liquidity_stress_filter": "liquidity_stress_too_high",
    "intraday_volatility_regime": "volatility_regime_blocked",
    "order_book_imbalance": "imbalance_not_confirmed",
    "pseudo_order_book_pressure_alignment": "imbalance_not_confirmed",
    "liquidity_sweep_detection": "liquidity_sweep_not_confirmed",
    "cooldown_logic": "cooldown_active",
    "duplicate_position": "position_exists",
    "flatten_near_close_logic": "near_close_window_blocked",
    "missing_market_data": "missing_market_data",
    "fee_adjusted_expectancy": "bracket_invalid",
    "invalid_broker_quantity": "bracket_invalid",
    "bracket_plan_invalid_after_rounding": "bracket_invalid",
    "live_mode_disabled": "execution_guard_blocked",
    "position_exists": "position_exists",
    "foreign_position_exists": "position_exists",
    "execution_guard_blocked": "execution_guard_blocked",
    "broker_rejected": "broker_rejected",
    "top_n_selection_cutoff": "top_n_selection_cutoff",
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
        self.analytics_exporter = RealizedAnalyticsExporter(
            settings=self.settings,
            store=self.store,
        )

    def create_session_context(self, *, strategy: str, mode: RuntimeMode) -> RuntimeSessionContext:
        broker_mode = self.resolve_broker_mode(mode=mode)
        context = RuntimeSessionContext(
            started_at=utc_now(),
            strategy=strategy,
            mode=mode,
            broker_mode=broker_mode,
            prediction_artifact_path=str(self.settings.prediction_artifact_path()),
            model_artifact_path=str(self.settings.qlib_model_artifact_path()),
            dataset_artifact_path=str(self.settings.qlib_dataset_artifact_path()),
            market_snapshot_artifact_path=str(self.settings.market_snapshot_artifact_path()),
        )
        self.store.record_session_start(context)
        return context

    def resolve_broker_mode(self, *, mode: RuntimeMode) -> BrokerMode:
        if mode is RuntimeMode.LIVE:
            return "live_guarded"
        configured = self.settings.broker.broker_mode
        if configured in {"local_paper", "alpaca_paper_api"}:
            return configured
        return "local_paper"

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

    def market_snapshot_age_seconds(self, *, market_snapshot_path: Path | None = None) -> int | None:
        path = market_snapshot_path or self.settings.market_snapshot_artifact_path()
        if not path.exists():
            return None
        return max(0, int(utc_now().timestamp() - path.stat().st_mtime))

    def enrich_signal_metadata(self, *, strategy_name: str, signals: list) -> list:
        cooldowns = self.store.active_cooldowns(strategy=strategy_name, now=utc_now())
        open_positions = self.store.active_position_symbols()
        foreign_positions = self.store.foreign_position_symbols()
        for signal in signals:
            signal.metadata["cooldown_active"] = signal.symbol in cooldowns
            signal.metadata["position_exists"] = signal.symbol in open_positions
            signal.metadata["foreign_position_exists"] = signal.symbol in foreign_positions
            signal.metadata["minutes_to_close"] = self.minutes_to_close(signal.market.timestamp)
        return signals

    @staticmethod
    def minutes_to_close(timestamp: datetime, *, reference_time: datetime | None = None) -> int:
        eastern = ZoneInfo("America/New_York")
        localized = timestamp.astimezone(eastern)
        reference = (reference_time or utc_now()).astimezone(eastern)
        if localized.date() != reference.date():
            return 999
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

        if strategy_outcome and (
            strategy_outcome.should_trade
            or strategy_outcome.passed_filters
            or strategy_outcome.quality is not None
        ):
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

        rejection_reasons = self._collect_rejection_reasons(trace)
        vwap_alignment_passed = self._filter_result(trace, "vwap_relationship")
        bracket_expectancy_passed = self._filter_result(trace, "fee_adjusted_expectancy")
        quality = strategy_outcome.quality if strategy_outcome is not None else None
        cost_estimate = quality.cost_estimate if quality is not None else None
        trend = quality.trend if quality is not None else signal.market.higher_timeframe_trend
        microstructure = (
            quality.microstructure
            if quality is not None and quality.microstructure is not None
            else signal.market.microstructure_proxy
        )
        if quality is not None and quality.microstructure_relation is not None:
            microstructure_relation = quality.microstructure_relation
        else:
            _, microstructure_relation = microstructure_relation_for_direction(
                microstructure,
                signal.prediction.direction,
            )
        rejection_code = self.map_rejection_reason(rejection_detail)
        audit = DecisionAuditRecord(
            session_id=context.session_id,
            run_id=context.run_id,
            correlation_id=trace.attempt_id,
            timestamp=signal.market.timestamp,
            strategy=context.strategy,
            strategy_version=context.strategy_version,
            mode=context.mode,
            broker_mode=context.broker_mode,
            symbol=signal.symbol,
            side_considered="buy" if signal.prediction.direction == "long" else "sell",
            bracket_considered=bool(strategy_outcome and strategy_outcome.intent and strategy_outcome.intent.bracket_plan),
            signal_source=signal_source,
            qlib_raw_score=signal.prediction.score,
            confidence=signal.prediction.confidence,
            predicted_return=signal.prediction.predicted_return,
            gross_predicted_return=(
                cost_estimate.gross_predicted_return if cost_estimate is not None else None
            ),
            target_return=signal.prediction.predicted_return,
            spread_bps=signal.market.spread_bps,
            estimated_spread_cost=(
                cost_estimate.estimated_spread_cost if cost_estimate is not None else None
            ),
            estimated_slippage_cost=(
                cost_estimate.estimated_slippage_cost if cost_estimate is not None else None
            ),
            estimated_fee_cost=(
                cost_estimate.estimated_fee_cost if cost_estimate is not None else None
            ),
            estimated_regulatory_fee_cost=(
                cost_estimate.estimated_regulatory_fee_cost
                if cost_estimate is not None
                else None
            ),
            estimated_total_cost=(
                cost_estimate.estimated_total_cost if cost_estimate is not None else None
            ),
            expected_edge_after_cost=(
                cost_estimate.expected_edge_after_cost if cost_estimate is not None else None
            ),
            liquidity_score=signal.market.liquidity_score,
            liquidity_stress=signal.market.liquidity_stress,
            vwap_alignment_passed=vwap_alignment_passed,
            microstructure_state=microstructure.state if microstructure is not None else None,
            microstructure_score=microstructure.score if microstructure is not None else None,
            microstructure_relation=microstructure_relation,
            higher_timeframe_state=trend.state if trend is not None else None,
            higher_timeframe_reason=trend.reason if trend is not None else None,
            higher_timeframe_source_timeframe=(
                trend.source_timeframe if trend is not None else None
            ),
            bracket_expectancy_passed=bracket_expectancy_passed,
            quality_score=quality.quality_score if quality is not None else None,
            candidate_rank=signal.prediction.rank,
            selection_rank=quality.selection_rank if quality is not None else None,
            selected_in_top_n=quality.selected_in_top_n if quality is not None else None,
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
            final_rejection_reason_code=rejection_code,
            final_rejection_reason_detail=self._normalize_rejection_detail(rejection_detail),
            rejection_reasons=rejection_reasons,
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
        cooldown_minutes: int | None = None,
    ) -> None:
        if result.order is not None:
            self.store.record_order(
                OrderLifecycleRecord(
                    order_id=result.order.order_id,
                    session_id=context.session_id,
                    run_id=context.run_id,
                    strategy=strategy_name,
                    mode=context.mode,
                    broker_mode=context.broker_mode,
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
                    broker_mode=context.broker_mode,
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
                resolved_cooldown_minutes = max(
                    0,
                    int(
                        self.settings.scalping.cooldown_minutes
                        if cooldown_minutes is None
                        else cooldown_minutes
                    ),
                )
                if resolved_cooldown_minutes > 0:
                    self.store.set_cooldown(
                        symbol=result.bracket_state.symbol,
                        strategy=strategy_name,
                        expires_at=result.bracket_state.closed_at
                        + timedelta(minutes=resolved_cooldown_minutes),
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
        broker_mode: BrokerMode | None = None,
        ownership_class: str = "bot_owned",
    ) -> RuntimeIncidentRecord:
        resolved_broker_mode = (
            broker_mode
            or (context.broker_mode if context else self.settings.broker.broker_mode)
        )
        incident = RuntimeIncidentRecord(
            session_id=context.session_id if context else None,
            run_id=context.run_id if context else None,
            timestamp=utc_now(),
            broker_mode=resolved_broker_mode,
            ownership_class=ownership_class,  # type: ignore[arg-type]
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
        readiness: DecisionPipelineReadiness | None = None,
        audits: list[DecisionAuditRecord],
        orders: list[BrokerOrder],
        fills: list[FillEvent],
        positions: list[PositionSnapshot],
        incidents: list[RuntimeIncidentRecord],
        notes: list[str],
    ) -> PaperTradingSessionReport:
        paths = self._paths_for_session_id(context.session_id)
        resolved_orders = self._resolve_session_orders(context.session_id, orders)
        resolved_fills = self._resolve_session_fills(context.session_id, fills)
        paths["audit_json"].write_text(
            json.dumps([audit.model_dump(mode="json") for audit in audits], indent=2),
            encoding="utf-8",
        )
        self._write_csv(
            paths["audit_csv"],
            [
                {
                    "event_id": audit.event_id,
                    "timestamp": audit.timestamp.isoformat(),
                    "symbol": audit.symbol,
                    "broker_mode": audit.broker_mode,
                    "signal_source": audit.signal_source,
                    "final_decision_status": audit.final_decision_status,
                    "rejection_reason_code": audit.final_rejection_reason_code,
                    "rejection_reason_detail": audit.final_rejection_reason_detail,
                    "rejection_reasons": "; ".join(audit.rejection_reasons),
                    "confidence": audit.confidence,
                    "predicted_return": audit.predicted_return,
                    "gross_predicted_return": audit.gross_predicted_return,
                    "qlib_raw_score": audit.qlib_raw_score,
                    "spread_bps": audit.spread_bps,
                    "estimated_spread_cost": audit.estimated_spread_cost,
                    "estimated_slippage_cost": audit.estimated_slippage_cost,
                    "estimated_fee_cost": audit.estimated_fee_cost,
                    "estimated_regulatory_fee_cost": audit.estimated_regulatory_fee_cost,
                    "estimated_total_cost": audit.estimated_total_cost,
                    "expected_edge_after_cost": audit.expected_edge_after_cost,
                    "liquidity_score": audit.liquidity_score,
                    "liquidity_stress": audit.liquidity_stress,
                    "vwap_alignment_passed": audit.vwap_alignment_passed,
                    "microstructure_state": audit.microstructure_state,
                    "microstructure_score": audit.microstructure_score,
                    "microstructure_relation": audit.microstructure_relation,
                    "higher_timeframe_state": audit.higher_timeframe_state,
                    "higher_timeframe_reason": audit.higher_timeframe_reason,
                    "bracket_expectancy_passed": audit.bracket_expectancy_passed,
                    "quality_score": audit.quality_score,
                    "candidate_rank": audit.candidate_rank,
                    "selection_rank": audit.selection_rank,
                    "selected_in_top_n": audit.selected_in_top_n,
                }
                for audit in audits
            ],
        )
        self._write_csv(paths["analytics_csv"], self._build_tuning_rows(audits))
        paths["audit_md"].write_text(self._render_audit_markdown(audits), encoding="utf-8")
        analytics_paths = self.materialize_closed_trade_analytics()

        accepted_count = len([audit for audit in audits if audit.final_decision_status.startswith("accepted")])
        rejected_count = len([audit for audit in audits if audit.final_decision_status == "rejected"])
        skipped_count = len([audit for audit in audits if audit.final_decision_status == "skipped"])
        foreign_orders = [
            order
            for order in self.store.list_observed_orders()
            if order.ownership_class in {"foreign", "unknown"}
        ]
        foreign_positions = [
            position
            for position in self.store.list_observed_positions()
            if position.ownership_class in {"foreign", "unknown"}
        ]
        report = PaperTradingSessionReport(
            session_id=context.session_id,
            run_id=context.run_id,
            strategy=context.strategy,
            mode=context.mode,
            broker_mode=context.broker_mode,
            started_at=context.started_at,
            completed_at=utc_now(),
            order_count=len(resolved_orders),
            fill_count=len(resolved_fills),
            accepted_count=accepted_count,
            rejected_count=rejected_count,
            skipped_count=skipped_count,
            no_trade_success=len(resolved_orders) == 0,
            artifact_paths=[
                context.prediction_artifact_path,
                context.model_artifact_path,
                context.dataset_artifact_path,
                context.market_snapshot_artifact_path,
            ],
            report_paths=[
                str(paths[key])
                for key in (
                    "audit_json",
                    "audit_csv",
                    "audit_md",
                    "session_json",
                    "session_md",
                    "analytics_md",
                    "analytics_csv",
                )
            ],
            incident_count=len(incidents),
            foreign_order_count=len(foreign_orders),
            foreign_position_count=len(foreign_positions),
            market_snapshot_ready=(readiness.market_snapshot_ready if readiness is not None else None),
            market_snapshot_age_seconds=(readiness.market_snapshot_age_seconds if readiness is not None else None),
            predictions_ready=(readiness.predictions_ready if readiness is not None else None),
            predictions_age_seconds=(readiness.predictions_age_seconds if readiness is not None else None),
            decision_pipeline_ready=(readiness.decision_pipeline_ready if readiness is not None else None),
            decision_block_reason=(readiness.decision_block_reason if readiness is not None else None),
            notes=notes,
        )
        report.report_paths.extend(analytics_paths)
        paths["session_json"].write_text(report.model_dump_json(indent=2), encoding="utf-8")
        paths["session_md"].write_text(
            self._render_session_markdown(
                report,
                resolved_orders,
                resolved_fills,
                positions,
                incidents,
            ),
            encoding="utf-8",
        )
        paths["analytics_md"].write_text(self._render_analytics_markdown(audits), encoding="utf-8")
        self.store.record_session_complete(report)
        return report

    def refresh_completed_session_artifacts(self) -> list[str]:
        refreshed_session_ids: list[str] = []
        for report in self.store.list_session_reports():
            resolved_orders = self.store.list_orders_for_session(report.session_id)
            resolved_fills = self.store.list_fills_for_session(report.session_id)
            resolved_order_count = len(resolved_orders)
            resolved_fill_count = len(resolved_fills)
            if (
                resolved_order_count == report.order_count
                and resolved_fill_count == report.fill_count
            ):
                continue
            refreshed_session_ids.append(report.session_id)
            report.order_count = resolved_order_count
            report.fill_count = resolved_fill_count
            report.no_trade_success = resolved_order_count == 0
            paths = self._paths_for_session_id(report.session_id)
            paths["session_json"].write_text(report.model_dump_json(indent=2), encoding="utf-8")
            paths["session_md"].write_text(
                self._render_session_markdown(
                    report,
                    resolved_orders,
                    resolved_fills,
                    self.store.list_positions(),
                    [],
                ),
                encoding="utf-8",
            )
            self.store.record_session_complete(report)
        return refreshed_session_ids

    def map_rejection_reason(self, reason: str | None) -> RejectionReasonCode | None:
        if reason is None:
            return None
        if reason.startswith("invalid_signal_payload:"):
            return "invalid_signal_payload"
        if reason.startswith("broker_rejected:"):
            return "broker_rejected"
        return FILTER_REASON_MAP.get(reason, "invalid_signal_payload")

    def materialize_closed_trade_analytics(self) -> list[str]:
        return self.analytics_exporter.write()

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
            RuleCheckRecord(stage="prediction", name="qlib_raw_score", value=signal.prediction.score),
            RuleCheckRecord(stage="prediction", name="confidence", value=signal.prediction.confidence),
            RuleCheckRecord(stage="prediction", name="predicted_return", value=signal.prediction.predicted_return),
            RuleCheckRecord(stage="strategy", name="spread_proxy_bps", value=signal.market.spread_bps),
            RuleCheckRecord(stage="strategy", name="liquidity_score", value=signal.market.liquidity_score),
            RuleCheckRecord(stage="strategy", name="liquidity_stress", value=signal.market.liquidity_stress),
            RuleCheckRecord(
                stage="strategy",
                name="vwap_reference",
                value={
                    "last_price": signal.market.last_price,
                    "vwap": signal.market.vwap,
                    "direction": signal.prediction.direction,
                },
            ),
            RuleCheckRecord(stage="strategy", name="duplicate_position_check", passed=not bool(signal.metadata.get("position_exists", False))),
            RuleCheckRecord(stage="strategy", name="foreign_position_check", passed=not bool(signal.metadata.get("foreign_position_exists", False))),
            RuleCheckRecord(stage="strategy", name="cooldown_check", passed=not bool(signal.metadata.get("cooldown_active", False))),
        ]
        if trace.strategy_outcome is not None:
            if trace.strategy_outcome.quality is not None:
                quality = trace.strategy_outcome.quality
                checks.extend(
                    [
                        RuleCheckRecord(
                            stage="strategy",
                            name="expected_edge_after_cost",
                            value=quality.expected_edge_after_cost,
                        ),
                        RuleCheckRecord(
                            stage="strategy",
                            name="quality_score",
                            value=quality.quality_score,
                        ),
                        RuleCheckRecord(
                            stage="strategy",
                            name="higher_timeframe_state",
                            value=quality.trend.state,
                        ),
                        RuleCheckRecord(
                            stage="strategy",
                            name="microstructure_proxy",
                            value={
                                "state": (
                                    quality.microstructure.state
                                    if quality.microstructure is not None
                                    else None
                                ),
                                "score": (
                                    quality.microstructure.score
                                    if quality.microstructure is not None
                                    else None
                                ),
                                "relation": quality.microstructure_relation,
                                "directional_pressure": (
                                    quality.microstructure.directional_pressure
                                    if quality.microstructure is not None
                                    else None
                                ),
                                "relative_volume": (
                                    quality.microstructure.relative_volume
                                    if quality.microstructure is not None
                                    else None
                                ),
                                "range_expansion": (
                                    quality.microstructure.range_expansion
                                    if quality.microstructure is not None
                                    else None
                                ),
                                "vwap_bias": (
                                    quality.microstructure.vwap_bias
                                    if quality.microstructure is not None
                                    else None
                                ),
                                "wick_bias": (
                                    quality.microstructure.wick_bias
                                    if quality.microstructure is not None
                                    else None
                                ),
                                "persistence": (
                                    quality.microstructure.persistence
                                    if quality.microstructure is not None
                                    else None
                                ),
                            },
                        ),
                        RuleCheckRecord(
                            stage="runtime",
                            name="top_n_selection",
                            passed=quality.selected_in_top_n,
                            detail=(
                                f"selection_rank={quality.selection_rank}"
                                if quality.selection_rank is not None
                                else None
                            ),
                        ),
                    ]
                )
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
        ownership_class = "foreign" if audit.symbol in self.store.foreign_position_symbols() else "bot_owned"
        self._append_csv_row(
            self.settings.paths.ledger_dir / "signal_outcomes.csv",
            SignalOutcomeLedgerRow(
                event_id=audit.event_id,
                session_id=audit.session_id,
                run_id=audit.run_id,
                timestamp=audit.timestamp,
                strategy=audit.strategy,
                broker_mode=audit.broker_mode,
                ownership_class=ownership_class,
                symbol=audit.symbol,
                signal_source=audit.signal_source,
                final_decision_status=audit.final_decision_status,
                rejection_reason_code=audit.final_rejection_reason_code,
                confidence=audit.confidence,
                predicted_return=audit.predicted_return,
                gross_predicted_return=audit.gross_predicted_return,
                qlib_raw_score=audit.qlib_raw_score,
                spread_bps=audit.spread_bps,
                expected_edge_after_cost=audit.expected_edge_after_cost,
                quality_score=audit.quality_score,
                liquidity_score=audit.liquidity_score,
                vwap_alignment_passed=audit.vwap_alignment_passed,
                bracket_expectancy_passed=audit.bracket_expectancy_passed,
                rejection_reasons=audit.rejection_reasons,
                candidate_rank=audit.candidate_rank,
                higher_timeframe_state=audit.higher_timeframe_state,
                selection_rank=audit.selection_rank,
                selected_in_top_n=audit.selected_in_top_n,
            ).model_dump(mode="json"),
        )

    def _append_incident_ledger(self, incident: RuntimeIncidentRecord) -> None:
        self._append_csv_row(
            self.settings.paths.ledger_dir / "incidents.csv",
            incident.model_dump(mode="json"),
        )

    def _paths(self, context: RuntimeSessionContext) -> dict[str, Path]:
        return self._paths_for_session_id(context.session_id)

    def _paths_for_session_id(self, session_id: str) -> dict[str, Path]:
        return {
            "audit_json": self.settings.paths.reports_signals_dir / f"{session_id}_decision_audit.json",
            "audit_csv": self.settings.paths.reports_signals_dir / f"{session_id}_decision_audit.csv",
            "audit_md": self.settings.paths.reports_signals_dir / f"{session_id}_decision_audit.md",
            "session_json": self.settings.paths.reports_paper_trading_dir / f"{session_id}_paper_session.json",
            "session_md": self.settings.paths.reports_paper_trading_dir / f"{session_id}_paper_session.md",
            "analytics_md": self.settings.paths.reports_analytics_dir / f"{session_id}_analytics.md",
            "analytics_csv": self.settings.paths.reports_analytics_dir / f"{session_id}_analytics.csv",
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
        broker_mode = audits[0].broker_mode if audits else "local_paper"
        lines = [
            "# Decision Audit",
            "",
            f"- candidates audited: `{len(audits)}`",
            f"- broker_mode: `{broker_mode}`",
            f"- broker_description: `{broker_mode_description(broker_mode)}`",
            "",
            "| Symbol | Timestamp | Source | Status | Rejection | Score | Confidence | Predicted Return | Edge After Cost | Quality Score | Trend | Microstructure | Spread (bps) | Liquidity | VWAP OK | Expectancy OK | Rejection Reasons |",
            "| --- | --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | --- | --- | ---: | ---: | --- | --- | --- |",
        ]
        for audit in audits:
            edge_after_cost = (
                audit.expected_edge_after_cost
                if audit.expected_edge_after_cost is not None
                else 0.0
            )
            quality_score = audit.quality_score if audit.quality_score is not None else 0.0
            lines.append(
                f"| {audit.symbol} | {audit.timestamp.isoformat()} | {audit.signal_source} | {audit.final_decision_status} | "
                f"{audit.final_rejection_reason_code or ''} | {audit.qlib_raw_score or 0:.4f} | "
                f"{audit.confidence or 0:.4f} | {audit.predicted_return or 0:.4f} | "
                f"{edge_after_cost:.4f} | {quality_score:.4f} | "
                f"{audit.higher_timeframe_state or ''} | "
                f"{(audit.microstructure_relation or '')}:{(audit.microstructure_score or 0):.2f} | "
                f"{audit.spread_bps or 0:.2f} | {audit.liquidity_score or 0:.2f} | "
                f"{audit.vwap_alignment_passed} | {audit.bracket_expectancy_passed} | "
                f"{', '.join(audit.rejection_reasons) if audit.rejection_reasons else ''} |"
            )
        return "\n".join(lines) + "\n"

    def _render_session_markdown(
        self,
        report: PaperTradingSessionReport,
        orders: list[BrokerOrder],
        fills: list[FillEvent],
        positions: list[PositionSnapshot],
        incidents: list[RuntimeIncidentRecord],
    ) -> str:
        external_submission_enabled = self.settings.broker.resolved_external_submission_enabled()
        lines = [
            f"# Paper Trading Session ({broker_mode_description(report.broker_mode).title()})",
            "",
            f"- session_id: `{report.session_id}`",
            f"- strategy: `{report.strategy}`",
            f"- mode: `{report.mode.value}`",
            f"- broker_mode: `{report.broker_mode}`",
            f"- broker_description: `{broker_mode_description(report.broker_mode)}`",
            f"- api_base_url: `{self.settings.broker.alpaca_base_url}`",
            f"- external_broker_submission_enabled: `{str(external_submission_enabled).lower()}`",
            f"- ownership_mode: `{self.settings.broker.ownership_policy}`",
            f"- orders: `{len(orders)}`",
            f"- fills: `{len(fills)}`",
            f"- open positions: `{len([position for position in positions if abs(position.quantity) > 0])}`",
            f"- foreign_open_orders: `{report.foreign_order_count}`",
            f"- foreign_open_positions: `{report.foreign_position_count}`",
            f"- market_snapshot_ready: `{report.market_snapshot_ready}`",
            f"- market_snapshot_age_seconds: `{report.market_snapshot_age_seconds}`",
            f"- predictions_ready: `{report.predictions_ready}`",
            f"- predictions_age_seconds: `{report.predictions_age_seconds}`",
            f"- decision_pipeline_ready: `{report.decision_pipeline_ready}`",
            f"- decision_block_reason: `{report.decision_block_reason}`",
            f"- incidents: `{report.incident_count}`",
            f"- no_trade_success: `{report.no_trade_success}`",
            "",
            "## Notes",
            "",
        ]
        lines.extend([f"- {note}" for note in report.notes] or ["- no notes"])
        return "\n".join(lines) + "\n"

    @staticmethod
    def _render_analytics_markdown(audits: list[DecisionAuditRecord]) -> str:
        by_source: Counter[str] = Counter()
        by_broker_mode: Counter[str] = Counter()
        reject_counts: Counter[str] = Counter()
        approved_symbols: Counter[str] = Counter()
        threshold_blocked: Counter[str] = Counter()
        spread_blocked: Counter[str] = Counter()
        invalid_payload_blocked: Counter[str] = Counter()
        trend_blocked: Counter[str] = Counter()
        microstructure_blocked: Counter[str] = Counter()
        top_ranked_symbols: Counter[str] = Counter()
        negative_edge_symbols: Counter[str] = Counter()
        top_n_approvals = 0
        edge_distribution: Counter[str] = Counter()
        approved_count = 0

        for audit in audits:
            by_source[audit.signal_source] += 1
            by_broker_mode[audit.broker_mode] += 1
            if audit.final_rejection_reason_code is not None:
                reject_counts[audit.final_rejection_reason_code] += 1
            if audit.final_decision_status.startswith("accepted"):
                approved_count += 1
                approved_symbols[audit.symbol] += 1
                if audit.selected_in_top_n:
                    top_n_approvals += 1
            if RuntimeStateService._audit_failed_check(audit, "predicted_return_threshold"):
                threshold_blocked[audit.symbol] += 1
            if RuntimeStateService._audit_failed_check(audit, "spread_filter"):
                spread_blocked[audit.symbol] += 1
            if RuntimeStateService._audit_failed_check(audit, "higher_timeframe_trend_alignment"):
                trend_blocked[audit.symbol] += 1
            if RuntimeStateService._audit_failed_check(audit, "microstructure_proxy_alignment"):
                microstructure_blocked[audit.symbol] += 1
            if audit.final_rejection_reason_code == "invalid_signal_payload":
                invalid_payload_blocked[audit.symbol] += 1
            if audit.selection_rank == 1:
                top_ranked_symbols[audit.symbol] += 1
            if (
                audit.predicted_return is not None
                and audit.predicted_return > 0
                and audit.expected_edge_after_cost is not None
                and audit.expected_edge_after_cost <= 0
            ):
                negative_edge_symbols[audit.symbol] += 1
            edge_distribution[RuntimeStateService._edge_bucket(audit.expected_edge_after_cost)] += 1

        headline_mode = next(iter(sorted(by_broker_mode))) if by_broker_mode else "local_paper"
        lines = [f"# Analytics Summary ({broker_mode_description(headline_mode).title()})", ""]
        lines.append(f"- candidate count: `{len(audits)}`")
        lines.append(f"- approved count: `{approved_count}`")
        lines.append(f"- rejected count: `{len([audit for audit in audits if audit.final_decision_status == 'rejected'])}`")
        lines.append(f"- approvals from top-N selection: `{top_n_approvals}`")
        lines.append("")
        for broker_mode, count in sorted(by_broker_mode.items()):
            lines.append(
                f"- broker_mode={broker_mode}: `{count}` candidates via {broker_mode_description(broker_mode)}"
            )
        for source, count in sorted(by_source.items()):
            lines.append(f"- source={source}: `{count}`")
        lines.append("")
        lines.append("## Reject Counts By Reason")
        lines.extend(RuntimeStateService._format_counter_lines(reject_counts))
        lines.append("")
        lines.append("## Approved Symbols By Frequency")
        lines.extend(RuntimeStateService._format_counter_lines(approved_symbols))
        lines.append("")
        lines.append("## Top Symbols Blocked By Threshold")
        lines.extend(RuntimeStateService._format_counter_lines(threshold_blocked))
        lines.append("")
        lines.append("## Top Symbols Blocked By Spread")
        lines.extend(RuntimeStateService._format_counter_lines(spread_blocked))
        lines.append("")
        lines.append("## Top Symbols Blocked By Invalid Payload")
        lines.extend(RuntimeStateService._format_counter_lines(invalid_payload_blocked))
        lines.append("")
        lines.append("## Symbols Blocked By Trend Alignment")
        lines.extend(RuntimeStateService._format_counter_lines(trend_blocked))
        lines.append("")
        lines.append("## Symbols Blocked By Microstructure Confirmation")
        lines.extend(RuntimeStateService._format_counter_lines(microstructure_blocked))
        lines.append("")
        lines.append("## Highest Ranked Symbols")
        lines.extend(RuntimeStateService._format_counter_lines(top_ranked_symbols))
        lines.append("")
        lines.append("## Positive Return But Negative Edge After Cost")
        lines.extend(RuntimeStateService._format_counter_lines(negative_edge_symbols))
        lines.append("")
        lines.append("## Edge After Cost Distribution")
        lines.extend(RuntimeStateService._format_counter_lines(edge_distribution))
        return "\n".join(lines) + "\n"

    @staticmethod
    def _format_counter_lines(counter: Counter[str]) -> list[str]:
        if not counter:
            return ["- none"]
        return [f"- {key}: `{count}`" for key, count in counter.most_common(10)]

    @staticmethod
    def _audit_failed_check(audit: DecisionAuditRecord, check_name: str) -> bool:
        return any(
            check.name == check_name and check.passed is False
            for check in audit.rule_checks
        )

    def _build_tuning_rows(self, audits: list[DecisionAuditRecord]) -> list[dict[str, object]]:
        reject_counts: Counter[str] = Counter()
        approved_symbols: Counter[str] = Counter()
        threshold_blocked: Counter[str] = Counter()
        spread_blocked: Counter[str] = Counter()
        invalid_payload_blocked: Counter[str] = Counter()
        trend_blocked: Counter[str] = Counter()
        microstructure_blocked: Counter[str] = Counter()
        top_ranked_symbols: Counter[str] = Counter()
        negative_edge_symbols: Counter[str] = Counter()
        edge_distribution: Counter[str] = Counter()
        top_n_approvals = 0

        for audit in audits:
            if audit.final_rejection_reason_code is not None:
                reject_counts[audit.final_rejection_reason_code] += 1
            if audit.final_decision_status.startswith("accepted"):
                approved_symbols[audit.symbol] += 1
                if audit.selected_in_top_n:
                    top_n_approvals += 1
            if self._audit_failed_check(audit, "predicted_return_threshold"):
                threshold_blocked[audit.symbol] += 1
            if self._audit_failed_check(audit, "spread_filter"):
                spread_blocked[audit.symbol] += 1
            if self._audit_failed_check(audit, "higher_timeframe_trend_alignment"):
                trend_blocked[audit.symbol] += 1
            if self._audit_failed_check(audit, "microstructure_proxy_alignment"):
                microstructure_blocked[audit.symbol] += 1
            if audit.final_rejection_reason_code == "invalid_signal_payload":
                invalid_payload_blocked[audit.symbol] += 1
            if audit.selection_rank == 1:
                top_ranked_symbols[audit.symbol] += 1
            if (
                audit.predicted_return is not None
                and audit.predicted_return > 0
                and audit.expected_edge_after_cost is not None
                and audit.expected_edge_after_cost <= 0
            ):
                negative_edge_symbols[audit.symbol] += 1
            edge_distribution[self._edge_bucket(audit.expected_edge_after_cost)] += 1

        rows: list[dict[str, object]] = [
            {"section": "summary", "key": "candidate_count", "count": len(audits)},
            {
                "section": "summary",
                "key": "approved_count",
                "count": len([audit for audit in audits if audit.final_decision_status.startswith("accepted")]),
            },
            {
                "section": "summary",
                "key": "rejected_count",
                "count": len([audit for audit in audits if audit.final_decision_status == "rejected"]),
            },
            {
                "section": "summary",
                "key": "approvals_from_top_n_selection",
                "count": top_n_approvals,
            },
        ]
        rows.extend(self._counter_rows("reject_reason", reject_counts))
        rows.extend(self._counter_rows("approved_symbol", approved_symbols))
        rows.extend(self._counter_rows("blocked_by_threshold", threshold_blocked))
        rows.extend(self._counter_rows("blocked_by_spread", spread_blocked))
        rows.extend(self._counter_rows("blocked_by_invalid_payload", invalid_payload_blocked))
        rows.extend(self._counter_rows("blocked_by_trend_alignment", trend_blocked))
        rows.extend(self._counter_rows("blocked_by_microstructure_confirmation", microstructure_blocked))
        rows.extend(self._counter_rows("highest_ranked_symbol", top_ranked_symbols))
        rows.extend(self._counter_rows("positive_return_negative_edge", negative_edge_symbols))
        rows.extend(self._counter_rows("edge_after_cost_distribution", edge_distribution))
        return rows

    @staticmethod
    def _counter_rows(section: str, counter: Counter[str]) -> list[dict[str, object]]:
        return [
            {"section": section, "key": key, "count": count}
            for key, count in counter.most_common()
        ]

    @staticmethod
    def _edge_bucket(value: float | None) -> str:
        if value is None:
            return "unknown"
        if value <= 0:
            return "<=0"
        if value < 0.001:
            return "0-10bps"
        if value < 0.002:
            return "10-20bps"
        if value < 0.005:
            return "20-50bps"
        return "50bps+"

    def _resolve_session_orders(
        self,
        session_id: str,
        orders: list[BrokerOrder],
    ) -> list[BrokerOrder]:
        persisted = self.store.list_orders_for_session(session_id)
        return persisted or orders

    def _resolve_session_fills(
        self,
        session_id: str,
        fills: list[FillEvent],
    ) -> list[FillEvent]:
        persisted = self.store.list_fills_for_session(session_id)
        return persisted or fills

    @staticmethod
    def _normalize_rejection_detail(reason: str | None) -> str | None:
        if reason is None:
            return None
        if ":" in reason:
            return reason.split(":", 1)[1]
        return reason

    @staticmethod
    def _collect_rejection_reasons(trace: TradeAttemptTrace) -> list[str]:
        reasons: list[str] = []
        if trace.strategy_outcome is not None:
            reasons.extend(trace.strategy_outcome.failed_filters)
            if trace.strategy_outcome.reason and trace.strategy_outcome.reason not in reasons:
                reasons.append(trace.strategy_outcome.reason)
        if trace.risk_outcome is not None and trace.risk_outcome.reason:
            reasons.append(trace.risk_outcome.reason)
        if trace.execution_outcome is not None and trace.execution_outcome.reason:
            reasons.append(trace.execution_outcome.reason)
        deduped: list[str] = []
        for reason in reasons:
            normalized = RuntimeStateService._normalize_rejection_detail(reason) or reason
            if normalized not in deduped:
                deduped.append(normalized)
        return deduped

    @staticmethod
    def _filter_result(trace: TradeAttemptTrace, filter_name: str) -> bool | None:
        strategy_outcome = trace.strategy_outcome
        if strategy_outcome is None:
            return None
        if filter_name in strategy_outcome.passed_filters:
            return True
        if filter_name in strategy_outcome.failed_filters:
            return False
        return None
