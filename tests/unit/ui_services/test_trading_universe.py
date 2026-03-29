from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

from mytradingbot.core.paths import RepoPaths
from mytradingbot.core.settings import AppSettings
from mytradingbot.orchestration.service import TradingPlatformService
from mytradingbot.session_setup.service import SetupWizardService
from mytradingbot.ui_services.trading_universe import TradingUniverseUIService


def _build_settings(repo_root: Path) -> AppSettings:
    settings = AppSettings(paths=RepoPaths.for_root(repo_root))
    settings.ensure_runtime_directories()
    return settings


def _write_prediction_and_market_artifacts(settings: AppSettings) -> None:
    generated_at = datetime(2026, 3, 25, 0, 15, tzinfo=timezone.utc)
    settings.prediction_artifact_path().parent.mkdir(parents=True, exist_ok=True)
    settings.prediction_artifact_path().write_text(
        json.dumps(
            [
                {
                    "symbol": "AAPL",
                    "score": 0.95,
                    "predicted_return": 0.012,
                    "confidence": 0.84,
                    "rank": 1,
                    "direction": "long",
                    "generated_at": generated_at.isoformat(),
                    "horizon": "intraday",
                },
                {
                    "symbol": "MSFT",
                    "score": -0.91,
                    "predicted_return": -0.011,
                    "confidence": 0.8,
                    "rank": 2,
                    "direction": "short",
                    "generated_at": generated_at.isoformat(),
                    "horizon": "intraday",
                },
                {
                    "symbol": "NVDA",
                    "score": 0.5,
                    "predicted_return": 0.006,
                    "confidence": 0.7,
                    "rank": 3,
                    "direction": "long",
                    "generated_at": generated_at.isoformat(),
                    "horizon": "intraday",
                },
            ]
        ),
        encoding="utf-8",
    )
    settings.market_snapshot_artifact_path().parent.mkdir(parents=True, exist_ok=True)
    settings.market_snapshot_artifact_path().write_text(
        json.dumps(
            [
                {
                    "symbol": "AAPL",
                    "last_price": 100.0,
                    "vwap": 99.4,
                    "spread_bps": 1.0,
                    "volume": 1500000,
                    "liquidity_score": 0.88,
                    "liquidity_stress": 0.2,
                    "order_book_imbalance": 0.35,
                    "liquidity_sweep_detected": False,
                    "volatility_regime": "normal",
                    "timestamp": generated_at.isoformat(),
                },
                {
                    "symbol": "MSFT",
                    "last_price": 100.0,
                    "vwap": 100.6,
                    "spread_bps": 1.0,
                    "volume": 1500000,
                    "liquidity_score": 0.88,
                    "liquidity_stress": 0.2,
                    "order_book_imbalance": -0.35,
                    "liquidity_sweep_detected": False,
                    "volatility_regime": "normal",
                    "timestamp": generated_at.isoformat(),
                },
                {
                    "symbol": "NVDA",
                    "last_price": 100.0,
                    "vwap": 99.4,
                    "spread_bps": 1.0,
                    "volume": 1500000,
                    "liquidity_score": 0.88,
                    "liquidity_stress": 0.2,
                    "order_book_imbalance": 0.35,
                    "liquidity_sweep_detected": False,
                    "volatility_regime": "normal",
                    "timestamp": generated_at.isoformat(),
                },
            ]
        ),
        encoding="utf-8",
    )


def test_trading_universe_ui_service_exposes_profiles_and_preview(tmp_path: Path) -> None:
    settings = _build_settings(tmp_path)
    wizard_service = SetupWizardService(settings=settings)
    state = wizard_service.initialize_wizard(profile_name="Alice Trader", source_mode="create_new")
    state.universe.selection_mode = "replace_with_new"
    wizard_service.finalize_setup(state, generated_symbols=["AAPL", "MSFT"])

    service = TradingUniverseUIService(
        TradingPlatformService(settings=settings),
        wizard_service=wizard_service,
    )

    payload = service.get_payload()
    preview = service.preview_universe(
        profile_name="Alice Trader",
        selection_mode="combine_old_and_new",
        generated_symbols=["MSFT", "NVDA"],
        manual_symbols_text=" tsla \n",
    )

    assert "Alice Trader" in payload.profile_names
    assert payload.selection_modes == ["keep_old", "combine_old_and_new", "only_new"]
    assert preview.final_symbols == ["AAPL", "MSFT", "NVDA", "TSLA"]
    assert preview.added_symbols == ["NVDA", "TSLA"]
    assert preview.removed_symbols == []


def test_trading_universe_ui_service_saves_manifest_for_future_runs(tmp_path: Path) -> None:
    settings = _build_settings(tmp_path)
    wizard_service = SetupWizardService(settings=settings)
    state = wizard_service.initialize_wizard(profile_name="Alice Trader", source_mode="create_new")
    state.universe.selection_mode = "replace_with_new"
    wizard_service.finalize_setup(state, generated_symbols=["AAPL", "MSFT"])

    service = TradingUniverseUIService(
        TradingPlatformService(settings=settings),
        wizard_service=wizard_service,
    )

    result = service.save_universe(
        profile_name="Alice Trader",
        selection_mode="only_new",
        generated_symbols=["NVDA"],
        manual_symbols_text=" tsla \n nvda ",
    )

    manifest_path = settings.paths.active_universes_dir / "alice_trader_active_symbols.json"
    assert result.final_symbols == ["NVDA", "TSLA"]
    assert json.loads(manifest_path.read_text(encoding="utf-8")) == ["NVDA", "TSLA"]


def test_trading_universe_ui_service_exposes_raw_and_final_qlib_prediction_views(
    tmp_path: Path,
) -> None:
    settings = _build_settings(tmp_path)
    _write_prediction_and_market_artifacts(settings)
    wizard_service = SetupWizardService(settings=settings)
    state = wizard_service.initialize_wizard(profile_name="Alice Trader", source_mode="create_new")
    state.universe.selection_mode = "replace_with_new"
    wizard_service.finalize_setup(state, generated_symbols=["AAPL", "MSFT"])

    service = TradingUniverseUIService(
        TradingPlatformService(settings=settings),
        wizard_service=wizard_service,
    )

    raw_rows = service.get_qlib_prediction_rows(
        profile_name="Alice Trader",
        selection_mode="only_new",
        generated_symbols=["AAPL", "MSFT"],
        view_mode="raw",
    )
    final_rows = service.get_qlib_prediction_rows(
        profile_name="Alice Trader",
        selection_mode="only_new",
        generated_symbols=["AAPL", "MSFT"],
        view_mode="final",
    )

    assert [row["symbol"] for row in raw_rows] == ["AAPL", "MSFT", "NVDA"]
    assert [row["symbol"] for row in final_rows] == ["AAPL", "MSFT"]
    assert raw_rows[0]["is_final_symbol"] is True
    assert raw_rows[2]["is_final_symbol"] is False
    assert raw_rows[0]["score"] == 0.95
    assert raw_rows[0]["predicted_return"] == 0.012
    assert raw_rows[0]["confidence"] == 0.84
    assert raw_rows[0]["indicated_tp_pct"] == 0.009
    assert raw_rows[0]["indicated_sl_pct"] == 0.005
