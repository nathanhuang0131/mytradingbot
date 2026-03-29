from __future__ import annotations

import sys
from pathlib import Path

import pandas as pd
import streamlit as st

APP_DIR = Path(__file__).resolve().parents[1]
if str(APP_DIR) not in sys.path:
    sys.path.insert(0, str(APP_DIR))

from components.runtime import get_platform_service, get_selected_strategy
from mytradingbot.ui_services.data_training import DataTrainingService
from mytradingbot.ui_services.market_data_progress import MarketDataProgressPayload


def _parse_symbols(text: str) -> list[str] | None:
    symbols = [part.strip().upper() for part in text.replace(",", " ").split() if part.strip()]
    return symbols or None


def _resolve_action_symbol_inputs(
    *,
    manual_symbols: list[str] | None,
    universe_source,
) -> tuple[list[str] | None, Path | None]:
    if manual_symbols:
        return manual_symbols, None
    if universe_source.is_ready:
        return None, Path(universe_source.selected_universe_file_path)
    return None, None


def _render_result(result_key: str) -> None:
    payload = st.session_state.get(result_key)
    if payload is not None:
        st.json(payload)


def _run_action(result_key: str, action) -> None:
    st.session_state[result_key] = action().model_dump(mode="json")


def _requested_symbols_for_progress(
    *,
    manual_symbols: list[str] | None,
    universe_source,
) -> list[str]:
    if manual_symbols:
        return manual_symbols
    return list(universe_source.symbols)


def _render_market_data_progress(
    container,
    progress: MarketDataProgressPayload | None,
) -> None:
    with container.container():
        st.subheader("Market Data Progress")
        if progress is None:
            st.info("Start a download or update run to see live timeframe progress here.")
            return

        total_steps = len(progress.completed_steps) + len(progress.remaining_steps)
        completion_ratio = (
            len(progress.completed_steps) / total_steps if total_steps else 0.0
        )
        st.progress(completion_ratio, text=progress.current_step)
        metric_left, metric_middle, metric_right, metric_far_right = st.columns(4)
        metric_left.metric("Operation", progress.operation.title())
        metric_middle.metric("Status", progress.status.replace("_", " ").title())
        metric_right.metric("Requested Symbols", progress.requested_symbol_count)
        metric_far_right.metric("Timeframes", len(progress.requested_timeframes))

        st.caption(
            f"Current step: `{progress.current_step}`  \n"
            f"Started: `{progress.started_at}`  \n"
            f"Last update: `{progress.updated_at}`"
        )

        st.markdown("**Per-Timeframe Progress**")
        timeframe_rows = [
            {
                "Timeframe": row.timeframe,
                "Status": row.status,
                "Stage": row.stage,
                "Requested Symbols": row.symbols_requested,
                "Symbols With Data": row.symbols_with_data,
                "Symbols Without Data": row.symbols_without_data,
                "Rows Downloaded": row.rows_downloaded,
                "Raw Folder": row.raw_folder,
                "Normalized Folder": row.normalized_folder,
                "Resolved Start": row.resolved_start_at,
                "Resolved End": row.resolved_end_at,
            }
            for row in progress.timeframe_progress
        ]
        st.dataframe(pd.DataFrame(timeframe_rows), use_container_width=True, hide_index=True)

        steps_left, steps_right = st.columns(2)
        with steps_left:
            st.markdown("**Remaining Steps**")
            if progress.remaining_steps:
                st.write(pd.DataFrame({"Step": progress.remaining_steps}))
            else:
                st.success("No remaining steps.")
        with steps_right:
            st.markdown("**Completed Steps**")
            if progress.completed_steps:
                st.write(pd.DataFrame({"Step": progress.completed_steps}))
            else:
                st.info("No completed steps yet.")

        st.markdown("**Output Paths**")
        st.write(
            {
                "raw_output_root": progress.raw_output_root,
                "normalized_output_root": progress.normalized_output_root,
                "snapshot_output_path": progress.snapshot_output_path,
            }
        )


platform_service = get_platform_service()
service = DataTrainingService(platform_service)
payload = service.get_payload()
strategy = get_selected_strategy() or payload.default_strategy

st.title("Data Management")
st.caption(
    "Run real repo-local liquidity, market data, qlib dataset, training, and prediction workflows from one maintenance surface."
)

