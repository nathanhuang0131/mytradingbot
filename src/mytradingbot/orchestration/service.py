"""Platform orchestration for paper and dry-run sessions."""

from __future__ import annotations

import logging

from mytradingbot.brokers.paper import PaperBroker
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
from mytradingbot.data.service import MarketDataService
from mytradingbot.execution.service import ExecutionEngine
from mytradingbot.qlib_engine.service import QlibWorkflowService
from mytradingbot.risk.service import RiskEngine
from mytradingbot.strategies.registry import StrategyRegistry

logger = logging.getLogger(__name__)


class TradingPlatformService:
    """Coordinate the end-to-end trading workflow."""

    def __init__(
        self,
        settings: AppSettings | None = None,
        *,
        qlib_service: QlibWorkflowService | None = None,
        market_data_service: MarketDataService | None = None,
        strategy_registry: StrategyRegistry | None = None,
        risk_engine: RiskEngine | None = None,
        execution_engine: ExecutionEngine | None = None,
        broker: PaperBroker | None = None,
    ) -> None:
        self.settings = settings or AppSettings()
        self.qlib_service = qlib_service or QlibWorkflowService(settings=self.settings)
        self.market_data_service = market_data_service or MarketDataService(
            settings=self.settings
        )
        self.strategy_registry = strategy_registry or StrategyRegistry.build_default()
        self.risk_engine = risk_engine or RiskEngine()
        self.broker = broker or PaperBroker()
        self.execution_engine = execution_engine or ExecutionEngine(broker=self.broker)
        self.last_session_result: SessionResult | None = None

    @classmethod
    def bootstrap_default(cls) -> "TradingPlatformService":
        return cls()

    def get_strategy_names(self) -> list[str]:
        return self.strategy_registry.names()

    def get_prediction_status(self) -> ArtifactStatus:
        return self.qlib_service.get_runtime_prediction_status()

    def get_health_status(self) -> HealthStatus:
        prediction_status = self.get_prediction_status()
        if prediction_status.is_ready:
            return HealthStatus(summary="Platform ready for dry-run or paper sessions.", ok=True)
        reason = prediction_status.reason or "unknown"
        return HealthStatus(
            summary=f"Prediction artifact is {reason}.",
            ok=False,
            issues=prediction_status.guidance,
        )

    def refresh_predictions(self):
        return self.qlib_service.refresh_predictions()

    def train_models(self):
        return self.qlib_service.train_models()

    def build_dataset(self):
        return self.qlib_service.build_dataset()

    def run_session(
        self,
        *,
        strategy_name: str,
        mode: RuntimeMode | str,
    ) -> SessionResult:
        normalized_mode = mode if isinstance(mode, RuntimeMode) else RuntimeMode(mode)
        summary = SessionSummary(strategy_name=strategy_name, mode=normalized_mode)

        prediction_result = self.qlib_service.load_predictions()
        if not prediction_result.ok:
            summary.status = "failed"
            summary.completed_at = utc_now()
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
            self.last_session_result = result
            return result

        try:
            signals = self.market_data_service.build_signal_bundles(
                prediction_result.predictions
            )
        except (FileNotFoundError, KeyError, ValueError) as exc:
            summary.status = "failed"
            summary.completed_at = utc_now()
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
            self.last_session_result = result
            return result

        strategy = self.strategy_registry.get(strategy_name)
        attempts: list[TradeAttemptTrace] = []
        rejection_reasons: list[str] = []

        for signal in signals:
            trace = TradeAttemptTrace.for_symbol(signal.symbol, strategy_name)
            trace.signal = signal

            strategy_decision = strategy.evaluate(signal)
            trace.strategy_outcome = strategy_decision
            if not strategy_decision.should_trade or strategy_decision.intent is None:
                rejection_reasons.append(strategy_decision.reason or "strategy_rejected")
                attempts.append(trace)
                continue

            risk_decision = self.risk_engine.evaluate(
                intent=strategy_decision.intent,
                mode=normalized_mode if normalized_mode is not RuntimeMode.DRY_RUN else RuntimeMode.PAPER,
            )
            trace.risk_outcome = risk_decision
            if not risk_decision.approved:
                rejection_reasons.append(risk_decision.reason or "risk_rejected")
                attempts.append(trace)
                continue

            execution_result = self.execution_engine.execute(
                risk_decision,
                mode=normalized_mode,
            )
            trace.execution_request = execution_result.request
            trace.execution_outcome = execution_result
            if execution_result.reason and execution_result.execution_skipped:
                rejection_reasons.append(execution_result.reason)
            attempts.append(trace)

        orders = [] if normalized_mode is RuntimeMode.DRY_RUN else self.broker.list_orders()
        fills = [] if normalized_mode is RuntimeMode.DRY_RUN else self.broker.list_fills()
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
        self.last_session_result = result
        return result
