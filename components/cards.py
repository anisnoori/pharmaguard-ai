"""
=========================================================
PharmaGuard AI
Card Components
=========================================================
Enterprise Edition v3
=========================================================
"""

from __future__ import annotations

import streamlit as st

# ==========================================================
# METRIC CARD
# ==========================================================

def metric_card(

    title: str,

    value,

    delta=None

):

    st.metric(

        label=title,

        value=value,

        delta=delta

    )


# ==========================================================
# STATUS CARD
# ==========================================================

def status_card(

    title: str,

    status: bool

):

    if status:

        st.success(

            f"✅ {title}"

        )

    else:

        st.error(

            f"❌ {title}"

        )


# ==========================================================
# RISK CARD
# ==========================================================

def risk_card(

    risk_level: str,

    score: float

):

    colors = {

        "Low": "#2ECC71",

        "Medium": "#F39C12",

        "High": "#E74C3C"

    }

    icons = {

        "Low": "🟢",

        "Medium": "🟡",

        "High": "🔴"

    }

    color = colors.get(

        risk_level,

        "#95A5A6"

    )

    icon = icons.get(

        risk_level,

        "⚪"

    )

    st.markdown(

        f"""

        <div style="

            background:{color};

            color:white;

            padding:20px;

            border-radius:12px;

            text-align:center;

            font-size:22px;

            font-weight:bold;

        ">

            {icon}<br>

            {risk_level}<br><br>

            Risk Score : {score}

        </div>

        """,

        unsafe_allow_html=True

    )


# ==========================================================
# INFORMATION CARD
# ==========================================================

def info_card(

    title: str,

    message: str

):

    st.markdown(

        f"""

        <div style="

            border:1px solid #DDDDDD;

            border-radius:12px;

            padding:15px;

            background:#FAFAFA;

        ">

            <h4>{title}</h4>

            <p>{message}</p>

        </div>

        """,

        unsafe_allow_html=True

    )


# ==========================================================
# KPI ROW
# ==========================================================

def kpi_row(

    users,

    drugs,

    predictions,

    high_risk

):

    c1, c2, c3, c4 = st.columns(4)

    with c1:

        metric_card(

            "Users",

            users

        )

    with c2:

        metric_card(

            "Drugs",

            drugs

        )

    with c3:

        metric_card(

            "Predictions",

            predictions

        )

    with c4:

        metric_card(

            "High Risk",

            high_risk

        )


# ==========================================================
# EXPORTS
# ==========================================================

__all__ = [

    "metric_card",

    "status_card",

    "risk_card",

    "info_card",

    "kpi_row"

]