from __future__ import annotations

from pathlib import Path

import streamlit as st

from app.components.runtime import get_platform_service
from mytradingbot.core.enums import RuntimeMode
from mytradingbot.session_setup.models import SetupWizardState
from mytradingbot.ui_services.setup_wizard import SetupWizardUIService


STEPS = [
    "User Profile",
    "Strategy & Session",
    "Symbol Universe",
    "Refresh & Data Policy",
    "Alpha & Model",
    "Risk Controls",
    "Execution & Brackets",
    "Review & Start",
]

RECOMMENDED_BADGE = (
    "<span style='display:inline-block;padding:2px 8px;border-radius:999px;"
    "background:#e8f5ee;color:#185c37;font-size:0.8rem;font-weight:600;'>"
    "Recommended default</span>"
)


def _wizard_state_key(name: str) -> str:
    version = st.session_state.get("wizard_form_version", 0)
    return f"wizard_{version}_{name}"


def _wizard_state() -> SetupWizardState | None:
    return st.session_state.get("wizard_state")


def _set_wizard_state(state: SetupWizardState) -> None:
    st.session_state["wizard_state"] = state


def _bump_form_version() -> None:
    st.session_state["wizard_form_version"] = st.session_state.get("wizard_form_version", 0) + 1


def _recommended_hint(label: str) -> None:
    st.markdown(
        f"{RECOMMENDED_BADGE}<div style='font-size:0.88rem;color:#5b6470;margin-top:0.3rem'>{label}</div>",
        unsafe_allow_html=True,
    )


def _step_navigation(*, step: int) -> None:
    progress = (step + 1) / len(STEPS)
    st.progress(progress)
    left, right = st.columns([3, 1])
    left.markdown(f"### Step {step + 1} of {len(STEPS)}: {STEPS[step]}")
    right.caption(f"Visibility: {st.session_state.get('wizard_visibility_mode', 'basic').title()}")


def _profile_card(payload, selected_name: str | None) -> None:
    if not selected_name:
        return
    card = next((profile for profile in payload.profiles if profile.profile_name == selected_name), None)
    if card is None:
        return
    st.info(
        "\n".join(
            [
                f"Profile: `{card.profile_name}`",
                f"Last used: `{card.last_used_at or 'new profile'}`",
                f"Last preset: `{card.last_preset_name or 'none yet'}`",
            ]
        )
    )


def _render_profile_step(service: SetupWizardUIService, payload) -> None:
    st.subheader("Choose a profile")
    st.caption("Profiles are auto-saved. You do not need a separate manual save step.")
    source_mode = st.radio(
        "Profile action",
        options=[
            ("create_new", "Create new profile"),
            ("load_existing", "Load existing profile"),
            ("use_last_setup", "Use last setup as starting point"),
        ],
        format_func=lambda item: item[1],
        key=_wizard_state_key("profile_source_mode"),
    )[0]
    profile_name = st.text_input(
        "User or profile name",
        value=st.session_state.get("wizard_profile_name", ""),
        help="This name is used to create or load a repo-local profile file automatically.",
        key=_wizard_state_key("profile_name"),
    )
    selected_existing = None
    if payload.profile_names:
        selected_existing = st.selectbox(
            "Existing profiles",
            options=payload.profile_names,
            index=0,
            help="Pick a saved profile to load or use as a starting point.",
            key=_wizard_state_key("existing_profile_name"),
        )
    _profile_card(payload, selected_existing)
    st.session_state["wizard_profile_source_mode"] = source_mode
    st.session_state["wizard_profile_name"] = profile_name
    st.session_state["wizard_existing_profile_name"] = selected_existing


