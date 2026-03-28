from mytradingbot.orchestration.service import TradingPlatformService
from mytradingbot.ui_services.dashboard import DashboardService


def test_dashboard_service_surfaces_prediction_health() -> None:
    payload = DashboardService(TradingPlatformService.bootstrap_default()).get_dashboard_payload()

    assert payload.health is not None
    assert payload.prediction_status is not None
    assert payload.available_strategies


def test_dashboard_service_builds_readable_summary_sections() -> None:
    payload = DashboardService(TradingPlatformService.bootstrap_default()).get_dashboard_payload()

    section_titles = [section.title for section in payload.summary_sections]

    assert "Runtime Readiness" in section_titles
    assert "Phase Capability Snapshot" in section_titles
    assert all(section.description for section in payload.summary_sections)
    assert all(item.description and item.effect for section in payload.summary_sections for item in section.items)
