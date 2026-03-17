"""Reporting services for paper session outputs."""

from __future__ import annotations

import logging

from mytradingbot.core.models import PostSessionReport, SessionResult

logger = logging.getLogger(__name__)


class ReportingService:
    """Generate structured reports from completed session artifacts."""

    def build_post_session_review(self, result: SessionResult) -> PostSessionReport:
        return PostSessionReport(
            session_id=result.session_summary.session_id,
            strategy_name=result.session_summary.strategy_name,
            mode=result.session_summary.mode,
            trade_count=result.session_summary.trade_count,
            rejection_reasons=result.rejection_reasons,
            notes=[
                f"Health summary: {result.health_status.summary}",
                f"Prediction status ready: {result.prediction_status.is_ready}",
            ],
        )
