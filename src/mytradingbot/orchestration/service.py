"""Platform orchestration for paper and dry-run sessions."""

from __future__ import annotations

import logging
from datetime import datetime
from pathlib import Path

from mytradingbot.brokers.alpaca_paper import AlpacaPaperBroker
from mytradingbot.brokers.base import BaseBroker
from mytradingbot.brokers.paper import PaperBroker
from mytradingbot.core.capabilities import CapabilityService, CapabilitySnapshot
from mytradingbot.core.enums import RuntimeMode
from mytradingbot.core.models import (
    ArtifactStatus,
    HealthStatus,
    SessionResult,
    SessionSummary,
    TradeAttemptTrace,
    utc_now,
)
from mytradingbot.core.settings import AppSettings
from mytradingbot.data.pipeline import MarketDataPipeline
from mytradingbot.data.service import MarketDataService
from mytradingbot.diagnostics.service import DiagnosticsService
from mytradingbot.execution.service import ExecutionEngine
from mytradingbot.qlib_engine.service import QlibWorkflowService
from mytradingbot.risk.service import RiskEngine
from mytradingbot.reporting.service import ReportingService
from mytradingbot.runtime.models import BrokerMode, BrokerReconciliationSnapshot
from mytradingbot.runtime.service import RuntimeStateService
from mytradingbot.strategies.registry import StrategyRegistry
from mytradingbot.universe.storage import UniverseStorage

logger = logging.getLogger(__name__)


