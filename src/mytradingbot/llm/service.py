"""Advisory-only LLM workflows grounded in runtime artifacts."""

from __future__ import annotations

import logging
from typing import Any

from mytradingbot.core.models import AdvisoryResponse, SessionResult, TradeAttemptTrace

logger = logging.getLogger(__name__)


class AdvisoryLLMService:
    """Provide advisory summaries without affecting trading decisions."""

    def __init__(self, client: Any | None) -> None:
        self.client = client

    def explain_signal(self, attempt: TradeAttemptTrace) -> AdvisoryResponse:
        symbol = attempt.symbol
        strategy = attempt.strategy_name
        details = [
            f"Qlib remains the authority for direction and ranking on {symbol}.",
            f"Strategy under review: {strategy}.",
        ]
        if attempt.strategy_outcome and attempt.strategy_outcome.failed_filters:
            details.append(
                "Rejected filters: "
                + ", ".join(attempt.strategy_outcome.failed_filters)
            )
        return AdvisoryResponse(
            summary=f"Advisory explanation for the qlib-driven {strategy} signal on {symbol}.",
            details=details,
        )

    def summarize_diagnostics(self, result: SessionResult) -> AdvisoryResponse:
        details = [
            f"Health: {result.health_status.summary}",
            f"Prediction ready: {result.prediction_status.is_ready}",
            f"Rejection reasons: {', '.join(result.rejection_reasons) if result.rejection_reasons else 'none'}",
        ]
        return AdvisoryResponse(
            summary="Advisory diagnostics summary generated from recorded session artifacts.",
            details=details,
        )

    def compare_strategies(self, results: list[SessionResult]) -> AdvisoryResponse:
        details = [
            (
                f"{result.session_summary.strategy_name}: "
                f"{result.session_summary.trade_count} trades, "
                f"{result.session_summary.rejected_trade_count} rejected"
            )
            for result in results
        ]
        return AdvisoryResponse(
            summary="Advisory strategy comparison based on recorded session results.",
            details=details,
        )

    def build_post_market_review(self, result: SessionResult) -> AdvisoryResponse:
        return AdvisoryResponse(
            summary="Advisory post-market review generated from session artifacts.",
            details=[
                f"Trades executed: {result.session_summary.trade_count}",
                f"Rejections: {len(result.rejection_reasons)}",
            ],
        )

    def generate_export_pack(self, result: SessionResult) -> dict[str, Any]:
        return {
            "mode": "advisory",
            "session_id": result.session_summary.session_id,
            "strategy_name": result.session_summary.strategy_name,
            "trade_count": result.session_summary.trade_count,
            "rejection_reasons": result.rejection_reasons,
        }

    def import_structured_feedback(self, payload: dict[str, Any]) -> dict[str, Any]:
        return {
            "mode": "advisory",
            "feedback": payload,
        }
