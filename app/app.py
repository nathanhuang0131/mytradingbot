from __future__ import annotations

import sys
from pathlib import Path

import streamlit as st

APP_DIR = Path(__file__).resolve().parent
if str(APP_DIR) not in sys.path:
    sys.path.insert(0, str(APP_DIR))

from components.descriptive_sections import render_descriptive_section
from components.runtime import get_platform_service
from mytradingbot.ui_services.dashboard import DashboardService

st.set_page_config(page_title="Dashboard Summary", layout="wide")

platform_service = get_platform_service()
payload = DashboardService(platform_service).get_dashboard_payload()

st.title("Dashboard Summary")
st.caption("Readable overview of system readiness, qlib capability status, and the next operator actions to take.")

left, right = st.columns(2)
left.metric("Prediction Ready", "Yes" if payload.prediction_status.is_ready else "No")
left.metric("Strategies", len(payload.available_strategies))
right.metric("Platform Health", "Healthy" if payload.health.ok else "Attention")
right.metric("Default Mode", platform_service.settings.runtime.default_mode.value)

st.subheader("Operator Notes")
st.write(
    "Use the Setup Wizard to launch trading sessions, then use the sidebar pages to inspect profile status, diagnostics, training readiness, and advisory summaries."
)
if hasattr(st, "page_link"):
    st.page_link("pages/00_Setup_Wizard.py", label="Start New Trading Session (Wizard)")
else:
    st.info("Open `00_Setup_Wizard` from the sidebar to use the guided setup flow.")
for section in payload.summary_sections:
    render_descriptive_section(section)
if not payload.prediction_status.is_ready:
    st.warning(
        "Predictions are not currently ready. Qlib-dependent actions fail clearly, but the dashboard remains available."
    )