def _render_strategy_step(service: SetupWizardUIService, payload, state: SetupWizardState) -> None:
    st.subheader("Select strategy and session mode")
    preset_name = st.selectbox(
        "Preset template",
        options=payload.preset_names,
        index=payload.preset_names.index(state.strategy.preset_name),
        help="Presets apply recommended defaults but remain fully editable.",
        key=_wizard_state_key("preset_name"),
    )
    if preset_name != state.strategy.preset_name:
        state = service.apply_preset(state, preset_name)
        _set_wizard_state(state)
        _bump_form_version()
        st.rerun()

    strategy_name = st.selectbox(
        "Strategy",
        options=payload.available_strategies,
        index=payload.available_strategies.index(state.strategy.strategy_name),
        key=_wizard_state_key("strategy_name"),
    )
    _recommended_hint("Scalping is the recommended starting strategy for guided paper sessions.")
    run_type = st.selectbox(
        "Run type",
        options=["paper"],
        index=0,
        key=_wizard_state_key("run_type"),
    )
    _recommended_hint("Paper mode is the safe default while the wizard remains dashboard-first.")
    broker_mode = st.selectbox(
        "Broker mode",
        options=payload.broker_modes,
        index=payload.broker_modes.index(state.strategy.broker_mode),
        key=_wizard_state_key("broker_mode"),
        help="Use local_paper for repo-local simulation or alpaca_paper_api to route real Alpaca paper orders.",
    )
    if broker_mode == "local_paper":
        _recommended_hint("Local paper is the safest default while you validate a new profile.")
    session_mode = st.radio(
        "Session mode",
        options=payload.session_modes,
        horizontal=True,
        index=payload.session_modes.index(state.strategy.session_mode),
        key=_wizard_state_key("session_mode"),
    )
    state.strategy.strategy_name = strategy_name
    state.strategy.run_type = RuntimeMode(run_type)
    state.strategy.broker_mode = broker_mode
    state.strategy.session_mode = session_mode
    _set_wizard_state(state)


def _render_universe_step(service: SetupWizardUIService, state: SetupWizardState) -> None:
    st.subheader("Choose symbol behavior")
    option = st.radio(
        "Active symbol behavior",
        options=[
            ("keep_old", "Keep using old symbols"),
            ("combine_old_and_new", "Run liquidity flow and combine new symbols with old symbols"),
            ("replace_with_new", "Use completely new symbols"),
        ],
        format_func=lambda item: item[1],
        key=_wizard_state_key("universe_mode"),
    )[0]
    state.universe.selection_mode = option
    explanations = {
        "keep_old": "Continue using the current active universe manifest for this profile.",
        "combine_old_and_new": "Generate a fresh liquidity universe, merge it with the current active set, and dedupe symbols.",
        "replace_with_new": "Generate a fresh liquidity universe and replace only the active manifest for this profile.",
    }
    st.info(explanations[option])

    if option != "keep_old":
        col1, col2 = st.columns(2)
        state.universe.target_symbol_count = int(
            col1.number_input(
                "Target symbol count",
                min_value=1,
                value=state.universe.target_symbol_count,
                step=10,
                key=_wizard_state_key("target_symbol_count"),
            )
        )
        _recommended_hint("Use the preset default unless you have a strong reason to change the active universe size.")
        state.universe.min_price = float(
            col2.number_input(
                "Minimum price",
                min_value=1.0,
                value=float(state.universe.min_price),
                step=1.0,
                key=_wizard_state_key("min_price"),
            )
        )
        state.universe.min_average_volume = int(
            col1.number_input(
                "Minimum average volume",
                min_value=1_000,
                value=state.universe.min_average_volume,
                step=50_000,
                key=_wizard_state_key("min_avg_volume"),
            )
        )
        state.universe.include_etfs = bool(
            col2.checkbox(
                "Include ETFs",
                value=state.universe.include_etfs,
                key=_wizard_state_key("include_etfs"),
            )
        )
        if st.button("Preview qualifying symbols", key=_wizard_state_key("preview_universe")):
            generated = service.preview_generated_symbols(state)
            st.session_state["wizard_generated_symbols"] = generated
            st.session_state["wizard_generated_symbol_count"] = len(generated)
            st.success(f"Preview generated {len(generated)} qualifying symbols.")
        generated = st.session_state.get("wizard_generated_symbols", [])
        if generated:
            st.caption(f"Preview count: {len(generated)} symbols")
            st.code(", ".join(generated[:20]) + (" ..." if len(generated) > 20 else ""))

    summary_lines = [
        f"Selection mode: `{state.universe.selection_mode}`",
        "Historical downloaded data is retained on disk.",
        "Active symbols are tracked separately from historical raw/normalized parquet.",
    ]
    if state.universe.selection_mode == "combine_old_and_new":
        summary_lines.append("New symbols will be merged with the existing active set and deduped.")
    elif state.universe.selection_mode == "replace_with_new":
        summary_lines.append("Only the active manifest changes; historical parquet is not deleted.")
    st.info("\n".join(summary_lines))
    _set_wizard_state(state)


