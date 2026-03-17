from __future__ import annotations

import streamlit as st

from app.components.runtime import get_platform_service
from mytradingbot.ui_services.dashboard import DashboardService

st.set_page_config(page_title="MyTradingBot Next", layout="wide")

platform_service = get_platform_service()
payload = DashboardService(platform_service).get_dashboard_payload()

st.title("MyTradingBot Next")
st.caption("Qlib-first, dashboard-first quant trading platform")

left, right = st.columns(2)
left.metric("Prediction Ready", "Yes" if payload.prediction_status.is_ready else "No")
left.metric("Strategies", len(payload.available_strategies))
right.metric("Platform Health", "Healthy" if payload.health.ok else "Attention")
right.metric("Default Mode", platform_service.settings.runtime.default_mode.value)

st.subheader("Operator Notes")
st.write(
    "Use the pages in the sidebar to control strategies, run paper sessions, inspect diagnostics, and review advisory summaries."
)
if not payload.prediction_status.is_ready:
    st.warning(
        "Predictions are not currently ready. Qlib-dependent actions fail clearly, but the dashboard remains available."
    )
