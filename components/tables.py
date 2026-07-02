"""
=========================================================
PharmaGuard AI
Tables Component
=========================================================
Enterprise Edition v3
=========================================================
"""

from __future__ import annotations

import pandas as pd
import streamlit as st

# ==========================================================
# GENERIC TABLE
# ==========================================================

def show_table(

    dataframe: pd.DataFrame,

    title: str | None = None

):

    if title:

        st.subheader(title)

    if dataframe.empty:

        st.info(

            "No data available."

        )

        return

    st.dataframe(

        dataframe,

        use_container_width=True,

        hide_index=True

    )


# ==========================================================
# DRUG TABLE
# ==========================================================

def drug_table(

    dataframe: pd.DataFrame

):

    show_table(

        dataframe,

        "💊 Registered Drugs"

    )


# ==========================================================
# PREDICTION TABLE
# ==========================================================

def prediction_table(

    dataframe: pd.DataFrame

):

    show_table(

        dataframe,

        "🤖 Prediction Results"

    )


# ==========================================================
# HISTORY TABLE
# ==========================================================

def history_table(

    dataframe: pd.DataFrame

):

    show_table(

        dataframe,

        "📜 Prediction History"

    )


# ==========================================================
# USER TABLE
# ==========================================================

def user_table(

    dataframe: pd.DataFrame

):

    show_table(

        dataframe,

        "👥 Users"

    )


# ==========================================================
# ACTIVITY LOG TABLE
# ==========================================================

def activity_table(

    dataframe: pd.DataFrame

):

    show_table(

        dataframe,

        "📋 Activity Log"

    )


# ==========================================================
# RISK SUMMARY TABLE
# ==========================================================

def risk_summary_table(

    dataframe: pd.DataFrame

):

    if dataframe.empty:

        st.info(

            "No summary available."

        )

        return

    summary = (

        dataframe["risk_level"]

        .value_counts()

        .rename_axis("Risk Level")

        .reset_index(name="Count")

    )

    st.subheader(

        "📊 Risk Summary"

    )

    st.dataframe(

        summary,

        use_container_width=True,

        hide_index=True

    )


# ==========================================================
# EXPORTS
# ==========================================================

__all__ = [

    "show_table",

    "drug_table",

    "prediction_table",

    "history_table",

    "user_table",

    "activity_table",

    "risk_summary_table"

]