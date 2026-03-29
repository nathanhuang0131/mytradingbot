import json
from pathlib import Path

from mytradingbot.core.models import utc_now
from mytradingbot.core.paths import RepoPaths
from mytradingbot.core.settings import AppSettings
from mytradingbot.data.models import MarketDataPipelineResult
from mytradingbot.orchestration.service import TradingPlatformService
from mytradingbot.qlib_engine.models import QlibOperationResult
from mytradingbot.session_setup.service import SetupWizardService
from mytradingbot.training.models import AlphaTrainingRunResult, TrainingDataQualityReport
from mytradingbot.ui_services.data_training import DataTrainingService


def _build_settings(repo_root: Path) -> AppSettings:
    settings = AppSettings(paths=RepoPaths.for_root(repo_root))
    settings.ensure_runtime_directories()
    return settings


def test_data_training_service_surfaces_capability_truth() -> None:
    payload = DataTrainingService(
        TradingPlatformService.bootstrap_default()
    ).get_payload()

    assert payload.capabilities.phase_1.name == "Phase 1"
    assert "download_market_data" in payload.works_without_pyqlib


def test_data_training_service_resolves_profile_active_universe_file(tmp_path: Path) -> None:
    settings = _build_settings(tmp_path)
    wizard_service = SetupWizardService(settings=settings)
    state = wizard_service.initialize_wizard(profile_name="Alice Trader", source_mode="create_new")
    state.universe.selection_mode = "replace_with_new"
    wizard_service.finalize_setup(state, generated_symbols=["AAPL", "MSFT"])

    service = DataTrainingService(
        TradingPlatformService(settings=settings),
    )

    payload = service.get_payload()
    universe_source = service.resolve_universe_source(profile_name="Alice Trader")

    assert "Alice Trader" in payload.profile_names
    assert payload.default_profile_name == "Alice Trader"
    assert universe_source.default_universe_file_path == str(
        settings.paths.active_universes_dir / "alice_trader_active_symbols.json"
    )
    assert universe_source.selected_universe_file_path == universe_source.default_universe_file_path
    assert universe_source.symbols == ["AAPL", "MSFT"]
    assert universe_source.symbol_count == 2
    assert universe_source.alternate_universe_file_path == str(
        settings.paths.universe_dir / "latest_top_liquidity_universe.json"
    )


def test_data_training_service_prefers_symbols_file_for_file_scoped_actions(tmp_path: Path) -> None:
    settings = _build_settings(tmp_path)
    universe_file = settings.paths.active_universes_dir / "alice_trader_active_symbols.json"
    universe_file.parent.mkdir(parents=True, exist_ok=True)
    universe_file.write_text(json.dumps(["AAPL", "MSFT"]), encoding="utf-8")
    platform_service = TradingPlatformService(settings=settings)
    service = DataTrainingService(platform_service)
    captured: dict[str, object] = {"market_data_calls": []}

    def fake_download_market_data(**kwargs):
        captured["market_data_calls"].append(kwargs)
        return MarketDataPipelineResult(ok=True, message="downloaded")

    def fake_build_dataset(**kwargs):
        captured["build_dataset"] = kwargs
        return QlibOperationResult(ok=True, message="dataset built")

    def fake_ensure_universe(*, symbols=None, symbols_file=None, top_n=None):
        captured["ensure_universe"] = {
            "symbols": symbols,
            "symbols_file": symbols_file,
            "top_n": top_n,
        }
        return ["AAPL", "MSFT"]

    def fake_run_quality_check(*, symbols, timeframes, minimum_eligible_symbols=None):
        captured["quality_check"] = {
            "symbols": symbols,
            "timeframes": timeframes,
            "minimum_eligible_symbols": minimum_eligible_symbols,
        }
        return TrainingDataQualityReport(
            ok=True,
            message="quality ok",
            generated_at=utc_now(),
            timeframes=timeframes,
            requested_symbols=symbols,
            eligible_symbols=symbols,
        )

    def fake_run_alpha_robust_training(**kwargs):
        captured["alpha_training"] = kwargs
        return AlphaTrainingRunResult(ok=True, message="training ok")

    platform_service.download_market_data = fake_download_market_data
    platform_service.build_dataset = fake_build_dataset
    service.training_service.ensure_universe = fake_ensure_universe
    service.training_service.run_quality_check = fake_run_quality_check
    service.training_service.run_alpha_robust_training = fake_run_alpha_robust_training

    service.download_market_data(symbols_file=universe_file, timeframes=["1m"])
    service.update_market_data(symbols_file=universe_file, timeframes=["5m"])
    service.build_dataset(strategy_name="scalping", symbols_file=universe_file)
    service.check_training_data_quality(
        strategy_name="scalping",
        symbols_file=universe_file,
        timeframes=["1m", "5m"],
    )
    service.run_alpha_robust_training(
        strategy_name="scalping",
        symbols_file=universe_file,
        timeframes=["1m", "5m"],
    )

    assert captured["market_data_calls"] == [
        {
            "symbols": None,
            "symbols_file": universe_file,
            "timeframes": ["1m"],
            "full_refresh": True,
        },
        {
            "symbols": None,
            "symbols_file": universe_file,
            "timeframes": ["5m"],
            "full_refresh": False,
        },
    ]
    assert captured["build_dataset"] == {
        "strategy_name": "scalping",
        "symbols": None,
        "symbols_file": universe_file,
    }
    assert captured["ensure_universe"] == {
        "symbols": None,
        "symbols_file": universe_file,
        "top_n": None,
    }
    assert captured["quality_check"] == {
        "symbols": ["AAPL", "MSFT"],
        "timeframes": ["1m", "5m"],
        "minimum_eligible_symbols": None,
    }
    assert captured["alpha_training"] == {
        "strategy_name": "scalping",
        "symbols": None,
        "symbols_file": universe_file,
        "timeframes": ["1m", "5m"],
    }
