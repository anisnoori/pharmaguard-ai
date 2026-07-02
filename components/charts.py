"""
=========================================================
PharmaGuard AI
Charts Components
=========================================================
Enterprise Edition v3
=========================================================
"""

from __future__ import annotations

import pandas as pd
import streamlit as st

# ==========================================================
# BAR CHART
# ==========================================================

def bar_chart(

    data,

    title: str = ""

):

    if title:

        st.subheader(title)

    st.bar_chart(

        data,

        use_container_width=True

    )


# ==========================================================
# LINE CHART
# ==========================================================

def line_chart(

    data,

    title: str = ""

):

    if title:

        st.subheader(title)

    st.line_chart(

        data,

        use_container_width=True

    )


# ==========================================================
# AREA CHART
# ==========================================================

def area_chart(

    data,

    title: str = ""

):

    if title:

        st.subheader(title)

    st.area_chart(

        data,

        use_container_width=True

    )


# ==========================================================
# RISK DISTRIBUTION
# ==========================================================

def risk_distribution_chart(

    dataframe: pd.DataFrame

):

    if dataframe.empty:

        st.info(

            "No data available."

        )

        return

    risk = dataframe[

        "risk_level"

    ].value_counts()

    st.subheader(

        "Risk Distribution"

    )

    st.bar_chart(

        risk,

        use_container_width=True

    )


# ==========================================================
# SCORE TREND
# ==========================================================

def score_trend_chart(

    dataframe: pd.DataFrame

):

    if dataframe.empty:

        st.info(

            "No data available."

        )

        return

    st.subheader(

        "Risk Score Trend"

    )

    st.line_chart(

        dataframe["risk_score"],

        use_container_width=True

    )


# ==========================================================
# STOCK CHART
# ==========================================================

def stock_chart(

    dataframe: pd.DataFrame

):

    if dataframe.empty:

        st.info(

            "No data available."

        )

        return

    if "drug_name" not in dataframe.columns:

        return

    if "stock_level" not in dataframe.columns:

        return

    chart = dataframe.set_index(

        "drug_name"

    )["stock_level"]

    st.subheader(

        "Drug Stock Levels"

    )

    st.bar_chart(

        chart,

        use_container_width=True

    )


# ==========================================================
# EXPORTS
# ==========================================================

__all__ = [

    "bar_chart",

    "line_chart",

    "area_chart",

    "risk_distribution_chart",

    "score_trend_chart",

    "stock_chart"

]