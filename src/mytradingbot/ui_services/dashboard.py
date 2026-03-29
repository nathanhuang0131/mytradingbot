"""Dashboard UI services."""

from __future__ import annotations

import logging

from pydantic import BaseModel

from mytradingbot.core.capabilities import CapabilitySnapshot
from mytradingbot.core.models import ArtifactStatus, HealthStatus, SessionSummary
from mytradingbot.orchestration.service import TradingPlatformService
from mytradingbot.ui_services.descriptive_sections import DescriptiveSection, describe_item

logger = logging.getLogger(__name__)


class DashboardPayload(BaseModel):
    """Data rendered on the dashboard landing page."""

    health: HealthStatus
    prediction_status: ArtifactStatus
    available_strategies: list[str]
    capabilities: CapabilitySnapshot
    last_session: SessionSummary | None = None
    summary_sections: list[DescriptiveSection] = []


class DashboardService:
    """Build dashboard page payloads."""

    def __init__(self, platform_service: TradingPlatformService) -> None:
        self.platform_service = platform_service

    def get_dashboard_payload(self) -> DashboardPayload:
        health = self.platform_service.get_health_status()
        prediction_status = self.platform_service.get_prediction_status()
        capabilities = self.platform_service.get_capabilities()
        return DashboardPayload(
            health=health,
            prediction_status=prediction_status,
            available_strategies=self.platform_service.get_strategy_names(),
            capabilities=capabilities,
            last_session=(
                self.platform_service.last_session_result.session_summary
                if self.platform_service.last_session_result
                else None
            ),
            summary_sections=[
                DescriptiveSection(
                    title="Runtime Readiness",
                    description="A concise summary of whether the platform is ready for a session and what the operator should watch first.",
                    items=[
                        describe_item(
                            "dashboard.health_summary",
                            health.summary,
                            label="Health summary",
                            description="The top-level health summary produced by the platform.",
                            effect="Tells the operator whether the environment looks ready or needs attention.",
                        ),
                        describe_item(
                            "dashboard.predictions_ready",
                            "Ready" if prediction_status.is_ready else f"{prediction_status.reason or 'Unavailable'}",
                            label="Prediction readiness",
                            description="Whether the runtime prediction artifact is currently usable.",
                            effect="Determines whether qlib-driven session flows can proceed without a freshness warning.",
                        ),
                        describe_item(
                            "dashboard.default_mode",
                            self.platform_service.settings.runtime.default_mode.value,
                            label="Default runtime mode",
                            description="The repo's default runtime mode when a session does not explicitly override it.",
                            effect="Sets the baseline execution mode the operator starts from in the UI.",
                        ),
                        describe_item(
                            "dashboard.strategy_count",
                            len(self.platform_service.get_strategy_names()),
                            label="Available strategies",
                            description="How many strategy choices are currently exposed by the registry.",
                            effect="Shows the breadth of strategy workflows available from the UI.",
                        ),
                    ],
                ),
                DescriptiveSection(
                    title="Phase Capability Snapshot",
                    description="The current readiness of each rollout phase and what each phase means operationally.",
                    items=[
                        describe_item(
                            "dashboard.phase_1",
                            capabilities.phase_1.status,
                            label=capabilities.phase_1.name,
                            description=capabilities.phase_1.summary,
                            effect="Summarizes whether paper-trading artifacts and basic runtime flows are ready.",
                        ),
                        describe_item(
                            "dashboard.phase_2",
                            capabilities.phase_2.status,
                            label=capabilities.phase_2.name,
                            description=capabilities.phase_2.summary,
                            effect="Summarizes whether the market-data download and normalization pipeline is operational.",
                        ),
                        describe_item(
                            "dashboard.phase_3",
                            capabilities.phase_3.status,
                            label=capabilities.phase_3.name,
                            description=capabilities.phase_3.summary,
                            effect="Summarizes whether qlib dataset, training, and prediction-refresh workflows are ready.",
                        ),
                        describe_item(
                            "dashboard.phase_4",
                            capabilities.phase_4.status,
                            label=capabilities.phase_4.name,
                            description=capabilities.phase_4.summary,
                            effect="Summarizes whether live-trading scaffolding is available or still guarded.",
                        ),
                    ],
                ),
            ],
        )
