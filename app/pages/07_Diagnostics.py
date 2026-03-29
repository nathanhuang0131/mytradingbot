from __future__ import annotations

import sys
from pathlib import Path

import streamlit as st

APP_DIR = Path(__file__).resolve().parents[1]
if str(APP_DIR) not in sys.path:
    sys.path.insert(0, str(APP_DIR))

from components.runtime import get_platform_service
from mytradingbot.ui_services.diagnostics import DiagnosticsPageService

payload = DiagnosticsPageService(get_platform_service()).get_payload()

st.title("Diagnostics")
st.caption("Prediction health, no-trade analysis, and post-session review notes.")
st.json(payload.model_dump(mode="json"))
