from __future__ import annotations

import json

from mytradingbot.core.paths import RepoPaths
from mytradingbot.core.settings import AppSettings
from mytradingbot.session_setup.service import SetupWizardService


def test_setup_wizard_service_creates_new_profile_and_autosaves_it(tmp_path) -> None:
    settings = AppSettings(paths=RepoPaths.for_root(tmp_path))
    service = SetupWizardService(settings=settings)

    state = service.initialize_wizard(profile_name="Alice Trader", source_mode="create_new")

    profile_path = settings.paths.user_profiles_dir / "alice_trader.json"
    assert state.profile.profile_name == "Alice Trader"
    assert profile_path.exists()


def test_setup_wizard_service_loads_existing_profile(tmp_path) -> None:
    settings = AppSettings(paths=RepoPaths.for_root(tmp_path))
    service = SetupWizardService(settings=settings)

    original = service.initialize_wizard(profile_name="Alice Trader", source_mode="create_new")
    original = service.apply_preset(original, "Scalping - Alpaca Paper Long Only")
    service.autosave_profile(original)

    loaded = service.initialize_wizard(
        profile_name="ignored",
        source_mode="load_existing",
        existing_profile_name="Alice Trader",
    )

    assert loaded.profile.profile_name == "Alice Trader"
    assert loaded.strategy.preset_name == "Scalping - Alpaca Paper Long Only"
    assert loaded.strategy.broker_mode == "alpaca_paper_api"


def test_setup_wizard_service_applies_presets_with_real_defaults(tmp_path) -> None:
    settings = AppSettings(paths=RepoPaths.for_root(tmp_path))
    service = SetupWizardService(settings=settings)
    state = service.initialize_wizard(profile_name="Alice Trader", source_mode="create_new")

    state = service.apply_preset(state, "Scalping - Overnight Loop")

    assert state.strategy.strategy_name == "scalping"
    assert state.strategy.session_mode == "loop"
    assert state.refresh.auto_refresh_market_snapshot is True
    assert state.refresh.auto_refresh_predictions is True
    assert state.alpha.side_mode == "both"


def test_setup_wizard_service_keep_old_symbols_preserves_existing_manifest(tmp_path) -> None:
    settings = AppSettings(paths=RepoPaths.for_root(tmp_path))
    service = SetupWizardService(settings=settings)
    state = service.initialize_wizard(profile_name="Alice Trader", source_mode="create_new")
    state.universe.selection_mode = "keep_old"

    old_symbols = ["AAPL", "MSFT", "NVDA"]
    service.storage.write_active_symbols(profile_slug=state.profile.profile_slug, symbols=old_symbols)

    resolved_path = service.materialize_active_universe(state, generated_symbols=["TSLA", "AMD"])

    assert json.loads(resolved_path.read_text(encoding="utf-8")) == old_symbols


def test_setup_wizard_service_combines_old_and_new_symbols_with_dedupe(tmp_path) -> None:
    settings = AppSettings(paths=RepoPaths.for_root(tmp_path))
    service = SetupWizardService(settings=settings)
    state = service.initialize_wizard(profile_name="Alice Trader", source_mode="create_new")
    state.universe.selection_mode = "combine_old_and_new"

    service.storage.write_active_symbols(
        profile_slug=state.profile.profile_slug,
        symbols=["AAPL", "MSFT"],
    )

    resolved_path = service.materialize_active_universe(
        state,
        generated_symbols=["MSFT", "NVDA", "TSLA"],
    )

    assert json.loads(resolved_path.read_text(encoding="utf-8")) == ["AAPL", "MSFT", "NVDA", "TSLA"]


def test_setup_wizard_service_replaces_active_symbols_without_deleting_historical_data(tmp_path) -> None:
    settings = AppSettings(paths=RepoPaths.for_root(tmp_path))
    service = SetupWizardService(settings=settings)
    state = service.initialize_wizard(profile_name="Alice Trader", source_mode="create_new")
    state.universe.selection_mode = "replace_with_new"

    raw_file = settings.paths.raw_data_dir / "alpaca" / "bars" / "1m" / "AAPL.parquet"
    raw_file.parent.mkdir(parents=True, exist_ok=True)
    raw_file.write_text("historical-data-retained", encoding="utf-8")
    service.storage.write_active_symbols(
        profile_slug=state.profile.profile_slug,
        symbols=["AAPL", "MSFT"],
    )

    resolved_path = service.materialize_active_universe(
        state,
        generated_symbols=["TSLA", "AMD"],
    )

    assert json.loads(resolved_path.read_text(encoding="utf-8")) == ["AMD", "TSLA"]
    assert raw_file.exists()


def test_setup_wizard_service_generates_and_autosaves_resolved_session_config(tmp_path) -> None:
    settings = AppSettings(paths=RepoPaths.for_root(tmp_path))
    service = SetupWizardService(settings=settings)
    state = service.initialize_wizard(profile_name="Alice Trader", source_mode="create_new")
    state = service.apply_preset(state, "Scalping - Alpaca Paper Long + Short")
    state.universe.selection_mode = "replace_with_new"

    resolved = service.finalize_setup(state, generated_symbols=["AAPL", "MSFT", "NVDA"])

    latest_path = settings.paths.session_profiles_dir / "alice_trader_latest.json"
    assert latest_path.exists()
    assert resolved.profile_name == "Alice Trader"
    assert resolved.strategy.strategy_name == "scalping"
    assert resolved.strategy.broker_mode == "alpaca_paper_api"
    assert resolved.alpha.side_mode == "both"
    assert resolved.active_symbols == ["AAPL", "MSFT", "NVDA"]
    assert resolved.active_symbols_path == str(
        settings.paths.active_universes_dir / "alice_trader_active_symbols.json"
    )
