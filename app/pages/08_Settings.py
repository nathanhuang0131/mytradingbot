from __future__ import annotations

import sys
from pathlib import Path

import streamlit as st

APP_DIR = Path(__file__).resolve().parents[1]
if str(APP_DIR) not in sys.path:
    sys.path.insert(0, str(APP_DIR))

from components.runtime import get_platform_service
from mytradingbot.ui_services.settings import SettingsService

payload = SettingsService(get_platform_service().settings).get_settings_payload()

st.title("Settings")
st.caption("Current application settings and resolved repository paths.")
st.json(payload)
