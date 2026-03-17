"""Diagnostics UI services."""

from __future__ import annotations

import logging

from pydantic import BaseModel

from mytradingbot.diagnostics.service import DiagnosticsService
from mytradingbot.orchestration.service import TradingPlatformService
from mytradingbot.reporting.service import ReportingService

logger = logging.getLogger(__name__)


class DiagnosticsPayload(BaseModel):
    """Diagnostics page payload."""

    prediction_health: str
    no_trade_summary: str | None = None
    post_session_notes: list[str] = []


class DiagnosticsPageService:
    """Build diagnostics and report payloads for the UI."""

    def __init__(self, platform_service: TradingPlatformService) -> None:
        self.platform_service = platform_service
        self.diagnostics_service = DiagnosticsService()
        self.reporting_service = ReportingService()

    def get_payload(self) -> DiagnosticsPayload:
        result = self.platform_service.last_session_result
        if result is None:
            health = self.platform_service.get_prediction_status()
            return DiagnosticsPayload(
                prediction_health=f"{health.name}: ready={health.is_ready}",
            )

        prediction = self.diagnostics_service.build_prediction_diagnostics(result)
        no_trade = (
            self.diagnostics_service.build_no_trade_report(result)
            if result.session_summary.trade_count == 0
            else None
        )
        report = self.reporting_service.build_post_session_review(result)
        return DiagnosticsPayload(
            prediction_health=prediction.summary,
            no_trade_summary=no_trade.summary if no_trade else None,
            post_session_notes=report.notes,
        )