def _render_refresh_step(state: SetupWizardState) -> None:
    st.subheader("Refresh and data policy")
    col1, col2 = st.columns(2)
    state.refresh.auto_refresh_market_snapshot = bool(
        col1.checkbox(
            "Auto-refresh market snapshot",
            value=state.refresh.auto_refresh_market_snapshot,
            key=_wizard_state_key("auto_refresh_market_snapshot"),
        )
    )
    state.refresh.auto_refresh_predictions = bool(
        col2.checkbox(
            "Auto-refresh predictions",
            value=state.refresh.auto_refresh_predictions,
            key=_wizard_state_key("auto_refresh_predictions"),
        )
    )
    _recommended_hint("Keep both refresh toggles on for a safe overnight loop.")
    state.refresh.loop_interval_seconds = int(
        st.number_input(
            "Loop interval (seconds)",
            min_value=60,
            value=state.refresh.loop_interval_seconds,
            step=60,
            key=_wizard_state_key("loop_interval_seconds"),
        )
    )
    _recommended_hint("300 seconds is the recommended overnight loop interval.")
    state.refresh.stale_input_behavior = st.selectbox(
        "Stale input handling",
        options=["block_trading", "warn_only", "stop_session"],
        index=["block_trading", "warn_only", "stop_session"].index(state.refresh.stale_input_behavior),
        key=_wizard_state_key("stale_input_behavior"),
        help="Block trading is the safest operational policy and remains the recommended default.",
    )

    with st.expander("Advanced refresh settings", expanded=st.session_state.get("wizard_visibility_mode") != "basic"):
        state.refresh.market_refresh_interval_seconds = int(
            st.number_input(
                "Market snapshot refresh cadence (seconds)",
                min_value=60,
                value=state.refresh.market_refresh_interval_seconds,
                step=60,
                key=_wizard_state_key("market_refresh_interval_seconds"),
            )
        )
        state.refresh.prediction_refresh_interval_seconds = int(
            st.number_input(
                "Prediction refresh cadence (seconds)",
                min_value=60,
                value=state.refresh.prediction_refresh_interval_seconds,
                step=60,
                key=_wizard_state_key("prediction_refresh_interval_seconds"),
            )
        )
        state.refresh.dataset_refresh_interval_seconds = int(
            st.number_input(
                "Dataset rebuild cadence (seconds)",
                min_value=60,
                value=state.refresh.dataset_refresh_interval_seconds,
                step=60,
                key=_wizard_state_key("dataset_refresh_interval_seconds"),
            )
        )
        state.refresh.auto_refresh_dataset = bool(
            st.checkbox(
                "Auto-refresh dataset when inference policy requires it",
                value=state.refresh.auto_refresh_dataset,
                key=_wizard_state_key("auto_refresh_dataset"),
            )
        )
        state.refresh.training_remains_separate = bool(
            st.checkbox(
                "Keep model training separate from session execution",
                value=state.refresh.training_remains_separate,
                key=_wizard_state_key("training_remains_separate"),
            )
        )
    _set_wizard_state(state)


