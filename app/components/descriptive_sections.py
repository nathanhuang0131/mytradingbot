from __future__ import annotations

import streamlit as st

from mytradingbot.ui_services.descriptive_sections import DescriptiveSection
from mytradingbot.ui_services.status_reference import TradingTrackPayload


def render_descriptive_section(section: DescriptiveSection) -> None:
    st.markdown(f"#### {section.title}")
    st.caption(section.description)
    if not section.items:
        st.info("No details are available for this section yet.")
        return
    for item in section.items:
        st.markdown(f"**{item.label}:** {item.value}")
        if item.badge:
            st.caption(item.badge)
        st.caption(
            f"What it is: {item.description} What it affects: {item.effect}"
        )


def render_trading_track(track: TradingTrackPayload) -> None:
    st.markdown("### Trading Track")
    st.caption(track.description)

    current_col, saved_col = st.columns(2)
    with current_col:
        st.markdown("#### Current App Session")
        st.caption(
            "This reflects the session that has been run in the current Streamlit app session, if one exists."
        )
        if track.current_session is None:
            st.info("No current app session has been recorded in this Streamlit session yet.")
        else:
            st.markdown(f"**Session ID:** {track.current_session.session_id}")
            st.markdown(f"**Strategy:** {track.current_session.strategy_name}")
            st.markdown(f"**Mode:** {track.current_session.mode.value}")
            st.markdown(f"**Trades placed:** {track.current_session.trade_count}")
            st.markdown(
                f"**Rejected trade attempts:** {track.current_session.rejected_trade_count}"
            )

    with saved_col:
        st.markdown("#### Latest Saved Session")
        st.caption(
            "This is the latest persisted paper-session report found in the repo. It is useful for recent history even after a restart."
        )
        if track.latest_saved_session is None:
            st.info("No saved paper-session report has been found yet.")
        else:
            session = track.latest_saved_session
            st.markdown(f"**Session ID:** {session.session_id}")
            st.markdown(f"**Strategy:** {session.strategy}")
            st.markdown(f"**Mode:** {session.mode.value}")
            st.markdown(f"**Orders placed:** {session.order_count}")
            st.markdown(f"**Accepted candidates:** {session.accepted_count}")
            st.markdown(f"**Rejected candidates:** {session.rejected_count}")
            st.markdown(f"**No-trade success:** {'Yes' if session.no_trade_success else 'No'}")

    st.markdown("#### Recent Signal Outcomes")
    st.caption(
        "These are the most recent decision outcomes written to the repo-local signal ledger."
    )
    if track.recent_activity:
        st.dataframe(
            [
                {
                    "Time": item.timestamp,
                    "Symbol": item.symbol,
                    "Outcome": item.outcome,
                    "Source": item.signal_source,
                    "Predicted Return": item.predicted_return,
                    "Rejection Reason": item.rejection_reason,
                }
                for item in track.recent_activity
            ],
            use_container_width=True,
        )
    else:
        st.info("No recent signal-outcome rows are available yet.")
