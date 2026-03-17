"""Dashboard UI services."""

from __future__ import annotations

import logging

from pydantic import BaseModel

from mytradingbot.core.models import ArtifactStatus, HealthStatus, SessionSummary
from mytradingbot.orchestration.service import TradingPlatformService

logger = logging.getLogger(__name__)


class DashboardPayload(BaseModel):
    """Data rendered on the dashboard landing page."""

    health: HealthStatus
    prediction_status: ArtifactStatus
    available_strategies: list[str]
    last_session: SessionSummary | None = None


class DashboardService:
    """Build dashboard page payloads."""

    def __init__(self, platform_service: TradingPlatformService) -> None:
        self.platform_service = platform_service

    def get_dashboard_payload(self) -> DashboardPayload:
        return DashboardPayload(
            health=self.platform_service.get_health_status(),
            prediction_status=self.platform_service.get_prediction_status(),
            available_strategies=self.platform_service.get_strategy_names(),
            last_session=(
                self.platform_service.last_session_result.session_summary
                if self.platform_service.last_session_result
                else None
            ),
        )
