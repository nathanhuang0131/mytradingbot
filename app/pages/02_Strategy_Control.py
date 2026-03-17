from __future__ import annotations

import streamlit as st

from app.components.runtime import (
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
st.json(
    {
        "strategy": strategy,
        "mode": mode,
        "live_trading_enabled": payload.live_trading_enabled,
    }
)
