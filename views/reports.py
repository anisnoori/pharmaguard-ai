"""
=========================================================
PharmaGuard AI
Reports Page
=========================================================
Enterprise Edition v3
=========================================================
"""

from __future__ import annotations

import pandas as pd
import streamlit as st

from database.database import (

    get_prediction_history,

    get_dashboard_statistics

)

# ==========================================================
# PAGE
# ==========================================================

def show_reports():

    st.title("📊 Reports")

    st.caption(

        "Analytics and statistics for pharmaceutical supply chain."

    )

    stats = get_dashboard_statistics()

    history = get_prediction_history()

    if len(history) == 0:

        st.info(

            "No reports available."

        )

        return

    df = pd.DataFrame(

        [

            dict(row)

            for row in history

        ]

    )

    # ======================================================
    # KPI
    # ======================================================

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
    # RISK DISTRIBUTION
    # ======================================================

    st.subheader("Risk Distribution")

    risk_counts = (

        df["risk_level"]

        .value_counts()

    )

    st.bar_chart(

        risk_counts

    )

    # ======================================================
    # RISK SCORE
    # ======================================================

    st.subheader("Risk Score Distribution")

    st.line_chart(

        df["risk_score"]

    )

    # ======================================================
    # RECENT REPORT
    # ======================================================

    st.subheader("Prediction Report")

    st.dataframe(

        df,

        use_container_width=True,

        hide_index=True

    )

    # ======================================================
    # EXPORT
    # ======================================================

    st.download_button(

        "📄 Export Report",

        data=df.to_csv(

            index=False

        ),

        file_name="reports.csv",

        mime="text/csv",

        use_container_width=True

    )

    st.success(

        "Report generated successfully."

    )


# ==========================================================
# EXPORTS
# ==========================================================

__all__ = [

    "show_reports"

]