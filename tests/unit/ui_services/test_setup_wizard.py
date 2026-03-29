from mytradingbot.core.paths import RepoPaths
from mytradingbot.core.settings import AppSettings
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
    assert payload.recommended_defaults["refresh.prediction_refresh_interval_seconds"] == 600
    assert payload.recommended_defaults["alpha.predicted_return_threshold"] == 0.0008
    assert payload.recommended_defaults["alpha.confidence_threshold"] == 0.6
    assert payload.recommended_defaults["alpha.top_n_per_cycle"] == 3
    assert payload.recommended_defaults["alpha.edge_after_cost_min_buffer"] == 0.0005
    assert payload.recommended_defaults["risk.higher_timeframe_filter_enabled"] is True
    assert payload.recommended_defaults["risk.higher_timeframe_source_timeframe"] == "15m"
    assert payload.recommended_defaults["risk.higher_timeframe_fast_ma_length"] == 5
    assert payload.recommended_defaults["risk.higher_timeframe_slow_ma_length"] == 10
    assert payload.recommended_defaults["risk.disable_pseudo_order_book_gate"] is True
    assert payload.recommended_defaults["risk.microstructure_proxy_mode"] == "soft_rank"
    assert payload.recommended_defaults["risk.microstructure_proxy_min_alignment_score"] == 0.15
    assert payload.recommended_defaults["risk.cooldown_minutes"] == 10


def test_setup_wizard_ui_service_builds_readable_review_payload(tmp_path) -> None:
    settings = AppSettings(paths=RepoPaths.for_root(tmp_path))
    platform_service = TradingPlatformService(settings=settings)
    service = SetupWizardUIService(platform_service)
    state = service.initialize_wizard(
        profile_name="Alice Trader",
        source_mode="create_new",
    )
    state.alpha.confidence_threshold = 0.72
    state.risk.max_positions = 8

    review = service.build_review_payload(
        state,
        generated_symbols=["AAPL", "MSFT", "NVDA"],
    )

    assert review.sections
    assert any(section.title == "Risk Controls" for section in review.sections)
    assert any(section.title == "Execution & Brackets" for section in review.sections)
    assert review.defaults_section.items
    assert review.customized_section.items
    assert all("." not in item.label for item in review.defaults_section.items)
    assert all(item.description and item.effect for item in review.defaults_section.items)
    assert all(item.description and item.effect for item in review.customized_section.items)
