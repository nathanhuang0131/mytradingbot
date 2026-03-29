"""Typed models for the guided setup wizard."""

from __future__ import annotations

import re
from datetime import datetime
from typing import Literal

from pydantic import BaseModel, Field, computed_field

from mytradingbot.core.enums import RuntimeMode, StrategyName
from mytradingbot.core.models import utc_now
from mytradingbot.runtime.models import BrokerMode

ProfileSourceMode = Literal["create_new", "load_existing", "use_last_setup"]
WizardVisibilityMode = Literal["basic", "advanced", "expert"]
WizardSessionMode = Literal["single_run", "bounded_smoke", "loop"]
UniverseSelectionMode = Literal["keep_old", "combine_old_and_new", "replace_with_new"]
TradeSideMode = Literal["long_only", "short_only", "both"]
StaleInputBehavior = Literal["block_trading", "warn_only", "stop_session"]
SizingMode = Literal["fixed_quantity", "risk_budget"]
OrderType = Literal["market", "limit"]
PresetName = Literal[
    "Scalping - Local Paper Safe",
    "Scalping - Alpaca Paper Long Only",
    "Scalping - Alpaca Paper Long + Short",
    "Scalping - Smoke Test",
    "Scalping - Overnight Loop",
]


def slugify_profile_name(value: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "_", value.strip().lower()).strip("_")
    return slug or "default_profile"


class UserProfile(BaseModel):
    profile_name: str
    profile_slug: str
    created_at: datetime = Field(default_factory=utc_now)
    updated_at: datetime = Field(default_factory=utc_now)
    last_used_at: datetime | None = None
    last_preset_name: str | None = None
    default_visibility_mode: WizardVisibilityMode = "basic"
    latest_session_config_path: str | None = None
    latest_active_symbols_path: str | None = None

    @classmethod
    def create(cls, profile_name: str) -> "UserProfile":
        now = utc_now()
        return cls(
            profile_name=profile_name.strip(),
            profile_slug=slugify_profile_name(profile_name),
            created_at=now,
            updated_at=now,
            last_used_at=now,
        )


class StrategyProfile(BaseModel):
    preset_name: str = "Scalping - Local Paper Safe"
    strategy_name: str = StrategyName.SCALPING.value
    run_type: RuntimeMode = RuntimeMode.PAPER
    broker_mode: BrokerMode = "local_paper"
    session_mode: WizardSessionMode = "single_run"
    smoke_max_cycles: int = 1
    loop_max_cycles: int | None = None


class UniverseSelectionProfile(BaseModel):
    selection_mode: UniverseSelectionMode = "keep_old"
    target_symbol_count: int = 100
    min_price: float = 15.0
    min_average_volume: int = 500_000
    min_dollar_volume: float | None = None
    include_etfs: bool = False
    exchange_filters: list[str] = Field(default_factory=list)
    active_symbols_path: str | None = None
    active_symbol_count: int = 0
    generated_symbol_count: int = 0
    delete_historical_data: bool = False


class RefreshPolicyProfile(BaseModel):
    auto_refresh_market_snapshot: bool = True
    auto_refresh_predictions: bool = True
    auto_refresh_dataset: bool = True
    loop_interval_seconds: int = 300
    stale_input_behavior: StaleInputBehavior = "block_trading"
    market_refresh_interval_seconds: int = 300
    prediction_refresh_interval_seconds: int = 600
    dataset_refresh_interval_seconds: int = 1800
    training_remains_separate: bool = True
    market_snapshot_max_age_minutes: int = 15
    predictions_max_age_minutes: int = 60


class AlphaModelProfile(BaseModel):
    use_latest_trained_model: bool = True
    side_mode: TradeSideMode = "both"
    refresh_predictions_before_run: bool = True
    candidate_count: int = 20
    top_n_per_cycle: int = 3
    model_artifact_path: str | None = None
    long_threshold: float = 0.0
    short_threshold: float = 0.0
    predicted_return_threshold: float = 0.0008
    confidence_threshold: float = 0.6
    edge_after_cost_min_buffer: float = 0.0005


