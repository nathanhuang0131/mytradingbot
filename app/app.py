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
if hasattr(st, "page_link"):
    st.page_link("pages/00_Setup_Wizard.py", label="Start New Trading Session (Wizard)")
else:
    st.info("Open `00_Setup_Wizard` from the sidebar to use the guided setup flow.")
st.subheader("Phase Capability Snapshot")
st.json(payload.capabilities.model_dump(mode="json"))
if not payload.prediction_status.is_ready:
    st.warning(
        "Predictions are not currently ready. Qlib-dependent actions fail clearly, but the dashboard remains available."
    )
