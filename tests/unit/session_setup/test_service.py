from __future__ import annotations

import json
from datetime import datetime, timezone

from mytradingbot.core.paths import RepoPaths
from mytradingbot.core.settings import AppSettings
from mytradingbot.session_setup.service import SetupWizardService
from mytradingbot.universe.models import TopLiquidityUniverseResult, UniverseLiquidityRow


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


def test_setup_wizard_service_resolves_generated_symbols_with_universe_filters(tmp_path) -> None:
    class RecordingUniverseService:
        def __init__(self) -> None:
            self.calls = []

        def generate_top_liquidity_universe(self, **kwargs):
            self.calls.append(kwargs)
            return TopLiquidityUniverseResult(
                ok=True,
                message="ok",
                rows=[
                    UniverseLiquidityRow(
                        symbol="AAPL",
                        exchange="NASDAQ",
                        asset_class="us_equity",
                        status="active",
                        tradable=True,
                        marginable=True,
                        shortable=True,
                        easy_to_borrow=True,
                        avg_close=200.0,
                        avg_volume=2_000_000,
                        avg_dollar_volume=400_000_000.0,
                        median_dollar_volume=395_000_000.0,
                        completeness_ratio=1.0,
                        rank=1,
                        lookback_start=datetime(2026, 2, 1, tzinfo=timezone.utc),
                        lookback_end=datetime(2026, 3, 1, tzinfo=timezone.utc),
                        bars_used=20,
                        generated_at=datetime(2026, 3, 1, tzinfo=timezone.utc),
                    )
                ],
                artifacts=["data/universe/latest_top_liquidity_universe.json"],
            )

    settings = AppSettings(paths=RepoPaths.for_root(tmp_path))
    recording_service = RecordingUniverseService()
    service = SetupWizardService(settings=settings, universe_service=recording_service)  # type: ignore[arg-type]
    state = service.initialize_wizard(profile_name="Alice Trader", source_mode="create_new")
    state.universe.selection_mode = "combine_old_and_new"
    state.universe.target_symbol_count = 125
    state.universe.min_price = 17.5
    state.universe.min_average_volume = 750_000
    state.universe.include_etfs = True

    symbols = service.resolve_generated_symbols(state)

    assert symbols == ["AAPL"]
    assert state.universe.generated_symbol_count == 1
    assert recording_service.calls == [
        {
            "top_n": 125,
            "minimum_price": 17.5,
            "minimum_average_volume": 750_000,
            "include_etfs": True,
        }
    ]


def test_setup_wizard_service_persists_scalping_thresholds_in_latest_config(tmp_path) -> None:
    settings = AppSettings(paths=RepoPaths.for_root(tmp_path))
    service = SetupWizardService(settings=settings)
    state = service.initialize_wizard(profile_name="Alice Trader", source_mode="create_new")
    state.alpha.predicted_return_threshold = 0.007
    state.alpha.confidence_threshold = 0.72

    resolved = service.finalize_setup(state, generated_symbols=["AAPL", "MSFT"])
    latest = service.storage.load_latest_session_config(state.profile.profile_slug)

    assert resolved.alpha.predicted_return_threshold == 0.007
    assert resolved.alpha.confidence_threshold == 0.72
    assert latest is not None
    assert latest.alpha.predicted_return_threshold == 0.007
    assert latest.alpha.confidence_threshold == 0.72


def test_setup_wizard_service_previews_final_universe_with_diff_counts_and_manual_additions(
    tmp_path,
) -> None:
    settings = AppSettings(paths=RepoPaths.for_root(tmp_path))
    service = SetupWizardService(settings=settings)
    state = service.initialize_wizard(profile_name="Alice Trader", source_mode="create_new")
    state.universe.selection_mode = "replace_with_new"
    service.storage.write_active_symbols(
        profile_slug=state.profile.profile_slug,
        symbols=["AAPL", "MSFT", "AMD"],
    )

    preview = service.preview_final_universe(
        state,
        generated_symbols=["MSFT", "NVDA"],
        manual_symbols=[" tsla ", "nvda"],
    )

    assert preview.previous_symbols == ["AAPL", "AMD", "MSFT"]
    assert preview.generated_symbols == ["MSFT", "NVDA"]
    assert preview.manual_symbols == ["NVDA", "TSLA"]
    assert preview.final_symbols == ["MSFT", "NVDA", "TSLA"]
    assert preview.added_symbols == ["NVDA", "TSLA"]
    assert preview.removed_symbols == ["AAPL", "AMD"]
    assert preview.final_symbol_count == 3
    assert preview.added_symbol_count == 2
    assert preview.removed_symbol_count == 2


def test_setup_wizard_service_save_final_universe_updates_manifest_and_latest_config(
    tmp_path,
) -> None:
    settings = AppSettings(paths=RepoPaths.for_root(tmp_path))
    service = SetupWizardService(settings=settings)
    state = service.initialize_wizard(profile_name="Alice Trader", source_mode="create_new")
    state.universe.selection_mode = "combine_old_and_new"
    service.finalize_setup(state, generated_symbols=["AAPL", "MSFT"])

    saved = service.save_final_universe(
        state,
        generated_symbols=["MSFT", "NVDA"],
        manual_symbols=[" tsla "],
    )

    latest_config = service.storage.load_latest_session_config(state.profile.profile_slug)
    assert latest_config is not None
    assert saved.final_symbols == ["AAPL", "MSFT", "NVDA", "TSLA"]
    assert json.loads(
        service.storage
        .active_symbols_path(state.profile.profile_slug)
        .read_text(encoding="utf-8")
    ) == ["AAPL", "MSFT", "NVDA", "TSLA"]
    assert latest_config.active_symbols == ["AAPL", "MSFT", "NVDA", "TSLA"]
    assert latest_config.universe.active_symbol_count == 4
    assert latest_config.active_symbols_path == str(
        service.storage.active_symbols_path(state.profile.profile_slug)
    )