def _render_alpha_step(state: SetupWizardState) -> None:
    st.subheader("Alpha and model policy")
    col1, col2 = st.columns(2)
    state.alpha.use_latest_trained_model = bool(
        col1.checkbox(
            "Use latest trained model",
            value=state.alpha.use_latest_trained_model,
            key=_wizard_state_key("use_latest_trained_model"),
        )
    )
    _recommended_hint("Using the latest trained model is the safest default unless you are validating a specific model artifact.")
    state.alpha.side_mode = col2.selectbox(
        "Side mode",
        options=["long_only", "short_only", "both"],
        index=["long_only", "short_only", "both"].index(state.alpha.side_mode),
        key=_wizard_state_key("side_mode"),
        help="Short availability can still be blocked by runtime shortability and broker checks.",
    )
    state.alpha.refresh_predictions_before_run = bool(
        st.checkbox(
            "Refresh predictions before run",
            value=state.alpha.refresh_predictions_before_run,
            key=_wizard_state_key("refresh_predictions_before_run"),
        )
    )
    with st.expander("Advanced alpha settings", expanded=st.session_state.get("wizard_visibility_mode") != "basic"):
        state.alpha.candidate_count = int(
            st.number_input(
                "Candidate count",
                min_value=1,
                value=state.alpha.candidate_count,
                step=1,
                key=_wizard_state_key("candidate_count"),
            )
        )
        state.alpha.long_threshold = float(
            st.number_input(
                "Long threshold",
                min_value=0.0,
                value=float(state.alpha.long_threshold),
                step=0.001,
                format="%.3f",
                key=_wizard_state_key("long_threshold"),
            )
        )
        state.alpha.short_threshold = float(
            st.number_input(
                "Short threshold",
                min_value=0.0,
                value=float(state.alpha.short_threshold),
                step=0.001,
                format="%.3f",
                key=_wizard_state_key("short_threshold"),
            )
        )
        state.alpha.model_artifact_path = st.text_input(
            "Model artifact path",
            value=state.alpha.model_artifact_path or "",
            key=_wizard_state_key("model_artifact_path"),
            help="Optional. Leave blank to keep using the canonical model artifact path.",
        ) or None
    _set_wizard_state(state)


def _render_risk_step(state: SetupWizardState) -> None:
    st.subheader("Risk controls")
    col1, col2 = st.columns(2)
    state.risk.max_positions = int(
        col1.number_input(
            "Max positions",
            min_value=1,
            value=state.risk.max_positions,
            step=1,
            key=_wizard_state_key("max_positions"),
        )
    )
    state.risk.max_dollars_per_trade = float(
        col2.number_input(
            "Max dollars per trade",
            min_value=100.0,
            value=float(state.risk.max_dollars_per_trade),
            step=100.0,
            key=_wizard_state_key("max_dollars_per_trade"),
        )
    )
    _recommended_hint("The default max dollars per trade is sized to stay conservative in paper mode.")
    state.risk.max_daily_loss_percent = float(
        col1.number_input(
            "Max daily loss %",
            min_value=0.1,
            value=float(state.risk.max_daily_loss_percent),
            step=0.1,
            key=_wizard_state_key("max_daily_loss_percent"),
        )
    )
    state.risk.same_symbol_protection = bool(
        col2.checkbox(
            "Same-symbol protection",
            value=state.risk.same_symbol_protection,
            key=_wizard_state_key("same_symbol_protection"),
        )
    )
    with st.expander("Advanced risk settings", expanded=st.session_state.get("wizard_visibility_mode") == "expert"):
        state.risk.max_positions_long = int(
            st.number_input(
                "Max long positions",
                min_value=0,
                value=state.risk.max_positions_long,
                step=1,
                key=_wizard_state_key("max_positions_long"),
            )
        )
        state.risk.max_positions_short = int(
            st.number_input(
                "Max short positions",
                min_value=0,
                value=state.risk.max_positions_short,
                step=1,
                key=_wizard_state_key("max_positions_short"),
            )
        )
        state.risk.cooldown_minutes = int(
            st.number_input(
                "Cooldown after exit (minutes)",
                min_value=0,
                value=state.risk.cooldown_minutes,
                step=5,
                key=_wizard_state_key("cooldown_minutes"),
            )
        )
        state.risk.block_foreign_manual_exposure = bool(
            st.checkbox(
                "Block foreign/manual exposure",
                value=state.risk.block_foreign_manual_exposure,
                key=_wizard_state_key("block_foreign_manual_exposure"),
            )
        )
        state.risk.shortability_gate_policy = st.selectbox(
            "Shortability gate policy",
            options=["required", "warn", "off"],
            index=["required", "warn", "off"].index(state.risk.shortability_gate_policy),
            key=_wizard_state_key("shortability_gate_policy"),
        )
        state.risk.reversal_policy = st.selectbox(
            "Reversal policy",
            options=["block", "allow_after_flatten", "allow_immediate"],
            index=["block", "allow_after_flatten", "allow_immediate"].index(state.risk.reversal_policy),
            key=_wizard_state_key("reversal_policy"),
        )
        state.risk.regime_gating_enabled = bool(
            st.checkbox(
                "Regime gating enabled",
                value=state.risk.regime_gating_enabled,
                key=_wizard_state_key("regime_gating_enabled"),
            )
        )
    _set_wizard_state(state)


