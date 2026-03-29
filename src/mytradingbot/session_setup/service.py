"""Business logic for the guided setup wizard."""

from __future__ import annotations

from datetime import datetime
from pathlib import Path
from typing import Iterable

from mytradingbot.core.settings import AppSettings
from mytradingbot.session_setup.models import (
    FinalUniversePreview,
    FinalUniverseSaveResult,
    PresetName,
    ResolvedSessionConfig,
    SetupWizardState,
    UserProfile,
)
from mytradingbot.session_setup.presets import build_wizard_presets
from mytradingbot.session_setup.storage import SetupWizardStorage
from mytradingbot.universe.service import TopLiquidityUniverseService
from mytradingbot.universe.storage import UniverseStorage


class SetupWizardService:
    def __init__(
        self,
        settings: AppSettings | None = None,
        *,
        storage: SetupWizardStorage | None = None,
        universe_service: TopLiquidityUniverseService | None = None,
        universe_storage: UniverseStorage | None = None,
    ) -> None:
        self.settings = settings or AppSettings()
        self.storage = storage or SetupWizardStorage(settings=self.settings)
        self.universe_service = universe_service or TopLiquidityUniverseService(settings=self.settings)
        self.universe_storage = universe_storage or UniverseStorage(settings=self.settings)
        self.presets = build_wizard_presets()
        self.recommended_defaults = {
            "strategy.strategy_name": "scalping",
            "strategy.broker_mode": "local_paper",
            "strategy.session_mode": "single_run",
            "universe.selection_mode": "keep_old",
            "refresh.loop_interval_seconds": 300,
            "refresh.prediction_refresh_interval_seconds": 600,
            "refresh.auto_refresh_market_snapshot": True,
            "refresh.auto_refresh_predictions": True,
            "alpha.side_mode": "both",
            "alpha.predicted_return_threshold": 0.0008,
            "alpha.confidence_threshold": 0.6,
            "alpha.top_n_per_cycle": 3,
            "alpha.edge_after_cost_min_buffer": 0.0005,
            "risk.max_positions": 3,
            "risk.max_dollars_per_trade": 5000.0,
            "risk.higher_timeframe_filter_enabled": True,
            "risk.higher_timeframe_source_timeframe": "15m",
            "risk.higher_timeframe_fast_ma_length": 5,
            "risk.higher_timeframe_slow_ma_length": 10,
            "risk.disable_pseudo_order_book_gate": True,
            "risk.microstructure_proxy_mode": "soft_rank",
            "risk.microstructure_proxy_min_alignment_score": 0.15,
            "risk.cooldown_minutes": 10,
            "execution.bracket_enabled": True,
        }

    def list_profiles(self) -> list[UserProfile]:
        return self.storage.list_profiles()

    def initialize_wizard(
        self,
        *,
        profile_name: str,
        source_mode: str,
        existing_profile_name: str | None = None,
    ) -> SetupWizardState:
        if source_mode == "load_existing":
            if not existing_profile_name:
                raise ValueError("existing_profile_name is required when loading a saved profile.")
            profile = self.storage.load_profile(existing_profile_name)
            latest = self.storage.load_latest_session_config(profile.profile_slug)
            if latest is not None:
                state = SetupWizardState(
                    profile=profile,
                    source_mode="load_existing",
                    visibility_mode=profile.default_visibility_mode,
                    strategy=latest.strategy,
                    universe=latest.universe,
                    refresh=latest.refresh,
                    alpha=latest.alpha,
                    risk=latest.risk,
                    execution=latest.execution,
                )
                return state
            state = SetupWizardState(
                profile=profile,
                source_mode="load_existing",
                visibility_mode=profile.default_visibility_mode,
            )
            if profile.last_preset_name and profile.last_preset_name in self.presets:
                state = self.apply_preset(state, profile.last_preset_name)  # type: ignore[arg-type]
            return state

        if source_mode == "use_last_setup":
            target_name = existing_profile_name or profile_name
            profile = self.storage.load_profile(target_name)
            latest = self.storage.load_latest_session_config(profile.profile_slug)
            if latest is None:
                raise ValueError(f"No prior session config exists for profile '{target_name}'.")
            return SetupWizardState(
                profile=profile,
                source_mode="use_last_setup",
                visibility_mode=profile.default_visibility_mode,
                strategy=latest.strategy,
                universe=latest.universe,
                refresh=latest.refresh,
                alpha=latest.alpha,
                risk=latest.risk,
                execution=latest.execution,
            )

        profile = UserProfile.create(profile_name)
        state = SetupWizardState(profile=profile, source_mode="create_new")
        state = self.apply_preset(state, "Scalping - Local Paper Safe")
        self.autosave_profile(state)
        return state

    def autosave_profile(self, state: SetupWizardState) -> Path:
        profile = state.profile.model_copy(deep=True)
        profile.updated_at = datetime.now(profile.updated_at.tzinfo)
        profile.last_used_at = profile.updated_at
        profile.last_preset_name = state.strategy.preset_name
        profile.default_visibility_mode = state.visibility_mode
        if state.universe.active_symbols_path:
            profile.latest_active_symbols_path = state.universe.active_symbols_path
        latest_config_path = self.storage.session_config_path(profile.profile_slug)
        if latest_config_path.exists():
            profile.latest_session_config_path = str(latest_config_path)
        return self.storage.save_profile(profile)

    def apply_preset(self, state: SetupWizardState, preset_name: PresetName) -> SetupWizardState:
        preset = self.presets[preset_name]
        updated = state.model_copy(
            deep=True,
            update={
                "strategy": preset["strategy"].model_copy(deep=True),
                "universe": preset["universe"].model_copy(deep=True),
                "refresh": preset["refresh"].model_copy(deep=True),
                "alpha": preset["alpha"].model_copy(deep=True),
                "risk": preset["risk"].model_copy(deep=True),
                "execution": preset["execution"].model_copy(deep=True),
            },
        )
        updated.strategy.preset_name = preset_name
        updated.profile.last_preset_name = preset_name
        return updated

    def resolve_generated_symbols(self, state: SetupWizardState) -> list[str]:
        if state.universe.selection_mode == "keep_old":
            return []
        result = self.universe_service.generate_top_liquidity_universe(
            top_n=state.universe.target_symbol_count,
            minimum_price=state.universe.min_price,
            minimum_average_volume=state.universe.min_average_volume,
            include_etfs=state.universe.include_etfs,
        )
        if not result.ok:
            raise ValueError(result.message)
        state.universe.generated_symbol_count = len(result.rows)
        return [row.symbol for row in result.rows]

    def materialize_active_universe(
        self,
        state: SetupWizardState,
        *,
        generated_symbols: list[str] | None = None,
    ) -> Path:
        profile_slug = state.profile.profile_slug
        existing_symbols = self._default_active_symbols(profile_slug=profile_slug)
        if generated_symbols is None and state.universe.selection_mode != "keep_old":
            generated_symbols = self.resolve_generated_symbols(state.model_copy(deep=True))
        resolved_symbols = self._resolve_active_symbols(
            selection_mode=state.universe.selection_mode,
            existing_symbols=existing_symbols,
            generated_symbols=generated_symbols or [],
        )

        path = self.storage.write_active_symbols(
            profile_slug=profile_slug,
            symbols=resolved_symbols,
        )
        state.universe.active_symbols_path = str(path)
        state.universe.active_symbol_count = len(resolved_symbols)
        return path

    def preview_active_symbols(
        self,
        state: SetupWizardState,
        *,
        generated_symbols: list[str] | None = None,
    ) -> list[str]:
        profile_slug = state.profile.profile_slug
        existing_symbols = self._default_active_symbols(profile_slug=profile_slug)
        return self._resolve_active_symbols(
            selection_mode=state.universe.selection_mode,
            existing_symbols=existing_symbols,
            generated_symbols=generated_symbols or [],
        )

    def preview_final_universe(
        self,
        state: SetupWizardState,
        *,
        generated_symbols: list[str] | None = None,
        manual_symbols: list[str] | None = None,
    ) -> FinalUniversePreview:
        profile_slug = state.profile.profile_slug
        previous_symbols = self._normalize_symbols(
            self._default_active_symbols(profile_slug=profile_slug)
        )
        if generated_symbols is None and state.universe.selection_mode != "keep_old":
            generated_symbols = self.resolve_generated_symbols(state.model_copy(deep=True))
        normalized_generated = self._normalize_symbols(generated_symbols or [])
        normalized_manual = self._normalize_symbols(manual_symbols or [])
        final_symbols = self._resolve_active_symbols(
            selection_mode=state.universe.selection_mode,
            existing_symbols=previous_symbols,
            generated_symbols=normalized_generated,
            manual_symbols=normalized_manual,
        )
        previous_set = set(previous_symbols)
        final_set = set(final_symbols)
        added_symbols = sorted(final_set - previous_set)
        removed_symbols = sorted(previous_set - final_set)
        return FinalUniversePreview(
            previous_symbols=previous_symbols,
            generated_symbols=normalized_generated,
            manual_symbols=normalized_manual,
            final_symbols=final_symbols,
            added_symbols=added_symbols,
            removed_symbols=removed_symbols,
            final_symbol_count=len(final_symbols),
            added_symbol_count=len(added_symbols),
            removed_symbol_count=len(removed_symbols),
        )

    def save_final_universe(
        self,
        state: SetupWizardState,
        *,
        generated_symbols: list[str] | None = None,
        manual_symbols: list[str] | None = None,
    ) -> FinalUniverseSaveResult:
        preview = self.preview_final_universe(
            state,
            generated_symbols=generated_symbols,
            manual_symbols=manual_symbols,
        )
        active_symbols_path = self.storage.write_active_symbols(
            profile_slug=state.profile.profile_slug,
            symbols=preview.final_symbols,
        )
        state.universe.active_symbols_path = str(active_symbols_path)
        state.universe.active_symbol_count = len(preview.final_symbols)
        state.profile.latest_active_symbols_path = str(active_symbols_path)
        self.storage.save_profile(state.profile)

        latest_session_config_path: str | None = None
        latest_config = self.storage.load_latest_session_config(state.profile.profile_slug)
        if latest_config is not None:
            latest_config.universe.selection_mode = state.universe.selection_mode
            latest_config.universe.active_symbols_path = str(active_symbols_path)
            latest_config.universe.active_symbol_count = len(preview.final_symbols)
            latest_config.active_symbols_path = str(active_symbols_path)
            latest_config.active_symbols = preview.final_symbols
            saved_path = self.storage.save_latest_session_config(latest_config)
            latest_session_config_path = str(saved_path)
            state.profile.latest_session_config_path = latest_session_config_path
            self.storage.save_profile(state.profile)

        return FinalUniverseSaveResult(
            profile_slug=state.profile.profile_slug,
            active_symbols_path=str(active_symbols_path),
            latest_session_config_path=latest_session_config_path,
            **preview.model_dump(mode="python"),
        )

    def finalize_setup(
        self,
        state: SetupWizardState,
        *,
        generated_symbols: list[str] | None = None,
    ) -> ResolvedSessionConfig:
        active_symbols_path = self.materialize_active_universe(
            state,
            generated_symbols=generated_symbols,
        )
        active_symbols = self.storage.read_active_symbols(state.profile.profile_slug)
        expected_actions = self._expected_actions(state, active_symbols=active_symbols)
        profile_path = self.autosave_profile(state)
        latest_path = self.storage.session_config_path(state.profile.profile_slug)
        resolved = ResolvedSessionConfig(
            profile_name=state.profile.profile_name,
            profile_slug=state.profile.profile_slug,
            profile_path=str(profile_path),
            latest_session_config_path=str(latest_path),
            preset_name=state.strategy.preset_name,
            strategy=state.strategy,
            universe=state.universe,
            refresh=state.refresh,
            alpha=state.alpha,
            risk=state.risk,
            execution=state.execution,
            active_symbols_path=str(active_symbols_path),
            active_symbols=active_symbols,
            expected_actions=expected_actions,
        )
        latest_saved_path = self.storage.save_latest_session_config(resolved)
        state.profile.latest_session_config_path = str(latest_saved_path)
        state.profile.latest_active_symbols_path = str(active_symbols_path)
        self.storage.save_profile(state.profile)
        return resolved

    def build_expected_actions(
        self,
        state: SetupWizardState,
        *,
        active_symbols: list[str],
    ) -> list[str]:
        return self._expected_actions(state, active_symbols=active_symbols)

    def load_resolved_session_config(self, path: Path) -> ResolvedSessionConfig:
        return ResolvedSessionConfig.model_validate_json(path.read_text(encoding="utf-8"))

    def build_review_flags(self, state: SetupWizardState) -> dict[str, list[str]]:
        defaults: list[str] = []
        customized: list[str] = []
        for dotted_key, expected in self.recommended_defaults.items():
            actual = self._resolve_dotted_value(state, dotted_key)
            if actual == expected:
                defaults.append(dotted_key)
            else:
                customized.append(dotted_key)
        return {"defaults": defaults, "customized": customized}

    def _expected_actions(self, state: SetupWizardState, *, active_symbols: list[str]) -> list[str]:
        actions = [
            f"Use profile '{state.profile.profile_name}'.",
            f"Run strategy '{state.strategy.strategy_name}' in broker mode '{state.strategy.broker_mode}'.",
            f"Use {len(active_symbols)} active symbols from '{state.universe.selection_mode}'.",
        ]
        if state.universe.selection_mode == "combine_old_and_new":
            actions.append("Run liquidity flow, merge new symbols with the existing active universe, and dedupe.")
        elif state.universe.selection_mode == "replace_with_new":
            actions.append("Run liquidity flow and replace the active universe manifest only.")
        else:
            actions.append("Keep the existing active universe manifest.")
        actions.append("Retain all historical downloaded data already on disk.")
        if state.refresh.auto_refresh_market_snapshot:
            actions.append("Auto-refresh the market snapshot on the configured cadence.")
        if state.refresh.auto_refresh_predictions:
            actions.append("Auto-refresh predictions on the configured cadence.")
        if state.refresh.auto_refresh_dataset:
            actions.append("Incrementally rebuild the dataset only when the inference-refresh policy requires it.")
        if state.strategy.session_mode == "loop":
            actions.append(f"Launch a supervised loop every {state.refresh.loop_interval_seconds} seconds.")
        elif state.strategy.session_mode == "bounded_smoke":
            actions.append("Run a bounded smoke session using a single cycle.")
        else:
            actions.append("Run a single session from the latest saved configuration.")
        return actions

    def _default_active_symbols(self, *, profile_slug: str) -> list[str]:
        existing = self.storage.read_active_symbols(profile_slug)
        if existing:
            return existing
        latest_universe = self.settings.paths.universe_dir / "latest_top_liquidity_universe.json"
        if latest_universe.exists():
            return self.universe_storage.load_symbols(latest_universe)
        return self._normalize_symbols(self.settings.data.default_symbols)

    @staticmethod
    def _normalize_symbols(symbols: Iterable[str]) -> list[str]:
        cleaned = sorted({str(symbol).strip().upper() for symbol in symbols if str(symbol).strip()})
        return cleaned

    def _resolve_active_symbols(
        self,
        *,
        selection_mode: str,
        existing_symbols: list[str],
        generated_symbols: list[str],
        manual_symbols: list[str] | None = None,
    ) -> list[str]:
        normalized_existing = self._normalize_symbols(existing_symbols)
        normalized_generated = self._normalize_symbols(generated_symbols)
        normalized_manual = self._normalize_symbols(manual_symbols or [])

        if selection_mode == "keep_old":
            return self._normalize_symbols([*normalized_existing, *normalized_manual])
        if selection_mode == "combine_old_and_new":
            return self._normalize_symbols(
                [*normalized_existing, *normalized_generated, *normalized_manual]
            )
        return self._normalize_symbols([*normalized_generated, *normalized_manual])

    @staticmethod
    def _resolve_dotted_value(state: SetupWizardState, dotted_key: str):
        current = state
        for part in dotted_key.split("."):
            current = getattr(current, part)
        return current
