"""Shared descriptive section models for readable UI output."""

from __future__ import annotations

from dataclasses import dataclass

from pydantic import BaseModel, Field


class DescriptiveItem(BaseModel):
    """Single readable field/value row for UI pages."""

    key: str
    label: str
    value: str
    description: str
    effect: str
    badge: str | None = None


class DescriptiveSection(BaseModel):
    """Readable section of related descriptive items."""

    title: str
    description: str
    items: list[DescriptiveItem] = Field(default_factory=list)


@dataclass(frozen=True)
class FieldDescriptor:
    """Display metadata for a config or status field."""

    label: str
    description: str
    effect: str


FIELD_DESCRIPTORS: dict[str, FieldDescriptor] = {
    "profile.profile_name": FieldDescriptor(
        label="Profile name",
        description="The saved operator profile currently being summarized.",
        effect="Determines which saved session config and active-universe files are read.",
    ),
    "strategy.preset_name": FieldDescriptor(
        label="Preset template",
        description="The preset that last seeded this profile's strategy settings.",
        effect="Explains the default starting point used before any manual customization.",
    ),
    "strategy.strategy_name": FieldDescriptor(
        label="Strategy",
        description="The trading strategy selected for the profile.",
        effect="Changes which signal rules, thresholds, and execution logic are used.",
    ),
    "strategy.run_type": FieldDescriptor(
        label="Run type",
        description="The execution mode selected for the strategy run.",
        effect="Controls whether the workflow behaves as paper, dry-run, or other runtime modes.",
    ),
    "strategy.broker_mode": FieldDescriptor(
        label="Broker mode",
        description="The paper or broker path selected for this profile.",
        effect="Determines whether orders stay local or route to Alpaca paper APIs.",
    ),
    "strategy.session_mode": FieldDescriptor(
        label="Session mode",
        description="The operating pattern selected for the strategy.",
        effect="Changes whether the session is single-run, smoke-style, or looped.",
    ),
    "universe.selection_mode": FieldDescriptor(
        label="Universe mode",
        description="How the active symbol list is built for the profile.",
        effect="Controls whether the current active universe is kept, merged, or replaced.",
    ),
    "universe.target_symbol_count": FieldDescriptor(
        label="Target symbol count",
        description="The number of symbols requested from the liquidity universe flow.",
        effect="A larger number broadens the candidate pool and downstream dataset scope.",
    ),
    "universe.min_price": FieldDescriptor(
        label="Minimum price",
        description="The minimum share price a symbol must meet to qualify for the generated universe.",
        effect="Filters out lower-priced names from the generated active-universe candidates.",
    ),
    "universe.min_average_volume": FieldDescriptor(
        label="Minimum average volume",
        description="The minimum average traded volume required for generated symbols.",
        effect="Filters out less liquid names before they enter the active universe.",
    ),
    "universe.include_etfs": FieldDescriptor(
        label="Include ETFs",
        description="Whether ETFs are allowed into the generated liquidity universe.",
        effect="Expands or narrows the mix of symbols available for trading and training.",
    ),
    "universe.active_symbol_count": FieldDescriptor(
        label="Active symbol count",
        description="The number of symbols currently in the saved active universe.",
        effect="Defines how many symbols the profile can consider during runtime preparation.",
    ),
    "universe.active_symbols_path": FieldDescriptor(
        label="Active universe file",
        description="The repo-local file storing the selected profile's active symbols.",
        effect="This file is the source of truth for profile-scoped symbol selection.",
    ),
    "refresh.loop_interval_seconds": FieldDescriptor(
        label="Loop interval",
        description="How often the supervised loop wakes up when session mode is loop.",
        effect="Controls how frequently the bot checks for fresh inputs and trading actions.",
    ),
    "refresh.auto_refresh_market_snapshot": FieldDescriptor(
        label="Auto-refresh market snapshot",
        description="Whether the runtime refreshes the market snapshot when needed.",
        effect="Keeps microstructure and price inputs current before a decision is made.",
    ),
    "refresh.auto_refresh_predictions": FieldDescriptor(
        label="Auto-refresh predictions",
        description="Whether the runtime refreshes qlib predictions on cadence.",
        effect="Helps prevent trading with stale forecast artifacts.",
    ),
    "refresh.auto_refresh_dataset": FieldDescriptor(
        label="Auto-refresh dataset",
        description="Whether the runtime rebuilds the dataset when inference freshness requires it.",
        effect="Keeps the prediction-refresh pipeline aligned with the latest normalized data.",
    ),
    "refresh.market_refresh_interval_seconds": FieldDescriptor(
        label="Snapshot refresh cadence",
        description="How often the runtime allows a new market snapshot refresh.",
        effect="Sets the freshness target for market inputs.",
    ),
    "refresh.prediction_refresh_interval_seconds": FieldDescriptor(
        label="Prediction refresh cadence",
        description="How often the runtime allows a new prediction refresh.",
        effect="Sets the freshness target for qlib predictions.",
    ),
    "refresh.dataset_refresh_interval_seconds": FieldDescriptor(
        label="Dataset rebuild cadence",
        description="How often the runtime allows a dataset rebuild for inference freshness.",
        effect="Controls how often qlib input features are regenerated before prediction refresh.",
    ),
    "refresh.stale_input_behavior": FieldDescriptor(
        label="Stale input handling",
        description="The policy used when market or prediction artifacts become stale.",
        effect="Determines whether trading blocks, warns, or stops when freshness gates fail.",
    ),
    "alpha.side_mode": FieldDescriptor(
        label="Side mode",
        description="The long/short direction policy selected for the profile.",
        effect="Limits the candidate pool to long ideas, short ideas, or both.",
    ),
    "alpha.candidate_count": FieldDescriptor(
        label="Candidate count",
        description="The number of ranked qlib candidates kept after shortlist filtering.",
        effect="Caps how many symbols move forward into the strategy evaluation path.",
    ),
    "alpha.long_threshold": FieldDescriptor(
        label="Long threshold",
        description="The minimum signed predicted return required for long ideas before shortlist slicing.",
        effect="Filters weak long predictions out before the candidate count is applied.",
    ),
    "alpha.short_threshold": FieldDescriptor(
        label="Short threshold",
        description="The minimum absolute predicted return required for short ideas before shortlist slicing.",
        effect="Filters weak short predictions out before the candidate count is applied.",
    ),
    "alpha.predicted_return_threshold": FieldDescriptor(
        label="Predicted return threshold",
        description="The minimum absolute qlib predicted return required during strategy evaluation.",
        effect="Blocks symbols whose expected move is too small to justify scalping attention.",
    ),
    "alpha.confidence_threshold": FieldDescriptor(
        label="Confidence threshold",
        description="The minimum qlib confidence required during strategy evaluation.",
        effect="Blocks lower-conviction signals before the rest of the strategy filters run.",
    ),
    "alpha.use_latest_trained_model": FieldDescriptor(
        label="Use latest trained model",
        description="Whether the profile follows the canonical latest trained qlib model artifact.",
        effect="Keeps forecasting tied to the newest approved model instead of a custom path.",
    ),
    "alpha.refresh_predictions_before_run": FieldDescriptor(
        label="Refresh predictions before run",
        description="Whether predictions should be refreshed before the session starts.",
        effect="Reduces the chance of entering a run with stale forecast inputs.",
    ),
    "alpha.model_artifact_path": FieldDescriptor(
        label="Model artifact path",
        description="Optional override for the qlib model artifact location.",
        effect="Allows the profile to point at a specific model file instead of the default path.",
    ),
    "risk.max_positions": FieldDescriptor(
        label="Max positions",
        description="The maximum number of concurrent positions the strategy may hold.",
        effect="Limits overall portfolio spread and concurrent exposure.",
    ),
    "risk.max_dollars_per_trade": FieldDescriptor(
        label="Max dollars per trade",
        description="The largest notional size allowed for any new position.",
        effect="Caps single-trade exposure and keeps position sizing conservative.",
    ),
    "risk.max_daily_loss_percent": FieldDescriptor(
        label="Max daily loss",
        description="The maximum tolerated daily drawdown before risk controls should halt new entries.",
        effect="Helps prevent the strategy from compounding losses in a bad session.",
    ),
    "risk.same_symbol_protection": FieldDescriptor(
        label="Same-symbol protection",
        description="Whether the system blocks duplicate exposure in the same symbol.",
        effect="Reduces accidental stacking of repeated entries in one name.",
    ),
    "risk.max_positions_long": FieldDescriptor(
        label="Max long positions",
        description="The maximum number of long positions allowed at one time.",
        effect="Caps long-side concentration independently from short exposure.",
    ),
    "risk.max_positions_short": FieldDescriptor(
        label="Max short positions",
        description="The maximum number of short positions allowed at one time.",
        effect="Caps short-side concentration independently from long exposure.",
    ),
    "risk.cooldown_minutes": FieldDescriptor(
        label="Cooldown after exit",
        description="The waiting time after an exit before the same symbol can re-enter.",
        effect="Reduces immediate churn and repeated entries on the same name.",
    ),
    "risk.block_foreign_manual_exposure": FieldDescriptor(
        label="Block foreign/manual exposure",
        description="Whether outside broker exposure should prevent bot-owned entries.",
        effect="Prevents the bot from trading through positions it did not originate.",
    ),
    "risk.shortability_gate_policy": FieldDescriptor(
        label="Shortability gate policy",
        description="The short-sale availability rule applied before approving short trades.",
        effect="Determines whether short candidates are blocked, warned, or allowed regardless of borrow status.",
    ),
    "risk.reversal_policy": FieldDescriptor(
        label="Reversal policy",
        description="The rule governing how the bot handles reversing an existing symbol exposure.",
        effect="Controls whether reversals are blocked, flattened first, or allowed immediately.",
    ),
    "risk.regime_gating_enabled": FieldDescriptor(
        label="Regime gating enabled",
        description="Whether market regime checks participate in risk gating.",
        effect="Adds or removes an extra layer of environmental filtering before entries.",
    ),
    "execution.order_type": FieldDescriptor(
        label="Order type",
        description="The order instruction used when the strategy submits an entry.",
        effect="Changes how execution requests are routed to the paper broker path.",
    ),
    "execution.bracket_enabled": FieldDescriptor(
        label="Bracket enabled",
        description="Whether bracket protection is attached to approved entries.",
        effect="Enables planned take-profit and stop-loss management around each trade.",
    ),
    "execution.take_profit_percent": FieldDescriptor(
        label="Take-profit",
        description="The configured take-profit distance used for bracket planning.",
        effect="Influences the upside target used when sizing and validating entries.",
    ),
    "execution.stop_loss_percent": FieldDescriptor(
        label="Stop-loss",
        description="The configured stop-loss distance used for bracket planning.",
        effect="Influences the downside protection and risk-per-share calculation.",
    ),
    "execution.sizing_mode": FieldDescriptor(
        label="Sizing mode",
        description="The position sizing method selected for entries.",
        effect="Determines whether quantities come from a fixed number or risk-budget logic.",
    ),
    "execution.quantity": FieldDescriptor(
        label="Quantity",
        description="The fixed quantity used when sizing mode is fixed quantity.",
        effect="Controls the order size sent into the execution path.",
    ),
    "execution.penny_normalization": FieldDescriptor(
        label="Penny normalization",
        description="Whether prices are normalized to broker-valid increments.",
        effect="Helps keep bracket prices valid for broker-side submission rules.",
    ),
    "execution.market_open_only": FieldDescriptor(
        label="Market-open-only policy",
        description="Whether entries are restricted to regular market hours.",
        effect="Prevents the strategy from submitting outside the configured market window.",
    ),
    "execution.allow_after_hours_submission": FieldDescriptor(
        label="Allow after-hours submission",
        description="Whether the profile allows orders outside regular hours when otherwise permitted.",
        effect="Expands or restricts order-routing windows during extended trading sessions.",
    ),
    "execution.smoke_order_behavior": FieldDescriptor(
        label="Smoke order behavior",
        description="How bounded smoke-order tests should be handled after submission.",
        effect="Controls whether smoke orders are automatically canceled or left open.",
    ),
}