def _render_execution_step(state: SetupWizardState) -> None:
    st.subheader("Execution and brackets")
    col1, col2 = st.columns(2)
    state.execution.order_type = col1.selectbox(
        "Order type",
        options=["market", "limit"],
        index=["market", "limit"].index(state.execution.order_type),
        key=_wizard_state_key("order_type"),
    )
    state.execution.bracket_enabled = bool(
        col2.checkbox(
            "Bracket enabled",
            value=state.execution.bracket_enabled,
            key=_wizard_state_key("bracket_enabled"),
        )
    )
    _recommended_hint("Keep bracket protection enabled for scalping sessions.")
    state.execution.take_profit_percent = float(
        col1.number_input(
            "Take-profit %",
            min_value=0.1,
            value=float(state.execution.take_profit_percent),
            step=0.05,
            key=_wizard_state_key("take_profit_percent"),
        )
    )
    state.execution.stop_loss_percent = float(
        col2.number_input(
            "Stop-loss %",
            min_value=0.1,
            value=float(state.execution.stop_loss_percent),
            step=0.05,
            key=_wizard_state_key("stop_loss_percent"),
        )
    )
    state.execution.sizing_mode = st.selectbox(
        "Sizing mode",
        options=["fixed_quantity", "risk_budget"],
        index=["fixed_quantity", "risk_budget"].index(state.execution.sizing_mode),
        key=_wizard_state_key("sizing_mode"),
    )
    state.execution.quantity = float(
        st.number_input(
            "Quantity",
            min_value=1.0,
            value=float(state.execution.quantity),
            step=1.0,
            key=_wizard_state_key("quantity"),
        )
    )
    with st.expander("Advanced execution settings", expanded=st.session_state.get("wizard_visibility_mode") == "expert"):
        state.execution.penny_normalization = bool(
            st.checkbox(
                "Enable penny normalization",
                value=state.execution.penny_normalization,
                key=_wizard_state_key("penny_normalization"),
            )
        )
        state.execution.market_open_only = bool(
            st.checkbox(
                "Market-open-only policy",
                value=state.execution.market_open_only,
                key=_wizard_state_key("market_open_only"),
            )
        )
        state.execution.allow_after_hours_submission = bool(
            st.checkbox(
                "Allow after-hours submission",
                value=state.execution.allow_after_hours_submission,
                key=_wizard_state_key("allow_after_hours_submission"),
            )
        )
        state.execution.smoke_order_behavior = st.selectbox(
            "Smoke submission behavior",
            options=["auto_cancel", "leave_open"],
            index=["auto_cancel", "leave_open"].index(state.execution.smoke_order_behavior),
            key=_wizard_state_key("smoke_order_behavior"),
        )
    st.caption("Long and short bracket geometry is enforced by the system automatically.")
    _set_wizard_state(state)


