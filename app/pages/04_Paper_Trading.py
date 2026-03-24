from __future__ import annotations

import sys
from pathlib import Path

import streamlit as st

APP_DIR = Path(__file__).resolve().parents[1]
if str(APP_DIR) not in sys.path:
    sys.path.insert(0, str(APP_DIR))

from components.runtime import get_platform_service, get_selected_mode, get_selected_strategy
from mytradingbot.ui_services.paper_trading import PaperTradingService

platform_service = get_platform_service()
service = PaperTradingService(platform_service)

st.title("Paper Trading")
st.caption("Run dry-run or paper sessions and inspect resulting artifacts.")

strategy = get_selected_strategy()
mode = get_selected_mode()
if mode == "live":
    st.warning("Live mode is not allowed from the Paper Trading page. Switch to dry_run or paper.")
else:
    st.write({"strategy": strategy, "mode": mode})
    if st.button("Run Session"):
        result = service.run_session(strategy_name=strategy, mode=mode)
        st.subheader("Session Summary")
        st.json(result.session_summary.model_dump(mode="json"))
        st.subheader("Orders")
        st.json([order.model_dump(mode="json") for order in result.orders])
        st.subheader("Positions")
        st.json([position.model_dump(mode="json") for position in result.positions])
        st.subheader("Trade Attempts")
        st.json([attempt.model_dump(mode="json") for attempt in result.trade_attempts])
