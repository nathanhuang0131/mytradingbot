"""Shared typed models for the trading platform runtime."""

from __future__ import annotations

import logging
from datetime import datetime, timezone
from typing import Any, Literal
from uuid import uuid4

from pydantic import BaseModel, ConfigDict, Field

from mytradingbot.core.enums import RuntimeMode

logger = logging.getLogger(__name__)


def utc_now() -> datetime:
    """Return a timezone-aware UTC timestamp."""

    return datetime.now(timezone.utc)


class ArtifactStatus(BaseModel):
    """Readiness and freshness status for runtime artifacts."""

    name: str
    is_ready: bool
    reason: str | None = None
    guidance: list[str] = Field(default_factory=list)
    as_of: datetime = Field(default_factory=utc_now)
    freshness_minutes: int | None = None

    @classmethod
    def ready(cls, name: str, freshness_minutes: int | None = None) -> "ArtifactStatus":
        return cls(name=name, is_ready=True, freshness_minutes=freshness_minutes)

    @classmethod
    def missing(
        cls, name: str, guidance: list[str] | None = None
    ) -> "ArtifactStatus":
        return cls(
            name=name,
            is_ready=False,
            reason="missing",
            guidance=guidance or [],
        )

    @classmethod
    def stale(
        cls, name: str, freshness_minutes: int, guidance: list[str] | None = None
    ) -> "ArtifactStatus":
        return cls(
            name=name,
            is_ready=False,
            reason="stale",
            freshness_minutes=freshness_minutes,
            guidance=guidance or [],
        )

    @classmethod
    def unavailable(
        cls, name: str, guidance: list[str] | None = None
    ) -> "ArtifactStatus":
        return cls(
            name=name,
            is_ready=False,
            reason="unavailable",
            guidance=guidance or [],
        )


class MarketSnapshot(BaseModel):
    """Market state used by signal and strategy evaluation."""

    symbol: str
    last_price: float
    vwap: float
    spread_bps: float
    volume: float
    liquidity_score: float
    liquidity_stress: float
    order_book_imbalance: float
    liquidity_sweep_detected: bool
    volatility_regime: Literal["low", "normal", "high"]
    timestamp: datetime = Field(default_factory=utc_now)


class QlibPrediction(BaseModel):
    """Prediction payload produced by qlib or imported from qlib artifacts."""

    symbol: str
    score: float
    predicted_return: float
    confidence: float
    rank: int
    direction: Literal["long", "short"]
    generated_at: datetime = Field(default_factory=utc_now)
    horizon: str = "intraday"


class SignalBundle(BaseModel):
    """Signal and market context passed into strategies."""

    symbol: str
    prediction: QlibPrediction
    market: MarketSnapshot
    artifact_status: ArtifactStatus | None = None
    metadata: dict[str, Any] = Field(default_factory=dict)


class ExitPlan(BaseModel):
    """Exit parameters attached to a trade intent."""

    take_profit: float | None = None
    stop_loss: float | None = None
    timeout_seconds: int | None = None
    flatten_near_close: bool = False


class BracketPlan(BaseModel):
    """Typed bracket entry/exit plan used by bracket-aware execution paths."""

    planned_entry_price: float
    planned_stop_loss_price: float
    planned_take_profit_price: float
    planned_quantity: float
    risk_per_share: float
    gross_reward_per_share: float
    estimated_fees: float
    estimated_slippage: float
    estimated_fee_per_share: float
    estimated_slippage_per_share: float
    estimated_fixed_fees: float = 0.0
    net_reward_per_share: float
    reward_risk_ratio: float
    expected_net_profit: float
    time_in_force: str = "day"
    valid_until: datetime | None = None
    exit_reason_metadata: dict[str, str] = Field(default_factory=dict)

    def with_quantity(self, quantity: float) -> "BracketPlan":
        """Return a copy re-scored for a broker-valid quantity."""

        if quantity <= 0:
            return self.model_copy(
                update={
                    "planned_quantity": quantity,
                    "estimated_fees": 0.0,
                    "estimated_slippage": 0.0,
                    "net_reward_per_share": 0.0,
                    "reward_risk_ratio": 0.0,
                    "expected_net_profit": 0.0,
                }
            )

        estimated_fees = self.estimated_fixed_fees + (self.estimated_fee_per_share * quantity)
        estimated_slippage = self.estimated_slippage_per_share * quantity
        gross_reward_total = self.gross_reward_per_share * quantity
        total_risk = self.risk_per_share * quantity
        expected_net_profit = gross_reward_total - estimated_fees - estimated_slippage
        net_reward_per_share = expected_net_profit / quantity
        reward_risk_ratio = (
            expected_net_profit / total_risk if total_risk > 0 else 0.0
        )
        return self.model_copy(
            update={
                "planned_quantity": quantity,
                "estimated_fees": estimated_fees,
                "estimated_slippage": estimated_slippage,
                "net_reward_per_share": net_reward_per_share,
                "reward_risk_ratio": reward_risk_ratio,
                "expected_net_profit": expected_net_profit,
            }
        )


