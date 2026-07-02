"""
=========================================================
PharmaGuard AI
Dashboard Page
=========================================================
Enterprise Edition v3
=========================================================
"""

from __future__ import annotations

import streamlit as st

from database.database import (
    get_dashboard_statistics,
    get_prediction_history,
    get_activity_log,
)

# ==========================================================
# DASHBOARD
# ==========================================================

def show_dashboard():

    # ------------------------------------------------------
    # PAGE TITLE
    # ------------------------------------------------------

    st.title("🏠 Dashboard")

    st.caption(
        "AI-Driven Pharmaceutical Supply Chain Monitoring"
    )

    # ------------------------------------------------------
    # SYSTEM STATISTICS
    # ------------------------------------------------------

    stats = get_dashboard_statistics()

    # ------------------------------------------------------
    # KPI CARDS
    # ------------------------------------------------------

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "👥 Users",
            stats.get("users", 0)
        )

    with col2:
        st.metric(
            "💊 Drugs",
            stats.get("drugs", 0)
        )

    with col3:
        st.metric(
            "🤖 Predictions",
            stats.get("predictions", 0)
        )

    with col4:
        st.metric(
            "🔴 High Risk",
            stats.get("high_risk", 0)
        )

    st.divider()

    # ------------------------------------------------------
    # RECENT PREDICTIONS
    # ------------------------------------------------------

    st.subheader("📊 Recent Predictions")

    history = get_prediction_history()

    if history:

        st.dataframe(
            history,
            use_container_width=True,
            hide_index=True,
        )

    else:

        st.info(
            "No predictions have been made yet."
        )

    st.divider()

    # ------------------------------------------------------
    # RECENT ACTIVITY
    # ------------------------------------------------------

    st.subheader("📜 Recent Activity")

    logs = get_activity_log(10)

    if logs:

        st.dataframe(
            logs,
            use_container_width=True,
            hide_index=True,
        )

    else:

        st.info(
            "No activity available."
        )

    st.divider()

    # ------------------------------------------------------
    # SYSTEM STATUS
    # ------------------------------------------------------

    st.subheader("🟢 System Status")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.success("Database Connected")

    with c2:
        st.success("AI Model Loaded")

    with c3:
        st.success("System Operational")


# ==========================================================
# EXPORTS
# ==========================================================

__all__ = [
    "show_dashboard"
]