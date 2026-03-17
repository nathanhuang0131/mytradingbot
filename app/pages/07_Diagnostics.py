from __future__ import annotations

import streamlit as st

from app.components.runtime import get_platform_service
from mytradingbot.ui_services.diagnostics import DiagnosticsPageService

payload = DiagnosticsPageService(get_platform_service()).get_payload()

st.title("Diagnostics")
st.caption("Prediction health, no-trade analysis, and post-session review notes.")
st.json(payload.model_dump(mode="json"))
