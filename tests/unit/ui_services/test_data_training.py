from mytradingbot.orchestration.service import TradingPlatformService
from mytradingbot.ui_services.data_training import DataTrainingService


def test_data_training_service_surfaces_capability_truth() -> None:
    payload = DataTrainingService(
        TradingPlatformService.bootstrap_default()
    ).get_payload()

    assert payload.capabilities.phase_1.name == "Phase 1"
    assert "download_market_data" in payload.works_without_pyqlib