class TradeIntent(BaseModel):
    """Intent generated by a strategy prior to risk approval."""

    model_config = ConfigDict(arbitrary_types_allowed=True)

    symbol: str
    strategy_name: str
    side: Literal["buy", "sell"]
    quantity: float
    limit_price: float | None = None
    predicted_return: float
    confidence: float
    exit_plan: ExitPlan = Field(default_factory=ExitPlan)
    bracket_plan: BracketPlan | None = None
    metadata: dict[str, Any] = Field(default_factory=dict)


class StrategyDecision(BaseModel):
    """Strategy output showing whether a trade should proceed."""

    strategy_name: str
    symbol: str
    should_trade: bool
    intent: TradeIntent | None = None
    reason: str | None = None
    passed_filters: list[str] = Field(default_factory=list)
    failed_filters: list[str] = Field(default_factory=list)

    @classmethod
    def approve(
        cls,
        *,
        strategy_name: str,
        symbol: str,
        intent: TradeIntent,
        passed_filters: list[str],
    ) -> "StrategyDecision":
        return cls(
            strategy_name=strategy_name,
            symbol=symbol,
            should_trade=True,
            intent=intent,
            passed_filters=passed_filters,
        )

    @classmethod
    def reject(
        cls,
        *,
        strategy_name: str,
        symbol: str,
        reason: str,
        failed_filters: list[str],
        passed_filters: list[str] | None = None,
    ) -> "StrategyDecision":
        return cls(
            strategy_name=strategy_name,
            symbol=symbol,
            should_trade=False,
            reason=reason,
            failed_filters=failed_filters,
            passed_filters=passed_filters or [],
        )


class RiskDecision(BaseModel):
    """Risk engine result for a trade intent."""

    approved: bool
    reason: str | None = None
    intent: TradeIntent | None = None
    checks: list[str] = Field(default_factory=list)

    @classmethod
    def approve(cls, intent: TradeIntent, checks: list[str] | None = None) -> "RiskDecision":
        return cls(approved=True, intent=intent, checks=checks or [])

    @classmethod
    def reject(cls, reason: str, checks: list[str] | None = None) -> "RiskDecision":
        return cls(approved=False, reason=reason, checks=checks or [])


class ExecutionRequest(BaseModel):
    """Execution-ready order request after risk approval."""

    symbol: str
    side: Literal["buy", "sell"]
    quantity: float
    strategy_name: str
    mode: RuntimeMode
    limit_price: float | None = None
    bracket_plan: BracketPlan | None = None
    metadata: dict[str, Any] = Field(default_factory=dict)

    @classmethod
    def from_intent(cls, intent: TradeIntent, mode: RuntimeMode) -> "ExecutionRequest":
        return cls(
            symbol=intent.symbol,
            side=intent.side,
            quantity=intent.quantity,
            strategy_name=intent.strategy_name,
            mode=mode,
            limit_price=intent.limit_price,
            bracket_plan=intent.bracket_plan,
            metadata=intent.metadata,
        )


class ExecutionConstraints(BaseModel):
    """Broker-side execution constraints applied before order submission."""

    whole_shares_only_for_brackets: bool = False
    minimum_quantity: float = 1.0


class BrokerOrder(BaseModel):
    """Broker-facing order record."""

    order_id: str = Field(default_factory=lambda: str(uuid4()))
    symbol: str
    side: Literal["buy", "sell"]
    quantity: float
    mode: RuntimeMode
    status: Literal["accepted", "filled", "rejected"] = "accepted"
    submitted_at: datetime = Field(default_factory=utc_now)
    avg_fill_price: float | None = None
    metadata: dict[str, Any] = Field(default_factory=dict)


