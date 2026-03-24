from __future__ import annotations

import streamlit as st

from app.components.runtime import get_platform_service
from mytradingbot.ui_services.dashboard import DashboardService

platform_service = get_platform_service()
payload = DashboardService(platform_service).get_dashboard_payload()

st.title("Dashboard")
st.caption("System health, prediction freshness, and recent session status.")

col1, col2, col3 = st.columns(3)
col1.metric("Prediction Ready", "Yes" if payload.prediction_status.is_ready else "No")
col2.metric("Platform Health", "Healthy" if payload.health.ok else "Attention")
col3.metric("Strategies", len(payload.available_strategies))

st.subheader("Prediction Status")
st.json(payload.prediction_status.model_dump(mode="json"))

st.subheader("Health")
st.json(payload.health.model_dump(mode="json"))

st.subheader("Phase Capabilities")
st.json(payload.capabilities.model_dump(mode="json"))

if hasattr(st, "page_link"):
    st.page_link("pages/00_Setup_Wizard.py", label="Start New Trading Session (Wizard)")
else:
    st.info("Open `00_Setup_Wizard` from the sidebar to use the guided setup flow.")

if payload.last_session is not None:
    st.subheader("Last Session")
    st.json(payload.last_session.model_dump(mode="json"))
