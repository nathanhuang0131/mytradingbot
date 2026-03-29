from __future__ import annotations

import sys
from pathlib import Path

import streamlit as st

APP_DIR = Path(__file__).resolve().parents[1]
if str(APP_DIR) not in sys.path:
    sys.path.insert(0, str(APP_DIR))

from components.runtime import (
    get_platform_service,
    get_selected_mode,
    get_selected_strategy,
    set_selected_mode,
    set_selected_strategy,
)
from mytradingbot.ui_services.strategy_control import StrategyControlService

platform_service = get_platform_service()
payload = StrategyControlService(platform_service).get_control_payload()

st.title("Strategy Control")
st.caption("Choose the active strategy and runtime mode.")

strategy = st.selectbox(
    "Strategy",
    options=payload.available_strategies,
    index=payload.available_strategies.index(get_selected_strategy()),
)
mode = st.selectbox(
    "Mode",
    options=payload.available_modes,
    index=payload.available_modes.index(get_selected_mode()),
)

set_selected_strategy(strategy)
set_selected_mode(mode)

st.write("Current selection")
st.markdown(f"**Strategy:** {strategy}")
st.caption("This selects which strategy logic and thresholds the app treats as active on pages that follow the shared strategy state.")
st.markdown(f"**Mode:** {mode}")
st.caption("This is the currently selected runtime mode for UI pages that respect the shared execution mode.")
st.markdown(f"**Live trading enabled in config:** {'Yes' if payload.live_trading_enabled else 'No'}")
st.caption("This shows whether the repo configuration currently allows the live-trading path to be enabled at all.")
