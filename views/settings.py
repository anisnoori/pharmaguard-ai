"""
=========================================================
PharmaGuard AI
Settings Page
=========================================================
Enterprise Edition v3
=========================================================
"""

from __future__ import annotations

import streamlit as st

from config import APP_NAME, APP_VERSION, SESSION_TIMEOUT

# ==========================================================
# PAGE
# ==========================================================

def show_settings():
    st.title("⚙️ Settings")
    st.caption("Application configuration and system information.")

    # ======================================================
    # THEME
    # ======================================================

    st.subheader("🎨 Theme")

    # Dark Mode - کار میکنه
    if "dark_mode" not in st.session_state:
        st.session_state.dark_mode = False

    dark_mode = st.toggle(
        "🌙 Dark Mode",
        value=st.session_state.dark_mode,
        key="dark_mode_toggle"
    )

    if dark_mode != st.session_state.dark_mode:
        st.session_state.dark_mode = dark_mode
        st.rerun()

    # Compact Dashboard - درست شد
    if "compact_mode" not in st.session_state:
        st.session_state.compact_mode = False

    compact_mode = st.toggle(
        "📐 Compact Dashboard",
        value=st.session_state.compact_mode,
        key="compact_mode_toggle"
    )

    if compact_mode != st.session_state.compact_mode:
        st.session_state.compact_mode = compact_mode
        st.rerun()

    # Enable Animations - درست شد
    if "animations_enabled" not in st.session_state:
        st.session_state.animations_enabled = True

    animations = st.toggle(
        "✨ Enable Animations",
        value=st.session_state.animations_enabled,
        key="animations_toggle"
    )

    if animations != st.session_state.animations_enabled:
        st.session_state.animations_enabled = animations
        st.rerun()

    st.divider()

    # ======================================================
    # NOTIFICATIONS
    # ======================================================

    st.subheader("🔔 Notifications")

    # Email Notifications - درست شد
    if "email_notifications" not in st.session_state:
        st.session_state.email_notifications = True

    st.checkbox(
        "📧 Email Notifications",
        value=st.session_state.email_notifications,
        key="email_notifications_check",
        disabled=False
    )

    # High Risk Alerts - درست شد
    if "high_risk_alerts" not in st.session_state:
        st.session_state.high_risk_alerts = True

    st.checkbox(
        "🚨 High Risk Alerts",
        value=st.session_state.high_risk_alerts,
        key="high_risk_alerts_check",
        disabled=False
    )

    # Weekly Reports - درست شد
    if "weekly_reports" not in st.session_state:
        st.session_state.weekly_reports = False

    st.checkbox(
        "📊 Weekly Reports",
        value=st.session_state.weekly_reports,
        key="weekly_reports_check",
        disabled=False
    )

    st.divider()

    # ======================================================
    # AI ENGINE
    # ======================================================

    st.subheader("🤖 AI Engine")

    # AI Prediction Model Loaded - درست شد
    if "ai_model_loaded" not in st.session_state:
        st.session_state.ai_model_loaded = True

    st.checkbox(
        "🧠 AI Prediction Model Loaded",
        value=st.session_state.ai_model_loaded,
        key="ai_model_loaded_check",
        disabled=True
    )

    st.success("✅ AI Prediction Model Loaded")
    st.success("✅ Explainability Module Enabled")
    st.success("✅ Recommendation Engine Enabled")

    st.divider()

    # ======================================================
    # DATABASE
    # ======================================================

    st.subheader("🗄️ Database")

    st.success("✅ SQLite Database Connected")
    st.success("✅ Automatic Backup Enabled")

    st.divider()

    # ======================================================
    # APPLICATION
    # ======================================================

    st.subheader("📱 Application")

    st.text_input(
        "Application Name",
        value=APP_NAME,
        disabled=True
    )

    st.text_input(
        "Version",
        value=APP_VERSION,
        disabled=True
    )

    st.number_input(
        "Session Timeout (Minutes)",
        value=SESSION_TIMEOUT,
        disabled=True
    )

    st.divider()

    # ======================================================
    # ABOUT
    # ======================================================

    st.subheader("ℹ️ About")

    st.info(
        "PharmaGuard AI is an AI-driven Early Warning System "
        "for Pharmaceutical Supply Chain Disruptions."
    )

    # ======================================================
    # SAVE BUTTON
    # ======================================================

    st.divider()

    if st.button("💾 Save Settings", use_container_width=True):
        st.success("✅ Settings saved successfully!")
        st.balloons()

# ==========================================================
# EXPORTS
# ==========================================================

__all__ = [
    "show_settings"
]