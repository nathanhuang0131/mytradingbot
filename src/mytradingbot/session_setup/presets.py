"""Preset templates for the guided setup wizard."""

from __future__ import annotations

from mytradingbot.session_setup.models import (
    AlphaModelProfile,
    ExecutionProfile,
    PresetName,
    RefreshPolicyProfile,
    RiskProfile,
    StrategyProfile,
    UniverseSelectionProfile,
)


def build_wizard_presets() -> dict[PresetName, dict[str, object]]:
    return {
        "Scalping - Local Paper Safe": {
            "strategy": StrategyProfile(
                preset_name="Scalping - Local Paper Safe",
                strategy_name="scalping",
                broker_mode="local_paper",
                session_mode="single_run",
            ),
            "universe": UniverseSelectionProfile(
                selection_mode="keep_old",
                target_symbol_count=100,
                min_price=15.0,
                min_average_volume=500_000,
            ),
            "refresh": RefreshPolicyProfile(),
            "alpha": AlphaModelProfile(side_mode="long_only"),
            "risk": RiskProfile(),
            "execution": ExecutionProfile(),
        },
        "Scalping - Alpaca Paper Long Only": {
            "strategy": StrategyProfile(
                preset_name="Scalping - Alpaca Paper Long Only",
                strategy_name="scalping",
                broker_mode="alpaca_paper_api",
                session_mode="single_run",
            ),
            "universe": UniverseSelectionProfile(
                selection_mode="keep_old",
                target_symbol_count=100,
                min_price=15.0,
                min_average_volume=500_000,
            ),
            "refresh": RefreshPolicyProfile(),
            "alpha": AlphaModelProfile(side_mode="long_only"),
            "risk": RiskProfile(),
            "execution": ExecutionProfile(),
        },
        "Scalping - Alpaca Paper Long + Short": {
            "strategy": StrategyProfile(
                preset_name="Scalping - Alpaca Paper Long + Short",
                strategy_name="scalping",
                broker_mode="alpaca_paper_api",
                session_mode="single_run",
            ),
            "universe": UniverseSelectionProfile(
                selection_mode="keep_old",
                target_symbol_count=100,
                min_price=15.0,
                min_average_volume=500_000,
            ),
            "refresh": RefreshPolicyProfile(),
            "alpha": AlphaModelProfile(side_mode="both"),
            "risk": RiskProfile(),
            "execution": ExecutionProfile(),
        },
        "Scalping - Smoke Test": {
            "strategy": StrategyProfile(
                preset_name="Scalping - Smoke Test",
                strategy_name="scalping",
                broker_mode="local_paper",
                session_mode="bounded_smoke",
                smoke_max_cycles=1,
            ),
            "universe": UniverseSelectionProfile(
                selection_mode="keep_old",
                target_symbol_count=25,
                min_price=15.0,
                min_average_volume=500_000,
            ),
            "refresh": RefreshPolicyProfile(loop_interval_seconds=60),
            "alpha": AlphaModelProfile(side_mode="long_only"),
            "risk": RiskProfile(max_positions=1, max_positions_long=1, max_positions_short=0),
            "execution": ExecutionProfile(quantity=1.0, smoke_order_behavior="auto_cancel"),
        },
        "Scalping - Overnight Loop": {
            "strategy": StrategyProfile(
                preset_name="Scalping - Overnight Loop",
                strategy_name="scalping",
                broker_mode="alpaca_paper_api",
                session_mode="loop",
            ),
            "universe": UniverseSelectionProfile(
                selection_mode="combine_old_and_new",
                target_symbol_count=100,
                min_price=15.0,
                min_average_volume=500_000,
            ),
            "refresh": RefreshPolicyProfile(
                auto_refresh_market_snapshot=True,
                auto_refresh_predictions=True,
                auto_refresh_dataset=True,
                loop_interval_seconds=300,
                market_refresh_interval_seconds=300,
                prediction_refresh_interval_seconds=1800,
                dataset_refresh_interval_seconds=1800,
            ),
            "alpha": AlphaModelProfile(side_mode="both"),
            "risk": RiskProfile(),
            "execution": ExecutionProfile(),
        },
    }