class FillEvent(BaseModel):
    """Simulated or broker-reported fill."""

    fill_id: str = Field(default_factory=lambda: str(uuid4()))
    order_id: str
    symbol: str
    quantity: float
    price: float
    filled_at: datetime = Field(default_factory=utc_now)
    metadata: dict[str, Any] = Field(default_factory=dict)


class PositionSnapshot(BaseModel):
    """Current broker position state."""

    symbol: str
    quantity: float
    average_price: float
    market_price: float
    unrealized_pnl: float = 0.0


class BrokerBracketState(BaseModel):
    """Managed bracket order state for synthetic paper execution."""

    symbol: str
    entry_order_id: str
    status: Literal["armed", "closed", "cancelled"] = "armed"
    bracket_plan: BracketPlan
    opened_at: datetime = Field(default_factory=utc_now)
    closed_at: datetime | None = None
    exit_reason: str | None = None
    exit_order_id: str | None = None
    realized_pnl: float | None = None


class ExecutionResult(BaseModel):
    """Execution engine outcome after broker routing."""

    execution_skipped: bool = False
    reason: str | None = None
    request: ExecutionRequest | None = None
    order: BrokerOrder | None = None
    fills: list[FillEvent] = Field(default_factory=list)
    position: PositionSnapshot | None = None
    bracket_state: BrokerBracketState | None = None
    realized_pnl: float | None = None

    @classmethod
    def skipped(cls, request: ExecutionRequest, reason: str) -> "ExecutionResult":
        return cls(execution_skipped=True, reason=reason, request=request)


class HealthStatus(BaseModel):
    """High-level system health state shown in diagnostics and the dashboard."""

    summary: str
    ok: bool
    issues: list[str] = Field(default_factory=list)


class NoTradeDiagnostics(BaseModel):
    """Structured explanation for no-trade sessions."""

    summary: str
    reasons: list[str] = Field(default_factory=list)


class AdvisoryResponse(BaseModel):
    """Advisory-only LLM or deterministic summary response."""

    mode: Literal["advisory"] = "advisory"
    summary: str
    details: list[str] = Field(default_factory=list)


class TradeAttemptTrace(BaseModel):
    """Trace record spanning signal, strategy, risk, and execution stages."""

    attempt_id: str = Field(default_factory=lambda: str(uuid4()))
    created_at: datetime = Field(default_factory=utc_now)
    symbol: str
    strategy_name: str
    signal: SignalBundle | None = None
    strategy_outcome: StrategyDecision | None = None
    risk_outcome: RiskDecision | None = None
    execution_request: ExecutionRequest | None = None
    execution_outcome: ExecutionResult | None = None
    notes: list[str] = Field(default_factory=list)

    @classmethod
    def for_symbol(cls, symbol: str, strategy_name: str) -> "TradeAttemptTrace":
        return cls(symbol=symbol, strategy_name=strategy_name)


class SessionSummary(BaseModel):
    """Compact session-level summary."""

    session_id: str = Field(default_factory=lambda: str(uuid4()))
    strategy_name: str
    mode: RuntimeMode
    started_at: datetime = Field(default_factory=utc_now)
    completed_at: datetime | None = None
    status: Literal["completed", "failed"] = "completed"
    trade_count: int = 0
    rejected_trade_count: int = 0


class PostSessionReport(BaseModel):
    """Structured summary for post-session review and export."""

    session_id: str
    strategy_name: str
    mode: RuntimeMode
    trade_count: int
    rejection_reasons: list[str] = Field(default_factory=list)
    notes: list[str] = Field(default_factory=list)


class SessionResult(BaseModel):
    """Top-level result returned by orchestration flows."""

    session_summary: SessionSummary
    prediction_status: ArtifactStatus
    health_status: HealthStatus
    trade_attempts: list[TradeAttemptTrace] = Field(default_factory=list)
    orders: list[BrokerOrder] = Field(default_factory=list)
    fills: list[FillEvent] = Field(default_factory=list)
    positions: list[PositionSnapshot] = Field(default_factory=list)
    rejection_reasons: list[str] = Field(default_factory=list)
    diagnostics: NoTradeDiagnostics | None = None
    post_session_report: PostSessionReport | None = None

    @property
    def traceability(self) -> list[TradeAttemptTrace]:
        return self.trade_attempts
