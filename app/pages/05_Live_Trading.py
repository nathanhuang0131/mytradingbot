from __future__ import annotations

import streamlit as st

from app.components.runtime import get_platform_service
from mytradingbot.ui_services.live_trading import LiveTradingService

payload = LiveTradingService(get_platform_service()).get_payload()

st.title("Live Trading")
st.caption("Visible gated scaffold for future live trading support.")
st.error(payload.message)
st.json(payload.model_dump(mode="json"))