def _bool_text(value: bool) -> str:
    return "Enabled" if value else "Disabled"


def format_value(key: str, value: object) -> str:
    """Render config/status values into readable text."""

    if value is None:
        return "Not set"
    if key == "alpha.predicted_return_threshold":
        return f"{float(value) * 100:.2f}%"
    if key in {"execution.take_profit_percent", "execution.stop_loss_percent", "risk.max_daily_loss_percent"}:
        return f"{float(value):.2f}%"
    if key in {
        "refresh.loop_interval_seconds",
        "refresh.market_refresh_interval_seconds",
        "refresh.prediction_refresh_interval_seconds",
        "refresh.dataset_refresh_interval_seconds",
    }:
        return f"{int(value)} seconds"
    if isinstance(value, bool):
        return _bool_text(value)
    if isinstance(value, float):
        return f"{value:.2f}"
    if isinstance(value, list):
        return ", ".join(str(item) for item in value) if value else "None"
    return str(value)


def describe_item(
    key: str,
    value: object,
    *,
    badge: str | None = None,
    label: str | None = None,
    description: str | None = None,
    effect: str | None = None,
) -> DescriptiveItem:
    """Build a descriptive row for a config or status field."""

    descriptor = FIELD_DESCRIPTORS.get(key)
    resolved_label = label or (descriptor.label if descriptor else key.replace(".", " ").replace("_", " ").title())
    resolved_description = description or (
        descriptor.description if descriptor else "Current value for this status field."
    )
    resolved_effect = effect or (
        descriptor.effect if descriptor else "Helps explain how this field changes the workflow."
    )
    return DescriptiveItem(
        key=key,
        label=resolved_label,
        value=format_value(key, value),
        description=resolved_description,
        effect=resolved_effect,
        badge=badge,
    )