def _render_review_step(service: SetupWizardUIService, state: SetupWizardState) -> None:
    st.subheader("Review and start")
    review_flags = service.review_flags(state)
    generated_symbols = st.session_state.get("wizard_generated_symbols")
    preview_symbols = service.wizard_service.preview_active_symbols(
        state.model_copy(deep=True),
        generated_symbols=generated_symbols,
    )
    if state.universe.selection_mode != "keep_old" and not generated_symbols:
        st.warning(
            "No previewed liquidity universe is cached yet. Start, smoke, or save will run the liquidity flow automatically before persisting the active symbol manifest."
        )
    expected_actions = service.wizard_service.build_expected_actions(
        state,
        active_symbols=preview_symbols,
    )
    profile_col, strategy_col = st.columns(2)
    with profile_col:
        st.info(
            "\n".join(
                [
                    f"Profile: `{state.profile.profile_name}`",
                    f"Profile config: `{service.wizard_service.storage.profile_path(state.profile.profile_slug)}`",
                    f"Latest session config: `{service.wizard_service.storage.session_config_path(state.profile.profile_slug)}`",
                ]
            )
        )
    with strategy_col:
        st.info(
            "\n".join(
                [
                    f"Strategy: `{state.strategy.strategy_name}`",
                    f"Broker mode: `{state.strategy.broker_mode}`",
                    f"Session mode: `{state.strategy.session_mode}`",
                    f"Side mode: `{state.alpha.side_mode}`",
                ]
            )
        )

    universe_col, refresh_col = st.columns(2)
    with universe_col:
        st.success(
            "\n".join(
                [
                    f"Universe mode: `{state.universe.selection_mode}`",
                    f"Active symbols: `{len(preview_symbols)}`",
                    f"Active manifest: `{service.wizard_service.storage.active_symbols_path(state.profile.profile_slug)}`",
                    "Historical parquet retention: `enabled`",
                ]
            )
        )
    with refresh_col:
        st.success(
            "\n".join(
                [
                    f"Loop interval: `{state.refresh.loop_interval_seconds}` seconds",
                    f"Snapshot refresh: `{state.refresh.auto_refresh_market_snapshot}`",
                    f"Prediction refresh: `{state.refresh.auto_refresh_predictions}`",
                    f"Dataset refresh: `{state.refresh.auto_refresh_dataset}`",
                ]
            )
        )

    risk_col, exec_col = st.columns(2)
    with risk_col:
        st.write(
            {
                "max_positions": state.risk.max_positions,
                "max_dollars_per_trade": state.risk.max_dollars_per_trade,
                "max_daily_loss_percent": state.risk.max_daily_loss_percent,
                "same_symbol_protection": state.risk.same_symbol_protection,
            }
        )
    with exec_col:
        st.write(
            {
                "order_type": state.execution.order_type,
                "bracket_enabled": state.execution.bracket_enabled,
                "take_profit_percent": state.execution.take_profit_percent,
                "stop_loss_percent": state.execution.stop_loss_percent,
                "sizing_mode": state.execution.sizing_mode,
                "quantity": state.execution.quantity,
            }
        )

    st.markdown("#### Expected backend actions")
    for action in expected_actions:
        st.write(f"- {action}")

    st.markdown("#### Defaults vs customized")
    st.write({"defaults_applied": review_flags["defaults"], "customized": review_flags["customized"]})
    st.caption("Auto-save happens for profile and latest resolved session config before any launch action.")

    back_col, start_col, smoke_col, save_col = st.columns(4)
    if back_col.button("Back", key=_wizard_state_key("review_back")):
        st.session_state["wizard_step"] = max(0, st.session_state.get("wizard_step", 0) - 1)
        st.rerun()
    if start_col.button("Start session", key=_wizard_state_key("review_start")):
        result = service.start_session(state, generated_symbols=generated_symbols, smoke_only=False)
        st.session_state["wizard_last_action_result"] = result.model_dump(mode="json")
        st.success(result.message)
        st.json(st.session_state["wizard_last_action_result"])
    if smoke_col.button("Run smoke only", key=_wizard_state_key("review_smoke")):
        result = service.start_session(state, generated_symbols=generated_symbols, smoke_only=True)
        st.session_state["wizard_last_action_result"] = result.model_dump(mode="json")
        st.success(result.message)
        st.json(st.session_state["wizard_last_action_result"])
    if save_col.button("Save and exit", key=_wizard_state_key("review_save_exit")):
        result = service.save_and_exit(state, generated_symbols=generated_symbols)
        st.session_state["wizard_last_action_result"] = result.model_dump(mode="json")
        st.success(result.message)
        st.json(st.session_state["wizard_last_action_result"])


