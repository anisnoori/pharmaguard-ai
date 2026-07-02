"""
=========================================================
PharmaGuard AI
Alert Components
=========================================================
Enterprise Edition v3
=========================================================
"""

from __future__ import annotations

import streamlit as st

# ==========================================================
# SUCCESS
# ==========================================================

def success_alert(

    message: str

):

    st.success(

        f"✅ {message}"

    )


# ==========================================================
# ERROR
# ==========================================================

def error_alert(

    message: str

):

    st.error(

        f"❌ {message}"

    )


# ==========================================================
# WARNING
# ==========================================================

def warning_alert(

    message: str

):

    st.warning(

        f"⚠️ {message}"

    )


# ==========================================================
# INFO
# ==========================================================

def info_alert(

    message: str

):

    st.info(

        f"ℹ️ {message}"

    )


# ==========================================================
# RISK ALERT
# ==========================================================

def risk_alert(

    level: str

):

    level = level.lower()

    if level == "high":

        st.error(

            "🔴 High Risk Detected"

        )

    elif level == "medium":

        st.warning(

            "🟡 Medium Risk Detected"

        )

    elif level == "low":

        st.success(

            "🟢 Low Risk"

        )

    else:

        st.info(

            "Unknown Risk Level"

        )


# ==========================================================
# SYSTEM STATUS
# ==========================================================

def system_status(

    status: bool,

    title: str

):

    if status:

        st.success(

            f"🟢 {title}"

        )

    else:

        st.error(

            f"🔴 {title}"

        )


# ==========================================================
# EXPORTS
# ==========================================================

__all__ = [

    "success_alert",

    "error_alert",

    "warning_alert",

    "info_alert",

    "risk_alert",

    "system_status"

]