settings_col, capability_col = st.columns([2, 1])
with settings_col:
    strategy = st.selectbox(
        "Strategy",
        options=platform_service.get_strategy_names(),
        index=platform_service.get_strategy_names().index(strategy),
    )
    if payload.profile_names:
        selected_profile_name = st.selectbox(
            "Profile",
            options=payload.profile_names,
            index=payload.profile_names.index(payload.default_profile_name or payload.profile_names[0]),
            help="The selected profile controls the default active-universe file used by the maintenance actions below.",
        )
    else:
        selected_profile_name = None
        st.info("No saved profile was found yet. Create one in the Setup Wizard or point this page at a custom universe file.")
    default_universe_source = service.resolve_universe_source(profile_name=selected_profile_name)
    universe_file_key = f"data_mgmt_universe_file_path_{selected_profile_name or 'default'}"
    if universe_file_key not in st.session_state:
        st.session_state[universe_file_key] = default_universe_source.default_universe_file_path
    universe_file_path = st.text_input(
        "Universe file path",
        key=universe_file_key,
        help="JSON and CSV symbol files are supported. By default this uses the selected profile's active-universe manifest.",
    )
    universe_source = service.resolve_universe_source(
        profile_name=selected_profile_name,
        universe_file_path=universe_file_path,
    )
    st.caption(
        "Default profile universe: "
        f"`{universe_source.default_universe_file_path}`  \n"
        "Typical profile file pattern: "
        "`data/runtime/active_universes/<profile>_active_symbols.json`  \n"
        "Alternate standard file: "
        f"`{universe_source.alternate_universe_file_path}`"
    )
    if universe_source.validation_message:
        st.warning(universe_source.validation_message)
    else:
        st.success(
            f"Loaded {universe_source.symbol_count} symbols from `{universe_source.selected_universe_file_path}`."
        )
        if universe_source.symbols:
            preview = ", ".join(universe_source.symbols[:20])
            st.code(preview + (" ..." if universe_source.symbol_count > 20 else ""))
    selected_timeframes = st.multiselect(
        "Timeframes",
        options=payload.default_timeframes,
        default=payload.default_timeframes,
        help="Used for market data download and update actions.",
    )
    symbols_text = st.text_area(
        "Optional manual symbol override",
        help="Leave blank to use the universe file above. Enter symbols separated by spaces, commas, or new lines to override the file for the current action run.",
    )
    selected_symbols = _parse_symbols(symbols_text)
    if selected_symbols:
        st.caption("Manual symbols override the universe file for the action buttons below.")
with capability_col:
    st.subheader("Capabilities")
    st.json(payload.capabilities.model_dump(mode="json"))

st.subheader("Availability Notes")
left, right = st.columns(2)
left.write({"works_without_pyqlib": payload.works_without_pyqlib})
right.write({"works_without_alpaca_credentials": payload.works_without_alpaca_credentials})

resolved_symbols, resolved_symbols_file = _resolve_action_symbol_inputs(
    manual_symbols=selected_symbols,
    universe_source=universe_source,
)
file_scoped_action_disabled = resolved_symbols is None and resolved_symbols_file is None

universe_tab, market_data_tab, qlib_tab, training_tab = st.tabs(
    [
        "Liquidity Universe",
        "Market Data",
        "Qlib Dataset",
        "Training & Predictions",
    ]
)

with universe_tab:
    st.write("Generate the ranked top-liquidity universe used by the rest of the maintenance flow.")
    if st.button("Generate Top Liquidity Universe", key="data_mgmt_generate_top_liquidity_universe"):
        _run_action(
            "data_mgmt_generate_top_liquidity_universe_result",
            lambda: service.generate_top_liquidity_universe(),
        )
    _render_result("data_mgmt_generate_top_liquidity_universe_result")

