"""Shared Streamlit session helpers for UI pages."""

from __future__ import annotations

import streamlit as st

from mytradingbot.orchestration.service import TradingPlatformService


def get_platform_service() -> TradingPlatformService:
    """Return a shared platform service stored in Streamlit session state."""

    if "platform_service" not in st.session_state:
        st.session_state["platform_service"] = TradingPlatformService.bootstrap_default()
    return st.session_state["platform_service"]


def get_selected_strategy() -> str:
    return st.session_state.get("selected_strategy", "scalping")


def set_selected_strategy(strategy_name: str) -> None:
    st.session_state["selected_strategy"] = strategy_name


def get_selected_mode() -> str:
    return st.session_state.get("selected_mode", "paper")


def set_selected_mode(mode: str) -> None:
    st.session_state["selected_mode"] = mode


def get_selected_profile_name() -> str | None:
    return st.session_state.get("selected_profile_name")


def set_selected_profile_name(profile_name: str | None) -> None:
    if profile_name is None:
        st.session_state.pop("selected_profile_name", None)
        return
    st.session_state["selected_profile_name"] = profile_name
