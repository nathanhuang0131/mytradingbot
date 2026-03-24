from __future__ import annotations

import sys
from pathlib import Path

import streamlit as st

APP_DIR = Path(__file__).resolve().parents[1]
if str(APP_DIR) not in sys.path:
    sys.path.insert(0, str(APP_DIR))

from components.runtime import get_platform_service
from mytradingbot.ui_services.live_trading import LiveTradingService

service = LiveTradingService(get_platform_service())
payload = service.get_payload()

st.title("Live Trading")
st.caption("Live trading remains explicitly gated. This page also shows operator-facing updates for managed background sessions.")

if payload.enabled:
    st.success(payload.message)
else:
    st.warning(payload.message)

refresh_col, summary_col = st.columns([1, 3])
with refresh_col:
    if st.button("Refresh Session View", use_container_width=True):
        st.rerun()
with summary_col:
    st.info(
        f"Detected {len(payload.running_sessions)} PID-managed session(s). "
        "Open a session dialog to inspect recent backend updates or terminate the run."
    )


@st.dialog("Running Session Updates")
def show_session_updates(session_payload: dict) -> None:
    st.caption("Recent backend output for the selected managed session.")
    status = "Running" if session_payload["is_running"] else "Stopped"
    st.markdown(
        f"**Profile:** `{session_payload['profile_name']}`  \n"
        f"**PID:** `{session_payload['pid']}`  \n"
        f"**Status:** `{status}`  \n"
        f"**Strategy:** `{session_payload.get('strategy_name') or 'unknown'}`  \n"
        f"**Broker mode:** `{session_payload.get('broker_mode') or 'unknown'}`  \n"
        f"**Session mode:** `{session_payload.get('session_mode') or 'unknown'}`  \n"
        f"**Active symbols:** `{session_payload.get('active_symbol_count') or 'unknown'}`"
    )
    if session_payload.get("session_config_path"):
        st.code(session_payload["session_config_path"], language="text")
    if session_payload.get("latest_session_report_path"):
        st.caption(f"Latest session report: {session_payload['latest_session_report_path']}")
    if session_payload.get("latest_decision_audit_path"):
        st.caption(f"Latest decision audit: {session_payload['latest_decision_audit_path']}")

    st.subheader("Profile Stderr Tail")
    st.code(
        "\n".join(session_payload.get("stderr_log_tail") or ["No stderr output recorded."]),
        language="text",
    )

    st.subheader("Profile Stdout Tail")
    st.code(
        "\n".join(session_payload.get("stdout_log_tail") or ["No stdout output recorded."]),
        language="text",
    )

    st.subheader("Shared Loop Log Tail")
    st.code(
        "\n".join(
            session_payload.get("shared_loop_log_tail")
            or ["No shared loop log output recorded."]
        ),
        language="text",
    )


if not payload.running_sessions:
    st.info("No PID-managed wizard sessions are currently detected.")
else:
    for session in payload.running_sessions:
        with st.container(border=True):
            top_col, meta_col, action_col = st.columns([2, 2, 2])
            top_col.subheader(session.profile_name)
            top_col.caption(
                f"strategy={session.strategy_name or 'unknown'} "
                f"broker={session.broker_mode or 'unknown'} "
                f"mode={session.session_mode or 'unknown'}"
            )
            meta_col.metric("PID", session.pid)
            meta_col.metric("Active Symbols", session.active_symbol_count or 0)
            action_col.metric("Status", "Running" if session.is_running else "Stopped")

            st.caption(
                f"Session config: {session.session_config_path or 'unavailable'}"
            )
            if session.active_symbols_path:
                st.caption(f"Active symbols file: {session.active_symbols_path}")

            action_left, action_right = st.columns(2)
            with action_left:
                if st.button(
                    "Open Session Updates",
                    key=f"open_session_updates_{session.profile_slug}",
                    use_container_width=True,
                ):
                    show_session_updates(session.model_dump(mode="json"))
            with action_right:
                terminate_disabled = not session.is_running
                if st.button(
                    "Terminate Current Run",
                    key=f"terminate_session_{session.profile_slug}",
                    type="primary",
                    use_container_width=True,
                    disabled=terminate_disabled,
                ):
                    result = service.terminate_session(session.profile_slug)
                    if result.ok:
                        st.success(result.message)
                    else:
                        st.error(result.message)
                    st.rerun()