class RiskProfile(BaseModel):
    max_positions: int = 3
    max_dollars_per_trade: float = 5_000.0
    max_daily_loss_percent: float = 2.0
    same_symbol_protection: bool = True
    max_positions_long: int = 3
    max_positions_short: int = 2
    cooldown_minutes: int = 10
    block_foreign_manual_exposure: bool = True
    shortability_gate_policy: Literal["required", "warn", "off"] = "required"
    reversal_policy: Literal["block", "allow_after_flatten", "allow_immediate"] = "block"
    regime_gating_enabled: bool = True
    higher_timeframe_filter_enabled: bool = True
    higher_timeframe_source_timeframe: str = "15m"
    higher_timeframe_fast_ma_length: int = 5
    higher_timeframe_slow_ma_length: int = 10
    disable_pseudo_order_book_gate: bool = True
    microstructure_proxy_mode: Literal["off", "soft_rank", "confirmation_gate"] = "soft_rank"
    microstructure_proxy_min_alignment_score: float = 0.15


class ExecutionProfile(BaseModel):
    order_type: OrderType = "market"
    bracket_enabled: bool = True
    take_profit_percent: float = 0.6
    stop_loss_percent: float = 0.35
    sizing_mode: SizingMode = "fixed_quantity"
    quantity: float = 1.0
    penny_normalization: bool = True
    market_open_only: bool = False
    allow_after_hours_submission: bool = False
    smoke_order_behavior: Literal["auto_cancel", "leave_open"] = "auto_cancel"


class SetupWizardState(BaseModel):
    profile: UserProfile
    source_mode: ProfileSourceMode = "create_new"
    visibility_mode: WizardVisibilityMode = "basic"
    strategy: StrategyProfile = Field(default_factory=StrategyProfile)
    universe: UniverseSelectionProfile = Field(default_factory=UniverseSelectionProfile)
    refresh: RefreshPolicyProfile = Field(default_factory=RefreshPolicyProfile)
    alpha: AlphaModelProfile = Field(default_factory=AlphaModelProfile)
    risk: RiskProfile = Field(default_factory=RiskProfile)
    execution: ExecutionProfile = Field(default_factory=ExecutionProfile)
    customized_fields: list[str] = Field(default_factory=list)

    @computed_field  # type: ignore[prop-decorator]
    @property
    def active_profile_slug(self) -> str:
        return self.profile.profile_slug


class ResolvedSessionConfig(BaseModel):
    config_version: str = "wizard_v1"
    saved_at: datetime = Field(default_factory=utc_now)
    profile_name: str
    profile_slug: str
    profile_path: str
    latest_session_config_path: str
    preset_name: str
    strategy: StrategyProfile
    universe: UniverseSelectionProfile
    refresh: RefreshPolicyProfile
    alpha: AlphaModelProfile
    risk: RiskProfile
    execution: ExecutionProfile
    active_symbols_path: str
    active_symbols: list[str]
    expected_actions: list[str] = Field(default_factory=list)
    launch_ready: bool = True


class FinalUniversePreview(BaseModel):
    previous_symbols: list[str] = Field(default_factory=list)
    generated_symbols: list[str] = Field(default_factory=list)
    manual_symbols: list[str] = Field(default_factory=list)
    final_symbols: list[str] = Field(default_factory=list)
    added_symbols: list[str] = Field(default_factory=list)
    removed_symbols: list[str] = Field(default_factory=list)
    final_symbol_count: int = 0
    added_symbol_count: int = 0
    removed_symbol_count: int = 0


class FinalUniverseSaveResult(FinalUniversePreview):
    profile_slug: str
    active_symbols_path: str
    latest_session_config_path: str | None = None
