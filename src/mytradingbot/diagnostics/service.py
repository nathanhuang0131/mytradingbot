"""Diagnostics builders for operator-facing system status."""

from __future__ import annotations

import logging

from mytradingbot.core.models import HealthStatus, NoTradeDiagnostics, SessionResult

logger = logging.getLogger(__name__)


class DiagnosticsService:
    """Build diagnostics from real runtime artifacts."""

    def build_no_trade_report(self, result: SessionResult) -> NoTradeDiagnostics:
        reasons = result.rejection_reasons or ["No trade attempts passed strategy or risk checks."]
        return NoTradeDiagnostics(
            summary="No trades were executed during the session.",
            reasons=reasons,
        )

    def build_prediction_diagnostics(self, result: SessionResult) -> HealthStatus:
        status = result.prediction_status
        if status.is_ready:
            return HealthStatus(
                summary="Predictions are fresh and ready.",
                ok=True,
                issues=[],
            )

        reason = status.reason or "unknown"
        issue = f"Prediction artifact is {reason}."
        return HealthStatus(summary=issue, ok=False, issues=[issue, *status.guidance])