with market_data_tab:
    st.write("Download a full refresh or run an incremental update against the repo-local market data pipeline.")
    market_progress_placeholder = st.empty()
    _render_market_data_progress(
        market_progress_placeholder,
        service.get_market_data_progress(),
    )
    market_left, market_right = st.columns(2)
    if market_left.button(
        "Download Market Data",
        key="data_mgmt_download_market_data",
        disabled=file_scoped_action_disabled,
    ):
        requested_symbols = _requested_symbols_for_progress(
            manual_symbols=selected_symbols,
            universe_source=universe_source,
        )
        tracker = service.create_market_data_progress_tracker(
            operation="download",
            requested_symbols=requested_symbols,
            requested_timeframes=selected_timeframes or payload.default_timeframes,
            on_update=lambda current: _render_market_data_progress(
                market_progress_placeholder,
                current,
            ),
        )
        result = service.download_market_data(
            symbols=resolved_symbols,
            symbols_file=resolved_symbols_file,
            timeframes=selected_timeframes or None,
            progress_callback=tracker.handle_event,
        )
        tracker.finalize(result)
        st.session_state["data_mgmt_download_market_data_result"] = result.model_dump(mode="json")
    if market_right.button(
        "Update Market Data",
        key="data_mgmt_update_market_data",
        disabled=file_scoped_action_disabled,
    ):
        requested_symbols = _requested_symbols_for_progress(
            manual_symbols=selected_symbols,
            universe_source=universe_source,
        )
        tracker = service.create_market_data_progress_tracker(
            operation="update",
            requested_symbols=requested_symbols,
            requested_timeframes=selected_timeframes or payload.default_timeframes,
            on_update=lambda current: _render_market_data_progress(
                market_progress_placeholder,
                current,
            ),
        )
        result = service.update_market_data(
            symbols=resolved_symbols,
            symbols_file=resolved_symbols_file,
            timeframes=selected_timeframes or None,
            progress_callback=tracker.handle_event,
        )
        tracker.finalize(result)
        st.session_state["data_mgmt_update_market_data_result"] = result.model_dump(mode="json")
    with st.expander("Latest market-data raw result", expanded=False):
        _render_result("data_mgmt_download_market_data_result")
        _render_result("data_mgmt_update_market_data_result")

with qlib_tab:
    st.write("Build the qlib dataset artifact and run training-data quality checks from the current repo-local data.")
    qlib_left, qlib_right = st.columns(2)
    if qlib_left.button(
        "Build Dataset",
        key="data_mgmt_build_dataset",
        disabled=file_scoped_action_disabled,
    ):
        _run_action(
            "data_mgmt_build_dataset_result",
            lambda: service.build_dataset(
                strategy_name=strategy,
                symbols=resolved_symbols,
                symbols_file=resolved_symbols_file,
            ),
        )
    if qlib_right.button(
        "Check Training Data Quality",
        key="data_mgmt_check_training_data_quality",
        disabled=file_scoped_action_disabled,
    ):
        _run_action(
            "data_mgmt_check_training_data_quality_result",
            lambda: service.check_training_data_quality(
                strategy_name=strategy,
                symbols=resolved_symbols,
                symbols_file=resolved_symbols_file,
                timeframes=selected_timeframes or None,
            ),
        )
    _render_result("data_mgmt_build_dataset_result")
    _render_result("data_mgmt_check_training_data_quality_result")

with training_tab:
    st.write("Train qlib models, refresh predictions, or run the full alpha-robust training workflow.")
    top_row_left, top_row_middle, top_row_right = st.columns(3)
    if top_row_left.button("Train Models", key="data_mgmt_train_models"):
        _run_action(
            "data_mgmt_train_models_result",
            lambda: service.train_models(strategy_name=strategy),
        )
    if top_row_middle.button("Refresh Predictions", key="data_mgmt_refresh_predictions"):
        _run_action(
            "data_mgmt_refresh_predictions_result",
            lambda: service.refresh_predictions(strategy_name=strategy),
        )
    if top_row_right.button(
        "Run Alpha Robust Training",
        key="data_mgmt_run_alpha_robust_training",
        disabled=file_scoped_action_disabled,
    ):
        _run_action(
            "data_mgmt_run_alpha_robust_training_result",
            lambda: service.run_alpha_robust_training(
                strategy_name=strategy,
                symbols=resolved_symbols,
                symbols_file=resolved_symbols_file,
                timeframes=selected_timeframes or None,
            ),
        )
    _render_result("data_mgmt_train_models_result")
    _render_result("data_mgmt_refresh_predictions_result")
    _render_result("data_mgmt_run_alpha_robust_training_result")
