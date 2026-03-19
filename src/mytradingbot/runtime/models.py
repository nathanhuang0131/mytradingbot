"""Typed runtime-state, audit, and incident models."""

from __future__ import annotations

from datetime import datetime
from typing import Any, Literal
from uuid import uuid4

from pydantic import BaseModel, Field

from mytradingbot.core.enums import RuntimeMode

SignalSource = Literal[
    "qlib_candidate_only",
    "rules_validated_only",
    "qlib_plus_rules",
    "no_valid_signal",
]

DecisionStatus = Literal[
    "accepted_buy",
    "accepted_bracket_buy",
    "accepted_short",
    "accepted_bracket_short",
    "rejected",
    "skipped",
    "no_action",
]

RejectionReasonCode = Literal[
    "score_below_threshold",
    "target_return_below_threshold",
    "spread_too_wide",
    "liquidity_too_low",
    "volatility_regime_blocked",
    "imbalance_not_confirmed",
    "liquidity_sweep_not_confirmed",
    "risk_budget_exceeded",
    "position_exists",
    "cooldown_active",
    "bracket_invalid",
    "broker_rejected",
    "missing_market_data",
    "invalid_signal_payload",
    "execution_guard_blocked",
    "no_candidate_from_predictions",
    "stale_predictions",
    "stale_market_snapshot",
    "runtime_state_unavailable",
    "strategy_exception",
    "broker_state_unreconciled",
]


class RuntimeSessionContext(BaseModel):
    """Stable identifiers and artifact references for a session run."""

    session_id: str = Field(default_factory=lambda: str(uuid4()))
    run_id: str = Field(default_factory=lambda: str(uuid4()))
    started_at: datetime
    strategy: str
    strategy_version: str = "v2"
    mode: RuntimeMode
    prediction_artifact_path: str
    model_artifact_path: str
    dataset_artifact_path: str
    market_snapshot_artifact_path: str


class RuleCheckRecord(BaseModel):
    """Single rule/check outcome recorded in the audit trail."""

    stage: Literal["prediction", "strategy", "risk", "execution", "freshness", "runtime"]
    name: str
    passed: bool | None = None
    detail: str | None = None
    value: Any | None = None


class DecisionAuditRecord(BaseModel):
    """Analytics-ready record for a candidate decision path."""

    event_id: str = Field(default_factory=lambda: str(uuid4()))
    session_id: str
    run_id: str
    correlation_id: str
    timestamp: datetime
    strategy: str
    strategy_version: str
    mode: RuntimeMode
    symbol: str
    side_considered: str | None = None
    bracket_considered: bool = False
    signal_source: SignalSource = "no_valid_signal"
    qlib_raw_score: float | None = None
    predicted_return: float | None = None
    target_return: float | None = None
    candidate_rank: int | None = None
    prediction_artifact_path: str
    model_artifact_path: str
    dataset_artifact_path: str
    source_data_timestamp: datetime | None = None
    source_data_freshness_minutes: int | None = None
    rule_checks: list[RuleCheckRecord] = Field(default_factory=list)
    final_decision_status: DecisionStatus = "no_action"
    final_rejection_reason_code: RejectionReasonCode | None = None
    final_rejection_reason_detail: str | None = None
    notes: list[str] = Field(default_factory=list)


class TradeExecutionRecord(BaseModel):
    """Order-level execution record for accepted or attempted actions."""

    event_id: str = Field(default_factory=lambda: str(uuid4()))
    session_id: str
    run_id: str
    timestamp: datetime
    strategy: str
    mode: RuntimeMode
    symbol: str
    side: str
    quantity: float
    order_id: str | None = None
    client_order_id: str | None = None
    status: str
    reason: str | None = None
    limit_price: float | None = None
    realized_pnl: float | None = None
    metadata: dict[str, Any] = Field(default_factory=dict)


class SignalOutcomeLedgerRow(BaseModel):
    """Flat row for signal acceptance/rejection analytics."""

    event_id: str
    session_id: str
    run_id: str
    timestamp: datetime
    strategy: str
    symbol: str
    signal_source: SignalSource
    final_decision_status: DecisionStatus
    rejection_reason_code: RejectionReasonCode | None = None
    predicted_return: float | None = None
    qlib_raw_score: float | None = None
    candidate_rank: int | None = None
    actual_exit_reason: str | None = None
    realized_pnl: float | None = None


class OrderLifecycleRecord(BaseModel):
    """Persistent order lifecycle row."""

    order_id: str
    session_id: str
    run_id: str
    strategy: str
    mode: RuntimeMode
    symbol: str
    side: str
    quantity: float
    client_order_id: str | None = None
    status: str
    submitted_at: datetime
    avg_fill_price: float | None = None
    metadata: dict[str, Any] = Field(default_factory=dict)


class FillLifecycleRecord(BaseModel):
    """Persistent fill lifecycle row."""

    fill_id: str
    order_id: str
    session_id: str
    run_id: str
    strategy: str
    mode: RuntimeMode
    symbol: str
    quantity: float
    price: float
    filled_at: datetime
    metadata: dict[str, Any] = Field(default_factory=dict)


class RuntimeIncidentRecord(BaseModel):
    """Persistent runtime incident row."""

    incident_id: str = Field(default_factory=lambda: str(uuid4()))
    session_id: str | None = None
    run_id: str | None = None
    timestamp: datetime
    code: str
    severity: Literal["info", "warning", "error", "critical"] = "warning"
    summary: str
    detail: str | None = None
    metadata: dict[str, Any] = Field(default_factory=dict)


class PaperTradingSessionReport(BaseModel):
    """Structured per-session paper trading report persisted to reports and state."""

    session_id: str
    run_id: str
    strategy: str
    mode: RuntimeMode
    started_at: datetime
    completed_at: datetime
    order_count: int
    fill_count: int
    accepted_count: int
    rejected_count: int
    skipped_count: int
    no_trade_success: bool
    artifact_paths: list[str] = Field(default_factory=list)
    report_paths: list[str] = Field(default_factory=list)
    incident_count: int = 0
    notes: list[str] = Field(default_factory=list)
