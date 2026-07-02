"""
=========================================================
PharmaGuard AI
Prediction History
=========================================================
Enterprise Edition v3
=========================================================
"""

from __future__ import annotations

import pandas as pd
import streamlit as st

from database.database import (

    get_prediction_history

)

# ==========================================================
# PAGE
# ==========================================================

def show_history():

    st.title("📜 Prediction History")

    st.caption(

        "View all previous AI prediction records."

    )

    history = get_prediction_history()

    if len(history) == 0:

        st.info(

            "No prediction history available."

        )

        return

    # ======================================================
    # DATAFRAME
    # ======================================================

    df = pd.DataFrame(

        [

            dict(row)

            for row in history

        ]

    )

    st.dataframe(

        df,

        use_container_width=True,

        hide_index=True

    )

    # ======================================================
    # SUMMARY
    # ======================================================

    st.divider()

    st.subheader("📊 Summary")

    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(

            "Total Predictions",

            len(df)

        )

    with col2:

        st.metric(

            "High Risk",

            len(

                df[

                    df["risk_level"] == "High"

                ]

            )

        )

    with col3:

        average = round(

            df["risk_score"].mean(),

            2

        )

        st.metric(

            "Average Risk",

            average

        )

    # ======================================================
    # DOWNLOAD
    # ======================================================

    st.download_button(

        "📄 Download CSV",

        data=df.to_csv(

            index=False

        ),

        file_name="prediction_history.csv",

        mime="text/csv",

        use_container_width=True

    )


# ==========================================================
# EXPORTS
# ==========================================================

__all__ = [

    "show_history"

]