class TradingPlatformService:
    """Coordinate the end-to-end trading workflow."""

    def __init__(
        self,
        settings: AppSettings | None = None,
        *,
        qlib_service: QlibWorkflowService | None = None,
        data_pipeline: MarketDataPipeline | None = None,
        market_data_service: MarketDataService | None = None,
        strategy_registry: StrategyRegistry | None = None,
        risk_engine: RiskEngine | None = None,
        execution_engine: ExecutionEngine | None = None,
        runtime_state_service: RuntimeStateService | None = None,
        reporting_service: ReportingService | None = None,
        diagnostics_service: DiagnosticsService | None = None,
        broker: BaseBroker | None = None,
        broker_mode: BrokerMode | None = None,
    ) -> None:
        self.settings = settings or AppSettings()
        if broker_mode is not None:
            self.settings.broker.broker_mode = broker_mode
        self.qlib_service = qlib_service or QlibWorkflowService(settings=self.settings)
        self.data_pipeline = data_pipeline or MarketDataPipeline(settings=self.settings)
        self.market_data_service = market_data_service or MarketDataService(
            settings=self.settings
        )
        self.capability_service = CapabilityService(settings=self.settings)
        self.strategy_registry = strategy_registry or StrategyRegistry.build_default()
        self.risk_engine = risk_engine or RiskEngine()
        self.runtime_state_service = runtime_state_service or RuntimeStateService(
            settings=self.settings
        )
        self.broker = broker or self._build_broker()
        self.execution_engine = execution_engine or ExecutionEngine(broker=self.broker)
        self.universe_storage = UniverseStorage(settings=self.settings)
        self.reporting_service = reporting_service or ReportingService()
        self.diagnostics_service = diagnostics_service or DiagnosticsService()
        self.last_session_result: SessionResult | None = None

    @classmethod
    def bootstrap_default(cls) -> "TradingPlatformService":
        return cls()

    def _build_broker(self) -> BaseBroker:
        if self.settings.broker.broker_mode == "alpaca_paper_api":
            return AlpacaPaperBroker(
                settings=self.settings,
                runtime_store=self.runtime_state_service.store,
            )
        return PaperBroker(runtime_store=self.runtime_state_service.store)

    def get_strategy_names(self) -> list[str]:
        return self.strategy_registry.names()

    def get_capabilities(self) -> CapabilitySnapshot:
        return self.capability_service.detect()

    def get_prediction_status(self) -> ArtifactStatus:
        return self.qlib_service.get_runtime_prediction_status()

    def get_health_status(self) -> HealthStatus:
        prediction_status = self.get_prediction_status()
        capabilities = self.get_capabilities()
        if prediction_status.is_ready:
            return HealthStatus(
                summary="Platform ready for dry-run or paper sessions.",
                ok=True,
                issues=[],
            )
        reason = prediction_status.reason or "unknown"
        return HealthStatus(
            summary=f"Prediction artifact is {reason}.",
            ok=False,
            issues=[
                *prediction_status.guidance,
                f"{capabilities.phase_2.name}: {capabilities.phase_2.status}",
                f"{capabilities.phase_3.name}: {capabilities.phase_3.status}",
            ],
        )

    def download_market_data(
        self,
        *,
        symbols: list[str] | None = None,
        symbols_file: Path | None = None,
        timeframes: list[str] | None = None,
        start_at: datetime | None = None,
        end_at: datetime | None = None,
        full_refresh: bool = False,
        normalize_only: bool = False,
    ):
        resolved_symbols = self.resolve_symbols(symbols=symbols, symbols_file=symbols_file)
        return self.data_pipeline.download_update_normalize_and_snapshot(
            symbols=resolved_symbols,
            timeframes=timeframes,
            start_at=start_at,
            end_at=end_at,
            full_refresh=full_refresh,
            normalize_only=normalize_only,
        )

    def refresh_predictions(self, *, strategy_name: str | None = None):
        return self.qlib_service.refresh_predictions(strategy_name=strategy_name)

    def train_models(self, *, strategy_name: str | None = None):
        return self.qlib_service.train_models(strategy_name=strategy_name)

    def build_dataset(
        self,
        *,
        strategy_name: str | None = None,
        symbols: list[str] | None = None,
        symbols_file: Path | None = None,
    ):
        resolved_symbols = self.resolve_symbols(symbols=symbols, symbols_file=symbols_file)
        return self.qlib_service.build_dataset(
            strategy_name=strategy_name,
            symbols=resolved_symbols,
        )

    def resolve_symbols(
        self,
        *,
        symbols: list[str] | None = None,
        symbols_file: Path | None = None,
    ) -> list[str] | None:
        if symbols:
            return sorted({symbol.strip().upper() for symbol in symbols if symbol and symbol.strip()})
        if symbols_file is None:
            return None
        return self.universe_storage.load_symbols(symbols_file)

    def _apply_reconciliation_notes(
        self,
        *,
        context,
        reconciliation: BrokerReconciliationSnapshot,
        incidents: list,
        session_notes: list[str],
    ) -> None:
        session_notes.extend(
            [
                f"bot_owned_open_orders={reconciliation.bot_owned_order_count}",
                f"bot_owned_open_positions={reconciliation.bot_owned_position_count}",
                f"foreign_open_orders={reconciliation.foreign_order_count}",
                f"foreign_open_positions={reconciliation.foreign_position_count}",
            ]
        )
        session_notes.extend(reconciliation.notes)
        if reconciliation.foreign_order_count or reconciliation.foreign_position_count:
            incidents.append(
                self.runtime_state_service.build_incident(
                    context=context,
                    code="foreign_broker_exposure_observed",
                    summary="Observed foreign or unknown Alpaca paper account exposure.",
                    detail=(
                        f"foreign_orders={reconciliation.foreign_order_count}, "
                        f"foreign_positions={reconciliation.foreign_position_count}"
                    ),
                    severity="info",
                    ownership_class="foreign",
                    metadata={
                        "foreign_order_count": reconciliation.foreign_order_count,
                        "foreign_position_count": reconciliation.foreign_position_count,
                        "ownership_policy": reconciliation.ownership_policy,
                    },
                )
            )

    def run_session(
        self,
        *,
        strategy_name: str,
        mode: RuntimeMode | str,
    ) -> SessionResult:
        normalized_mode = mode if isinstance(mode, RuntimeMode) else RuntimeMode(mode)
        context = self.runtime_state_service.create_session_context(
            strategy=strategy_name,
            mode=normalized_mode,
        )
        summary = SessionSummary(
            session_id=context.session_id,
            strategy_name=strategy_name,
            mode=normalized_mode,
        )
        incidents = []
        session_notes = [
            f"broker_mode={context.broker_mode}",
            f"api_base_url={self.settings.broker.alpaca_base_url}",
            "external_broker_submission_enabled="
            f"{str(self.settings.broker.resolved_external_submission_enabled()).lower()}",
            f"ownership_mode={self.settings.broker.ownership_policy}",
        ]

        preflight = self.broker.preflight()
        if not preflight.ok:
            summary.status = "failed"
            summary.completed_at = utc_now()
            incidents.append(
                self.runtime_state_service.build_incident(
                    context=context,
                    code="broker_rejected",
                    summary="Broker preflight failed before session execution.",
                    detail=preflight.message,
                    severity="error",
                    metadata=preflight.metadata,
                )
            )
            result = SessionResult(
                session_summary=summary,
                prediction_status=ArtifactStatus.unavailable("predictions"),
                health_status=HealthStatus(
                    summary="Broker preflight failed.",
                    ok=False,
                    issues=[preflight.message],
                ),
                rejection_reasons=[preflight.message],
            )
            result.post_session_report = self.reporting_service.build_post_session_review(result)
            self.runtime_state_service.write_session_artifacts(
                context=context,
                audits=[],
                orders=[],
                fills=[],
                positions=[],
                incidents=incidents,
                notes=[*session_notes, *result.post_session_report.notes],
            )
            self.last_session_result = result
            return result

        try:
            reconciliation = self.broker.reconcile_runtime_state(strategy_name=strategy_name)
        except Exception as exc:
            summary.status = "failed"
            summary.completed_at = utc_now()
            incidents.append(
                self.runtime_state_service.build_incident(
                    context=context,
                    code="broker_state_unreconciled",
                    summary="Broker state reconciliation failed before session execution.",
                    detail=str(exc),
                    severity="error",
                )
            )
            result = SessionResult(
                session_summary=summary,
                prediction_status=ArtifactStatus.unavailable("predictions"),
                health_status=HealthStatus(
                    summary="Broker reconciliation failed.",
                    ok=False,
                    issues=[str(exc)],
                ),
                rejection_reasons=["broker_state_unreconciled"],
            )
            result.post_session_report = self.reporting_service.build_post_session_review(result)
            self.runtime_state_service.write_session_artifacts(
                context=context,
                audits=[],
                orders=[],
                fills=[],
                positions=self.broker.list_positions(),
                incidents=incidents,
                notes=[*session_notes, *result.post_session_report.notes],
            )
            self.last_session_result = result
            return result

        self._apply_reconciliation_notes(
            context=context,
            reconciliation=reconciliation,
            incidents=incidents,
            session_notes=session_notes,
        )

        prediction_result = self.qlib_service.load_predictions()
        market_status = self.runtime_state_service.market_snapshot_status(
            market_snapshot_path=self.market_data_service.market_snapshot_path
        )
        if self.runtime_state_service.has_circuit_breaker_block():
            summary.status = "failed"
            summary.completed_at = utc_now()
            incidents.append(
                self.runtime_state_service.build_incident(
                    context=context,
                    code="execution_guard_blocked",
                    summary="Circuit breaker is active; new entries are halted.",
                    severity="critical",
                )
            )
            result = SessionResult(
                session_summary=summary,
                prediction_status=prediction_result.status,
                health_status=HealthStatus(
                    summary="Runtime circuit breaker halted the session.",
                    ok=False,
                    issues=["execution_guard_blocked"],
                ),
                rejection_reasons=["execution_guard_blocked"],
            )
            result.post_session_report = self.reporting_service.build_post_session_review(result)
            self.runtime_state_service.write_session_artifacts(
                context=context,
                audits=[],
                orders=[],
                fills=[],
                positions=[],
                incidents=incidents,
                notes=[*session_notes, *result.post_session_report.notes],
            )
            self.last_session_result = result
            return result

        if not market_status.is_ready:
            summary.status = "failed"
            summary.completed_at = utc_now()
            incidents.append(
                self.runtime_state_service.build_incident(
                    context=context,
                    code="stale_market_snapshot" if market_status.reason == "stale" else "missing_market_data",
                    summary="Market snapshot artifact is unavailable for trading.",
                    detail=market_status.reason,
                    severity="error",
                )
            )
            result = SessionResult(
                session_summary=summary,
                prediction_status=prediction_result.status,
                health_status=HealthStatus(
                    summary="Market snapshot unavailable.",
                    ok=False,
                    issues=market_status.guidance,
                ),
                rejection_reasons=[market_status.reason or "market_snapshot_unavailable"],
            )
            result.post_session_report = self.reporting_service.build_post_session_review(result)
            self.runtime_state_service.write_session_artifacts(
                context=context,
                audits=[],
                orders=[],
                fills=[],
                positions=[],
                incidents=incidents,
                notes=[*session_notes, *result.post_session_report.notes],
            )
            self.last_session_result = result
            return result

        if not prediction_result.ok:
            summary.status = "failed"
            summary.completed_at = utc_now()
            incidents.append(
                self.runtime_state_service.build_incident(
                    context=context,
                    code="stale_predictions" if prediction_result.status.reason == "stale" else "no_candidate_from_predictions",
                    summary="Prediction artifact unavailable for trading.",
                    detail=prediction_result.message,
                    severity="error",
                )
            )
            result = SessionResult(
                session_summary=summary,
                prediction_status=prediction_result.status,
                health_status=HealthStatus(
                    summary="Prediction artifact unavailable.",
                    ok=False,
                    issues=[prediction_result.message],
                ),
                rejection_reasons=[prediction_result.message],
            )
            result.post_session_report = self.reporting_service.build_post_session_review(result)
            self.runtime_state_service.write_session_artifacts(
                context=context,
                audits=[],
                orders=[],
                fills=[],
                positions=[],
                incidents=incidents,
                notes=[*session_notes, *result.post_session_report.notes],
            )
            self.last_session_result = result
            return result

        try:
            signals = self.market_data_service.build_signal_bundles(
                prediction_result.predictions
            )
        except (FileNotFoundError, KeyError, ValueError) as exc:
            summary.status = "failed"
            summary.completed_at = utc_now()
            incidents.append(
                self.runtime_state_service.build_incident(
                    context=context,
                    code="missing_market_data",
                    summary="Market data unavailable.",
                    detail=str(exc),
                    severity="error",
                )
            )
            result = SessionResult(
                session_summary=summary,
                prediction_status=prediction_result.status,
                health_status=HealthStatus(
                    summary="Market data unavailable.",
                    ok=False,
                    issues=[str(exc)],
                ),
                rejection_reasons=[str(exc)],
            )
            result.post_session_report = self.reporting_service.build_post_session_review(result)
            self.runtime_state_service.write_session_artifacts(
                context=context,
                audits=[],
                orders=[],
                fills=[],
                positions=[],
                incidents=incidents,
                notes=[*session_notes, *result.post_session_report.notes],
            )
            self.last_session_result = result
            return result

        exit_results = []
        session_orders = []
        session_fills = []
        for signal in signals:
            for exit_result in self.broker.process_market_snapshot(signal.market):
                self.runtime_state_service.record_execution_result(
                    context=context,
                    strategy_name=strategy_name,
                    result=exit_result,
                )
                exit_results.append(exit_result)
                if exit_result.order is not None:
                    session_orders.append(exit_result.order)
                session_fills.extend(exit_result.fills)

        if signals and any(
            self.runtime_state_service.minutes_to_close(signal.market.timestamp)
            <= self.settings.scalping.max_holding_seconds // 60
            for signal in signals
        ):
            for flatten_result in self.broker.flatten_open_brackets(reason="near_close_flatten"):
                self.runtime_state_service.record_execution_result(
                    context=context,
                    strategy_name=strategy_name,
                    result=flatten_result,
                )
                exit_results.append(flatten_result)
                if flatten_result.order is not None:
                    session_orders.append(flatten_result.order)
                session_fills.extend(flatten_result.fills)

        signals = self.runtime_state_service.enrich_signal_metadata(
            strategy_name=strategy_name,
            signals=signals,
        )
        strategy = self.strategy_registry.get(strategy_name)
        attempts: list[TradeAttemptTrace] = []
        audits = []
        rejection_reasons: list[str] = []

        for signal in signals:
            trace = TradeAttemptTrace.for_symbol(signal.symbol, strategy_name)
            trace.signal = signal
            try:
                strategy_decision = strategy.evaluate(signal)
                trace.strategy_outcome = strategy_decision
                if not strategy_decision.should_trade or strategy_decision.intent is None:
                    rejection_reasons.append(strategy_decision.reason or "strategy_rejected")
                    attempts.append(trace)
                    audits.append(
                        self.runtime_state_service.build_decision_audit(
                            context=context,
                            signal=signal,
                            trace=trace,
                            prediction_status=prediction_result.status,
                            market_status=market_status,
                        )
                    )
                    continue
                strategy_decision.intent.metadata["client_order_id"] = (
                    self.runtime_state_service.deterministic_client_order_id(
                        strategy_name=strategy_name,
                        signal=signal,
                        side=strategy_decision.intent.side,
                    )
                )
                strategy_decision.intent.metadata["signal_source"] = "qlib_plus_rules"
                strategy_decision.intent.metadata["broker_mode"] = context.broker_mode
                strategy_decision.intent.metadata["session_id"] = context.session_id
                strategy_decision.intent.metadata["run_id"] = context.run_id
                strategy_decision.intent.metadata["ownership_policy"] = self.settings.broker.ownership_policy
                strategy_decision.intent.metadata["position_exists"] = signal.metadata.get(
                    "position_exists",
                    False,
                )
                strategy_decision.intent.metadata["foreign_position_exists"] = signal.metadata.get(
                    "foreign_position_exists",
                    False,
                )
                strategy_decision.intent.metadata["circuit_breaker_blocked"] = (
                    self.runtime_state_service.has_circuit_breaker_block()
                    or self.runtime_state_service.store.has_client_order_id(
                        strategy_decision.intent.metadata["client_order_id"]
                    )
                )
                if strategy_decision.intent.bracket_plan is not None:
                    plan = strategy_decision.intent.bracket_plan
                    trace.notes.append(
                        "Bracket plan: "
                        f"entry={plan.planned_entry_price:.4f}, "
                        f"stop={plan.planned_stop_loss_price:.4f}, "
                        f"target={plan.planned_take_profit_price:.4f}, "
                        f"fees={plan.estimated_fees:.4f}, "
                        f"slippage={plan.estimated_slippage:.4f}, "
                        f"net_rr={plan.reward_risk_ratio:.4f}"
                    )

                risk_decision = self.risk_engine.evaluate(
                    intent=strategy_decision.intent,
                    mode=normalized_mode if normalized_mode is not RuntimeMode.DRY_RUN else RuntimeMode.PAPER,
                )
                trace.risk_outcome = risk_decision
                if not risk_decision.approved:
                    rejection_reasons.append(risk_decision.reason or "risk_rejected")
                    attempts.append(trace)
                    audits.append(
                        self.runtime_state_service.build_decision_audit(
                            context=context,
                            signal=signal,
                            trace=trace,
                            prediction_status=prediction_result.status,
                            market_status=market_status,
                        )
                    )
                    continue

                execution_result = self.execution_engine.execute(
                    risk_decision,
                    mode=normalized_mode,
                )
                trace.execution_request = execution_result.request
                trace.execution_outcome = execution_result
                if execution_result.reason and execution_result.execution_skipped:
                    rejection_reasons.append(execution_result.reason)
                if execution_result.bracket_state is not None:
                    trace.notes.append(
                        "Bracket state: "
                        f"status={execution_result.bracket_state.status}, "
                        f"exit_reason={execution_result.bracket_state.exit_reason}, "
                        f"realized_pnl={execution_result.bracket_state.realized_pnl}"
                    )
                self.runtime_state_service.record_execution_result(
                    context=context,
                    strategy_name=strategy_name,
                    result=execution_result,
                )
                if execution_result.order is not None:
                    session_orders.append(execution_result.order)
                session_fills.extend(execution_result.fills)
                attempts.append(trace)
                audits.append(
                    self.runtime_state_service.build_decision_audit(
                        context=context,
                        signal=signal,
                        trace=trace,
                        prediction_status=prediction_result.status,
                        market_status=market_status,
                    )
                )
            except Exception as exc:  # pragma: no cover - defensive session isolation
                trace.notes.append(str(exc))
                attempts.append(trace)
                rejection_reasons.append("strategy_exception")
                incidents.append(
                    self.runtime_state_service.build_incident(
                        context=context,
                        code="strategy_exception",
                        summary=f"Per-symbol exception for {signal.symbol}.",
                        detail=str(exc),
                        severity="error",
                    )
                )
                audits.append(
                    self.runtime_state_service.build_decision_audit(
                        context=context,
                        signal=signal,
                        trace=trace,
                        prediction_status=prediction_result.status,
                        market_status=market_status,
                    )
                )

        orders = [] if normalized_mode is RuntimeMode.DRY_RUN else session_orders
        fills = [] if normalized_mode is RuntimeMode.DRY_RUN else session_fills
        positions = [] if normalized_mode is RuntimeMode.DRY_RUN else self.broker.list_positions()

        summary.trade_count = len(orders)
        summary.rejected_trade_count = len(
            [attempt for attempt in attempts if attempt.execution_outcome is None or attempt.execution_outcome.order is None]
        )
        summary.completed_at = utc_now()

        result = SessionResult(
            session_summary=summary,
            prediction_status=prediction_result.status,
            health_status=HealthStatus(
                summary="Session completed.",
                ok=True,
                issues=[],
            ),
            trade_attempts=attempts,
            orders=orders,
            fills=fills,
            positions=positions,
            rejection_reasons=rejection_reasons,
        )
        if summary.trade_count == 0 and summary.status == "completed":
            result.diagnostics = self.diagnostics_service.build_no_trade_report(result)
        result.post_session_report = self.reporting_service.build_post_session_review(result)
        self.runtime_state_service.write_session_artifacts(
            context=context,
            audits=audits,
            orders=orders,
            fills=fills,
            positions=positions,
            incidents=incidents,
            notes=[
                *session_notes,
                *result.post_session_report.notes,
                *[
                    f"managed_exit={execution.reason}"
                    for execution in exit_results
                    if execution.reason
                ],
            ],
        )
        self.last_session_result = result
        return result
