"""
=========================================================
PharmaGuard AI
Register Page
=========================================================
"""

from __future__ import annotations

import streamlit as st

from auth.security import (
    hash_password,
    validate_registration,
    sanitize_text,
    normalize_email
)
from database.database import create_user, get_user_by_email, log_activity


def show_register() -> None:
    st.markdown("""
    <div style="text-align:center; margin-bottom:20px;">
        <h1 style="font-size:28px; color:#0F4C81;">📝 Create Account</h1>
        <p style="color:#666;">Register to access PharmaGuard AI</p>
    </div>
    """, unsafe_allow_html=True)

    with st.form("register_form"):
        fullname = st.text_input("Full Name", placeholder="Enter your full name")
        email = st.text_input("Email Address", placeholder="Enter your email")
        password = st.text_input("Password", type="password", placeholder="Min 8 characters")
        confirm_password = st.text_input("Confirm Password", type="password", placeholder="Re-enter password")
        role = st.selectbox("Role", ["Hospital", "Pharmacy"])

        submitted = st.form_submit_button("📝 Create Account", use_container_width=True, type="primary")

        if submitted:
            # Clean data
            fullname = sanitize_text(fullname)
            email = normalize_email(email)
            
            if not fullname or not email or not password or not confirm_password:
                st.error("❌ Please complete all fields.")
                return

            if password != confirm_password:
                st.error("❌ Passwords do not match.")
                return

            status, message = validate_registration(fullname, email, password, role)
            if not status:
                st.error(f"❌ {message}")
                return

            if get_user_by_email(email):
                st.error("❌ Email already registered.")
                return

            if create_user(fullname, email, hash_password(password), role):
                log_activity(0, f"New user registered: {email}")
                st.success("✅ Registration completed successfully!")
                st.info("🔐 Please login with your account.")
                st.balloons()
            else:
                st.error("❌ Registration failed.")