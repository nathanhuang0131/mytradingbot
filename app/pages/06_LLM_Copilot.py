from __future__ import annotations

import sys
from pathlib import Path

import streamlit as st

APP_DIR = Path(__file__).resolve().parents[1]
if str(APP_DIR) not in sys.path:
    sys.path.insert(0, str(APP_DIR))

from components.runtime import get_platform_service
from mytradingbot.ui_services.llm_copilot import LLMCopilotService

service = LLMCopilotService(get_platform_service())

st.title("LLM Copilot")
st.caption("Advisory-only explanations and summaries grounded in recorded artifacts.")

explanation = service.explain_last_attempt()
summary = service.summarize_last_session()

if explanation is None and summary is None:
    st.info("Run a paper or dry-run session first to unlock advisory outputs.")
else:
    if explanation is not None:
        st.subheader("Signal Explanation")
        st.json(explanation.model_dump(mode="json"))
    if summary is not None:
        st.subheader("Diagnostics Summary")
        st.json(summary.model_dump(mode="json"))