def _handle_next(service: SetupWizardUIService) -> None:
    step = st.session_state.get("wizard_step", 0)
    payload = service.get_payload()
    if step == 0:
        source_mode = st.session_state.get("wizard_profile_source_mode", "create_new")
        profile_name = st.session_state.get("wizard_profile_name", "").strip()
        existing_profile_name = st.session_state.get("wizard_existing_profile_name")
        if source_mode == "create_new" and not profile_name:
            st.error("Enter a profile name before continuing.")
            return
        if source_mode in {"load_existing", "use_last_setup"} and not existing_profile_name:
            st.error("Select an existing profile before continuing.")
            return
        try:
            state = service.initialize_wizard(
                profile_name=profile_name or existing_profile_name or "Default Profile",
                source_mode=source_mode,
                existing_profile_name=existing_profile_name,
            )
        except ValueError as exc:
            st.error(str(exc))
            return
        _set_wizard_state(state)
        st.session_state["wizard_visibility_mode"] = state.visibility_mode
        _bump_form_version()
        st.session_state["wizard_step"] = step + 1
        st.rerun()

    if step < len(STEPS) - 1:
        st.session_state["wizard_step"] = step + 1
        st.rerun()


def _handle_previous() -> None:
    step = st.session_state.get("wizard_step", 0)
    st.session_state["wizard_step"] = max(0, step - 1)
    st.rerun()


platform_service = get_platform_service()
wizard_service = SetupWizardUIService(platform_service)
payload = wizard_service.get_payload()

st.title("Setup Wizard")
st.caption("Guided, default-first configuration for a new trading session. The current dashboard and CLI workflows remain unchanged.")

if hasattr(st, "page_link"):
    st.page_link("app.py", label="Back to landing page")

st.info(
    "Recommended new setup flow: profiles and resolved session configs are auto-saved under repo-local paths, "
    "and historical downloaded data is retained even when your active symbol set changes."
)

visibility_mode = st.radio(
    "Wizard visibility mode",
    options=["basic", "advanced", "expert"],
    horizontal=True,
    index=["basic", "advanced", "expert"].index(st.session_state.get("wizard_visibility_mode", "basic")),
    key="wizard_visibility_mode_selector",
)
st.session_state["wizard_visibility_mode"] = visibility_mode

current_step = st.session_state.get("wizard_step", 0)
_step_navigation(step=current_step)

state = _wizard_state()
if current_step == 0:
    _render_profile_step(wizard_service, payload)
elif state is None:
    st.warning("Start with Step 1 to create or load a profile.")
    st.session_state["wizard_step"] = 0
    st.stop()
else:
    state.visibility_mode = visibility_mode
    if current_step == 1:
        _render_strategy_step(wizard_service, payload, state)
    elif current_step == 2:
        _render_universe_step(wizard_service, state)
    elif current_step == 3:
        _render_refresh_step(state)
    elif current_step == 4:
        _render_alpha_step(state)
    elif current_step == 5:
        _render_risk_step(state)
    elif current_step == 6:
        _render_execution_step(state)
    elif current_step == 7:
        _render_review_step(wizard_service, state)

if current_step < len(STEPS) - 1:
    left, right = st.columns([1, 1])
    left.button(
        "Previous",
        on_click=_handle_previous,
        disabled=current_step == 0,
        key=_wizard_state_key("previous_button"),
    )
    right.button(
        "Next",
        on_click=lambda: _handle_next(wizard_service),
        key=_wizard_state_key("next_button"),
    )

if "wizard_last_action_result" in st.session_state and current_step != 7:
    st.subheader("Latest wizard action")
    st.json(st.session_state["wizard_last_action_result"])
