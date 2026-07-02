"""
=========================================================
PharmaGuard AI
Profile Page - Full Operational Version
=========================================================
"""

from __future__ import annotations

import streamlit as st

from auth.session import get_current_user, session_duration
from auth.security import (
    change_password, validate_password,
    save_profile_picture, get_profile_picture, delete_profile_picture
)
from database.database import (
    get_notification_preferences, update_notification_preferences, log_activity
)


def show_profile():
    st.title("👤 User Profile")
    st.caption("View and manage your account information.")

    user = get_current_user()
    if user is None:
        st.error("User session not found.")
        return

    tab1, tab2, tab3, tab4 = st.tabs([
        "📋 Profile", "🔑 Change Password", "🖼️ Profile Picture", "🔔 Notifications"
    ])

    # ======================================================
    # TAB 1: PROFILE
    # ======================================================
    with tab1:
        st.subheader("Personal Information")
        col1, col2 = st.columns(2)
        with col1:
            st.text_input("Full Name", value=user["fullname"], disabled=True)
            st.text_input("Email", value=user["email"], disabled=True)
        with col2:
            st.text_input("Role", value=user["role"], disabled=True)
            duration = session_duration()
            st.text_input("Session Duration", value=f"{duration} Minutes" if duration > 0 else "Just started", disabled=True)

        st.divider()
        st.subheader("Account Status")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.markdown("""<div style="background:#E8F5E9;padding:15px;border-radius:10px;text-align:center;border:1px solid #4CAF50;"><div style="font-size:32px;">✅</div><div style="font-weight:600;color:#2E7D32;">Account Active</div></div>""", unsafe_allow_html=True)
        with col2:
            st.markdown("""<div style="background:#E3F2FD;padding:15px;border-radius:10px;text-align:center;border:1px solid #2196F3;"><div style="font-size:32px;">🔐</div><div style="font-weight:600;color:#0D47A1;">Authenticated</div></div>""", unsafe_allow_html=True)
        with col3:
            st.markdown("""<div style="background:#E8F5E9;padding:15px;border-radius:10px;text-align:center;border:1px solid #4CAF50;"><div style="font-size:32px;">🟢</div><div style="font-weight:600;color:#2E7D32;">Session Running</div></div>""", unsafe_allow_html=True)

    # ======================================================
    # TAB 2: CHANGE PASSWORD
    # ======================================================
    with tab2:
        st.subheader("🔑 Change Password")
        with st.form("change_password_form"):
            current = st.text_input("Current Password", type="password")
            new_password = st.text_input("New Password", type="password")
            confirm = st.text_input("Confirm New Password", type="password")
            submitted = st.form_submit_button("🔄 Update Password", use_container_width=True)
            if submitted:
                if not current or not new_password or not confirm:
                    st.error("❌ All fields are required!")
                elif new_password != confirm:
                    st.error("❌ Passwords do not match!")
                else:
                    status, message = validate_password(new_password)
                    if not status:
                        st.error(f"❌ {message}")
                    else:
                        if change_password(user["id"], new_password):
                            log_activity(user["id"], "Changed password")
                            st.success("✅ Password updated successfully!")
                            st.balloons()
                        else:
                            st.error("❌ Failed to update password.")

    # ======================================================
    # TAB 3: PROFILE PICTURE
    # ======================================================
    with tab3:
        st.subheader("🖼️ Profile Picture")
        col1, col2 = st.columns([1, 2])
        with col1:
            img_data = get_profile_picture(user["id"])
            if img_data:
                st.markdown(f"""<div style="width:150px;height:150px;border-radius:50%;overflow:hidden;border:3px solid #0F4C81;margin:0 auto;"><img src="data:image/png;base64,{img_data}" style="width:100%;height:100%;object-fit:cover;"></div>""", unsafe_allow_html=True)
                if st.button("🗑️ Remove Picture", use_container_width=True):
                    if delete_profile_picture(user["id"]):
                        st.success("✅ Picture removed!")
                        st.rerun()
            else:
                st.markdown("""<div style="width:150px;height:150px;border-radius:50%;background:#E0E0E0;display:flex;align-items:center;justify-content:center;font-size:64px;margin:0 auto;border:3px solid #0F4C81;">👤</div>""", unsafe_allow_html=True)
        with col2:
            uploaded_file = st.file_uploader("Choose a profile picture", type=["png", "jpg", "jpeg", "gif"])
            if uploaded_file is not None:
                if uploaded_file.size > 5 * 1024 * 1024:
                    st.error("❌ File too large. Max 5MB.")
                else:
                    save_profile_picture(user["id"], uploaded_file)
                    log_activity(user["id"], "Uploaded profile picture")
                    st.success("✅ Profile picture uploaded!")
                    st.rerun()

    # ======================================================
    # TAB 4: NOTIFICATIONS
    # ======================================================
    with tab4:
        st.subheader("🔔 Notification Preferences")
        prefs = get_notification_preferences(user["id"])
        with st.form("notification_preferences_form"):
            email_notif = st.checkbox("📧 Email Notifications", value=prefs["email_notifications"])
            high_risk = st.checkbox("🚨 High Risk Alerts", value=prefs["high_risk_alerts"])
            weekly_report = st.checkbox("📊 Weekly Reports", value=prefs["weekly_reports"])
            submitted = st.form_submit_button("💾 Save Preferences", use_container_width=True)
            if submitted:
                if update_notification_preferences(user["id"], email_notif, high_risk, weekly_report):
                    log_activity(user["id"], "Updated notification preferences")
                    st.success("✅ Preferences saved successfully!")
                    st.balloons()
                else:
                    st.error("❌ Failed to save preferences.")

    st.divider()
    st.caption(f"👤 Logged in as: {user['fullname']} ({user['email']})")


__all__ = ["show_profile"]