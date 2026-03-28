from __future__ import annotations

import sys
from pathlib import Path

import streamlit as st

APP_DIR = Path(__file__).resolve().parents[1]
if str(APP_DIR) not in sys.path:
    sys.path.insert(0, str(APP_DIR))

from components.descriptive_sections import render_descriptive_section, render_trading_track
from components.runtime import (
    get_platform_service,
    get_selected_profile_name,
    set_selected_profile_name,
)
from mytradingbot.ui_services.status_reference import StatusReferenceService

platform_service = get_platform_service()
service = StatusReferenceService(platform_service)
initial_payload = service.get_payload(profile_name=get_selected_profile_name())

st.title("Status Reference")
st.caption(
    "Readable summary of the selected profile, its saved runtime settings, current artifact readiness, and recent trading activity."
)

if not initial_payload.profile_names:
    st.info(
        "No saved profiles are available yet. Use the Setup Wizard first to create a profile, then return here to review its status."
    )
    st.stop()

profile_name = st.selectbox(
    "Profile",
    options=initial_payload.profile_names,
    index=initial_payload.profile_names.index(
        initial_payload.selected_profile_name or initial_payload.profile_names[0]
    ),
)
set_selected_profile_name(profile_name)
payload = service.get_payload(profile_name=profile_name)

left, right = st.columns(2)
for index, section in enumerate(payload.sections):
    with left if index % 2 == 0 else right:
        render_descriptive_section(section)

render_trading_track(payload.trading_track)
