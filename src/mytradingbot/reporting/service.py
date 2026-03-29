"""Reporting services for paper session outputs."""

from __future__ import annotations

import logging

from mytradingbot.core.models import PostSessionReport, SessionResult

logger = logging.getLogger(__name__)


class ReportingService:
    """Generate structured reports from completed session artifacts."""

    def build_post_session_review(self, result: SessionResult) -> PostSessionReport:
        bracket_notes: list[str] = []
        for attempt in result.trade_attempts:
            strategy_outcome = attempt.strategy_outcome
            if strategy_outcome and strategy_outcome.intent and strategy_outcome.intent.bracket_plan:
                plan = strategy_outcome.intent.bracket_plan
                bracket_notes.append(
                    "Bracket review: "
                    f"{attempt.symbol} entry={plan.planned_entry_price:.4f} "
                    f"stop={plan.planned_stop_loss_price:.4f} "
                    f"target={plan.planned_take_profit_price:.4f} "
                    f"fees={plan.estimated_fees:.4f} "
                    f"slippage={plan.estimated_slippage:.4f} "
                    f"net_rr={plan.reward_risk_ratio:.4f}"
                )
            execution = attempt.execution_outcome
            if execution and execution.bracket_state:
                bracket_notes.append(
                    "Bracket outcome: "
                    f"{attempt.symbol} exit_reason={execution.bracket_state.exit_reason} "
                    f"realized_pnl={execution.bracket_state.realized_pnl}"
                )
        return PostSessionReport(
            session_id=result.session_summary.session_id,
            strategy_name=result.session_summary.strategy_name,
            mode=result.session_summary.mode,
            trade_count=result.session_summary.trade_count,
            rejection_reasons=result.rejection_reasons,
            notes=[
                f"Health summary: {result.health_status.summary}",
                f"Prediction status ready: {result.prediction_status.is_ready}",
                (
                    "Decision pipeline ready: "
                    f"{result.decision_pipeline_readiness.decision_pipeline_ready}"
                    if result.decision_pipeline_readiness is not None
                    else "Decision pipeline ready: unknown"
                ),
                (
                    "Decision block reason: "
                    f"{result.decision_pipeline_readiness.decision_block_reason}"
                    if result.decision_pipeline_readiness is not None
                    and result.decision_pipeline_readiness.decision_block_reason is not None
                    else "Decision block reason: none"
                ),
                *bracket_notes,
            ],
        )
