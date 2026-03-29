from __future__ import annotations

import sys
from pathlib import Path

import streamlit as st

APP_DIR = Path(__file__).resolve().parents[1]
if str(APP_DIR) not in sys.path:
    sys.path.insert(0, str(APP_DIR))

from components.runtime import (
    get_platform_service,
    get_selected_profile_name,
    get_selected_strategy,
    set_selected_profile_name,
)
from mytradingbot.ui_services.trading_universe import TradingUniverseUIService


def _symbol_rows(symbols: list[str]) -> list[dict[str, str]]:
    return [{"symbol": symbol} for symbol in symbols]


service = TradingUniverseUIService(get_platform_service())
payload = service.get_payload()

st.title("Trading Universe")
st.caption(
    "Review the final profile-scoped trading universe before a scalping run, compare it with the last saved manifest, and persist manual additions for future runs."
)

selected_strategy = get_selected_strategy()
if selected_strategy != "scalping":
    st.warning(
        f"The currently selected strategy is '{selected_strategy}'. This page is designed for the scalping workflow, but saved universe changes remain profile-scoped."
    )

if not payload.profile_names:
    st.info(
        "No saved profiles were found yet. Use the Setup Wizard first to create a profile, then return here to manage its final trading universe."
    )
    st.stop()

profile_name = st.selectbox(
    "Profile",
    options=payload.profile_names,
    index=payload.profile_names.index(
        get_selected_profile_name()
        if get_selected_profile_name() in payload.profile_names
        else (payload.default_profile_name or payload.profile_names[0])
    ),
)
set_selected_profile_name(profile_name)
selection_mode = st.radio(
    "Final trading universe mode",
    options=payload.selection_modes,
    horizontal=True,
    format_func=lambda value: {
        "keep_old": "Keep old trading universe",
        "combine_old_and_new": "Combine old and new trading universe",
        "only_new": "Only new trading universe",
    }[value],
)

left, right = st.columns(2)
target_symbol_count = int(
    left.number_input("Target symbol count", min_value=1, value=100, step=10)
)
min_price = float(right.number_input("Minimum price", min_value=1.0, value=15.0, step=1.0))
min_average_volume = int(
    left.number_input(
        "Minimum average volume",
        min_value=1_000,
        value=500_000,
        step=50_000,
    )
)
include_etfs = bool(right.checkbox("Include ETFs", value=False))
manual_symbols_text = st.text_area(
    "Additional symbols to monitor and trade",
    help="Enter symbols separated by commas, spaces, or new lines. These symbols become part of the saved active universe for future runs.",
)

preview_disabled = selection_mode != "keep_old" and not profile_name
if st.button("Preview Final Trading Universe", disabled=preview_disabled):
    preview = service.preview_universe(
        profile_name=profile_name,
        selection_mode=selection_mode,
        manual_symbols_text=manual_symbols_text,
        target_symbol_count=target_symbol_count,
        min_price=min_price,
        min_average_volume=min_average_volume,
        include_etfs=include_etfs,
    )
    st.session_state["trading_universe_preview"] = preview.model_dump(mode="json")

preview_payload = st.session_state.get("trading_universe_preview")
if preview_payload:
    metric_one, metric_two, metric_three, metric_four = st.columns(4)
    metric_one.metric("Total Final Symbols", int(preview_payload["final_symbol_count"]))
    metric_two.metric("Reduced From Last Universe", int(preview_payload["removed_symbol_count"]))
    metric_three.metric("Added From Last Universe", int(preview_payload["added_symbol_count"]))
    metric_four.metric("Manual Additions", len(preview_payload["manual_symbols"]))

    previous_col, final_col = st.columns(2)
    with previous_col:
        st.subheader("Last Trading Universe")
        st.dataframe(_symbol_rows(preview_payload["previous_symbols"]), use_container_width=True)
    with final_col:
        st.subheader("Final Trading Universe")
        st.dataframe(_symbol_rows(preview_payload["final_symbols"]), use_container_width=True)

    added_col, removed_col = st.columns(2)
    with added_col:
        st.subheader("Added Symbols")
        st.dataframe(_symbol_rows(preview_payload["added_symbols"]), use_container_width=True)
    with removed_col:
        st.subheader("Removed Symbols")
        st.dataframe(_symbol_rows(preview_payload["removed_symbols"]), use_container_width=True)

    st.subheader("Generated New Universe")
    st.dataframe(_symbol_rows(preview_payload["generated_symbols"]), use_container_width=True)

    qlib_view_mode = st.radio(
        "Qlib prediction table view",
        options=["raw", "final"],
        horizontal=True,
        format_func=lambda value: {
            "raw": "Raw qlib prediction artifacts",
            "final": "Final qlib trading universe",
        }[value],
    )
    st.caption(
        "`is_final_symbol` follows the current scalping final-universe implementation on this page. `indicated_tp_pct` and `indicated_sl_pct` come from the existing scalping target logic without changing its rules."
    )
    try:
        qlib_rows = service.get_qlib_prediction_rows(
            profile_name=profile_name,
            selection_mode=selection_mode,
            generated_symbols=preview_payload["generated_symbols"],
            manual_symbols_text=" ".join(preview_payload["manual_symbols"]),
            target_symbol_count=target_symbol_count,
            min_price=min_price,
            min_average_volume=min_average_volume,
            include_etfs=include_etfs,
            view_mode=qlib_view_mode,
        )
    except ValueError as exc:
        st.warning(str(exc))
    else:
        st.subheader("Qlib Predictions")
        if qlib_rows:
            st.dataframe(qlib_rows, use_container_width=True)
        else:
            st.info("No qlib prediction artifact is available for the selected view yet.")

    if st.button("Save Final Trading Universe", type="primary"):
        result = service.save_universe(
            profile_name=profile_name,
            selection_mode=selection_mode,
            generated_symbols=preview_payload["generated_symbols"],
            manual_symbols_text=manual_symbols_text,
            target_symbol_count=target_symbol_count,
            min_price=min_price,
            min_average_volume=min_average_volume,
            include_etfs=include_etfs,
        )
        st.success(f"Saved {len(result.final_symbols)} symbols to the active trading universe.")
        st.markdown(f"**Active universe file:** {result.active_symbols_path}")
        if result.latest_session_config_path:
            st.markdown(
                f"**Latest session config updated:** {result.latest_session_config_path}"
            )
        st.caption(
            "The saved final universe becomes the profile-scoped active symbol manifest for future session runs."
        )
