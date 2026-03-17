from mytradingbot.orchestration.service import TradingPlatformService
from mytradingbot.ui_services.dashboard import DashboardService


def test_dashboard_service_surfaces_prediction_health() -> None:
    payload = DashboardService(TradingPlatformService.bootstrap_default()).get_dashboard_payload()

    assert payload.health is not None
    assert payload.prediction_status is not None
    assert payload.available_strategies
