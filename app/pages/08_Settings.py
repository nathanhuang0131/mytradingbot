from __future__ import annotations

import streamlit as st

from app.components.runtime import get_platform_service
from mytradingbot.ui_services.settings import SettingsService

payload = SettingsService(get_platform_service().settings).get_settings_payload()

st.title("Settings")
st.caption("Current application settings and resolved repository paths.")
st.json(payload)
