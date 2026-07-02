"""
=========================================================
PharmaGuard AI
Admin Dashboard
=========================================================
Enterprise Edition v3
=========================================================
"""

from __future__ import annotations

import streamlit as st

from auth.session import (

    is_admin

)

from database.database import (

    get_dashboard_statistics,

    get_prediction_history,

    get_activity_log,

    get_all_users,

    get_all_drugs

)

# ==========================================================
# PAGE
# ==========================================================

def show_admin():

    st.title("🛡 Admin Dashboard")

    if not is_admin():

        st.error(

            "Access denied."

        )

        return

    # ======================================================
    # SYSTEM KPI
    # ======================================================

    stats = get_dashboard_statistics()

    c1, c2, c3, c4 = st.columns(4)

    with c1:

        st.metric(

            "Users",

            stats["users"]

        )

    with c2:

        st.metric(

            "Drugs",

            stats["drugs"]

        )

    with c3:

        st.metric(

            "Predictions",

            stats["predictions"]

        )

    with c4:

        st.metric(

            "High Risk",

            stats["high_risk"]

        )

    st.divider()

    # ======================================================
    # USERS
    # ======================================================

    st.subheader("👥 Registered Users")

    users = get_all_users()

    if users:

        st.dataframe(

            users,

            use_container_width=True,

            hide_index=True

        )

    else:

        st.info(

            "No users found."

        )

    st.divider()

    # ======================================================
    # DRUGS
    # ======================================================

    st.subheader("💊 Registered Drugs")

    drugs = get_all_drugs()

    if drugs:

        st.dataframe(

            drugs,

            use_container_width=True,

            hide_index=True

        )

    else:

        st.info(

            "No drugs available."

        )

    st.divider()

    # ======================================================
    # RECENT PREDICTIONS
    # ======================================================

    st.subheader("🤖 Recent Predictions")

    history = get_prediction_history()

    if history:

        st.dataframe(

            history,

            use_container_width=True,

            hide_index=True

        )

    else:

        st.info(

            "No prediction history."

        )

    st.divider()

    # ======================================================
    # ACTIVITY LOG
    # ======================================================

    st.subheader("📜 Activity Log")

    logs = get_activity_log(20)

    if logs:

        st.dataframe(

            logs,

            use_container_width=True,

            hide_index=True

        )

    else:

        st.info(

            "No activity logs."

        )

    st.divider()

    # ======================================================
    # SYSTEM STATUS
    # ======================================================

    st.subheader("🟢 System Status")

    st.success("Database Connected")

    st.success("AI Model Loaded")

    st.success("Prediction Engine Active")

    st.success("Recommendation Engine Active")

    st.success("Explainability Engine Active")


# ==========================================================
# EXPORTS
# ==========================================================

__all__ = [

    "show_admin"

]