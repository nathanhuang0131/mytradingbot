from mytradingbot.orchestration.service import TradingPlatformService
from mytradingbot.ui_services.setup_wizard import SetupWizardUIService


def test_setup_wizard_ui_service_exposes_profiles_presets_and_recommended_defaults() -> None:
    payload = SetupWizardUIService(
        TradingPlatformService.bootstrap_default()
    ).get_payload()

    assert "Scalping - Local Paper Safe" in payload.preset_names
    assert "Scalping - Overnight Loop" in payload.preset_names
    assert payload.recommended_defaults["strategy.strategy_name"] == "scalping"
    assert payload.recommended_defaults["strategy.broker_mode"] == "local_paper"
    assert payload.recommended_defaults["refresh.loop_interval_seconds"] == 300
