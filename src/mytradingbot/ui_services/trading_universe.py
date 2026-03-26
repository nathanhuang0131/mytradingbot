"""Trading universe UI services."""

from __future__ import annotations

import json
import re
from typing import Any

from pydantic import BaseModel, Field

from mytradingbot.core.models import QlibPrediction, SignalBundle
from mytradingbot.orchestration.service import TradingPlatformService
from mytradingbot.strategies.scalping import ScalpingStrategy
from mytradingbot.session_setup.models import FinalUniversePreview, FinalUniverseSaveResult
from mytradingbot.session_setup.service import SetupWizardService


class TradingUniversePayload(BaseModel):
    profile_names: list[str] = Field(default_factory=list)
    selection_modes: list[str] = Field(
        default_factory=lambda: ["keep_old", "combine_old_and_new", "only_new"]
    )
    default_profile_name: str | None = None


class TradingUniverseUIService:
    """Expose profile-scoped trading-universe preview and save actions to Streamlit."""

    def __init__(
        self,
        platform_service: TradingPlatformService,
        *,
        wizard_service: SetupWizardService | None = None,
    ) -> None:
        self.platform_service = platform_service
        self.wizard_service = wizard_service or SetupWizardService(
            settings=self.platform_service.settings
        )

    def get_payload(self) -> TradingUniversePayload:
        profiles = self.wizard_service.list_profiles()
        profile_names = [profile.profile_name for profile in profiles]
        return TradingUniversePayload(
            profile_names=profile_names,
            default_profile_name=profile_names[0] if profile_names else None,
        )

    def preview_universe(
        self,
        *,
        profile_name: str,
        selection_mode: str,
        generated_symbols: list[str] | None = None,
        manual_symbols_text: str = "",
        target_symbol_count: int | None = None,
        min_price: float | None = None,
        min_average_volume: int | None = None,
        include_etfs: bool | None = None,
    ) -> FinalUniversePreview:
        state = self._load_state(profile_name)
        state.universe.selection_mode = self._selection_mode(selection_mode)
        self._apply_universe_overrides(
            state,
            target_symbol_count=target_symbol_count,
            min_price=min_price,
            min_average_volume=min_average_volume,
            include_etfs=include_etfs,
        )
        return self.wizard_service.preview_final_universe(
            state,
            generated_symbols=generated_symbols,
            manual_symbols=self._parse_manual_symbols_text(manual_symbols_text),
        )

    def save_universe(
        self,
        *,
        profile_name: str,
        selection_mode: str,
        generated_symbols: list[str] | None = None,
        manual_symbols_text: str = "",
        target_symbol_count: int | None = None,
        min_price: float | None = None,
        min_average_volume: int | None = None,
        include_etfs: bool | None = None,
    ) -> FinalUniverseSaveResult:
        state = self._load_state(profile_name)
        state.universe.selection_mode = self._selection_mode(selection_mode)
        self._apply_universe_overrides(
            state,
            target_symbol_count=target_symbol_count,
            min_price=min_price,
            min_average_volume=min_average_volume,
            include_etfs=include_etfs,
        )
        return self.wizard_service.save_final_universe(
            state,
            generated_symbols=generated_symbols,
            manual_symbols=self._parse_manual_symbols_text(manual_symbols_text),
        )

    def get_qlib_prediction_rows(
        self,
        *,
        profile_name: str,
        selection_mode: str,
        generated_symbols: list[str] | None = None,
        manual_symbols_text: str = "",
        target_symbol_count: int | None = None,
        min_price: float | None = None,
        min_average_volume: int | None = None,
        include_etfs: bool | None = None,
        view_mode: str = "raw",
    ) -> list[dict[str, Any]]:
        state = self._load_state(profile_name)
        state.universe.selection_mode = self._selection_mode(selection_mode)
        self._apply_universe_overrides(
            state,
            target_symbol_count=target_symbol_count,
            min_price=min_price,
            min_average_volume=min_average_volume,
            include_etfs=include_etfs,
        )
        preview = self.wizard_service.preview_final_universe(
            state,
            generated_symbols=generated_symbols,
            manual_symbols=self._parse_manual_symbols_text(manual_symbols_text),
        )
        final_symbols = set(preview.final_symbols)
        strategy = ScalpingStrategy(settings=self._settings_for_state(state))
        market_snapshots = self._load_market_snapshots()

        rows: list[dict[str, Any]] = []
        for prediction in self._load_predictions_for_table():
            row = prediction.model_dump(mode="json")
            row["is_final_symbol"] = prediction.symbol in final_symbols
            indicated_tp_pct, indicated_sl_pct = self._indicated_targets(
                strategy,
                prediction,
                market_snapshots,
            )
            row["indicated_tp_pct"] = indicated_tp_pct
            row["indicated_sl_pct"] = indicated_sl_pct
            rows.append(row)

        if view_mode == "raw":
            return rows
        if view_mode == "final":
            return [row for row in rows if row["is_final_symbol"]]
        raise ValueError(f"Unsupported qlib prediction view mode: {view_mode}")

    def _load_state(self, profile_name: str):
        existing_names = {profile.profile_name for profile in self.wizard_service.list_profiles()}
        if profile_name in existing_names:
            return self.wizard_service.initialize_wizard(
                profile_name=profile_name,
                source_mode="load_existing",
                existing_profile_name=profile_name,
            )
        return self.wizard_service.initialize_wizard(
            profile_name=profile_name,
            source_mode="create_new",
        )

    @staticmethod
    def _selection_mode(selection_mode: str) -> str:
        if selection_mode == "only_new":
            return "replace_with_new"
        return selection_mode

    @staticmethod
    def _parse_manual_symbols_text(text: str) -> list[str]:
        return [part for part in re.split(r"[\s,]+", text) if part]

    @staticmethod
    def _apply_universe_overrides(
        state,
        *,
        target_symbol_count: int | None,
        min_price: float | None,
        min_average_volume: int | None,
        include_etfs: bool | None,
    ) -> None:
        if target_symbol_count is not None:
            state.universe.target_symbol_count = int(target_symbol_count)
        if min_price is not None:
            state.universe.min_price = float(min_price)
        if min_average_volume is not None:
            state.universe.min_average_volume = int(min_average_volume)
        if include_etfs is not None:
            state.universe.include_etfs = bool(include_etfs)

    def _settings_for_state(self, state):
        settings = self.platform_service.settings.model_copy(deep=True)
        settings.scalping.max_position_notional = state.risk.max_dollars_per_trade
        settings.scalping.stop_loss_buffer_bps = state.execution.stop_loss_percent * 100
        settings.scalping.predicted_return_threshold = state.alpha.predicted_return_threshold
        settings.scalping.confidence_threshold = state.alpha.confidence_threshold
        return settings

    def _load_predictions_for_table(self) -> list[QlibPrediction]:
        predictions_path = self.platform_service.qlib_service.predictions_path
        if not predictions_path.exists():
            return []
        try:
            raw_payload = json.loads(predictions_path.read_text(encoding="utf-8-sig"))
        except json.JSONDecodeError as exc:
            raise ValueError(
                f"Prediction artifact at {predictions_path} is not valid JSON."
            ) from exc

        prediction_records = self._normalize_prediction_payload(raw_payload)
        return [QlibPrediction.model_validate(item) for item in prediction_records]

    def _load_market_snapshots(self) -> dict[str, Any]:
        try:
            return self.platform_service.market_data_service.load_market_snapshots()
        except FileNotFoundError:
            return {}

    @staticmethod
    def _normalize_prediction_payload(raw_payload: object) -> list[object]:
        if isinstance(raw_payload, list):
            return raw_payload
        if isinstance(raw_payload, dict) and isinstance(raw_payload.get("predictions"), list):
            return raw_payload["predictions"]
        raise ValueError(
            "Prediction artifact payload must be a list of prediction records or a dict with a 'predictions' list."
        )

    @staticmethod
    def _indicated_targets(
        strategy: ScalpingStrategy,
        prediction: QlibPrediction,
        market_snapshots: dict[str, Any],
    ) -> tuple[float | None, float | None]:
        snapshot = market_snapshots.get(prediction.symbol)
        if snapshot is None:
            return None, None
        signal = SignalBundle(
            symbol=prediction.symbol,
            prediction=prediction,
            market=snapshot,
        )
        take_profit_delta, stop_loss_delta = strategy._target_deltas(signal)
        return round(take_profit_delta, 4), round(stop_loss_delta, 4)
