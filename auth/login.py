"""
=========================================================
PharmaGuard AI
Login Page
=========================================================
Enterprise Edition v3
=========================================================
"""

from __future__ import annotations

import streamlit as st

from auth.security import (
    verify_password,
    validate_login
)

from auth.session import login

from database.database import (
    get_user_by_email,
    log_activity
)

# ==========================================================
# LOGIN PAGE
# ==========================================================
st.markdown("""
<div class="login-wrapper">
<div class="login-card">

<div class="login-logo">
💊
</div>

<div class="login-title">
PharmaGuard AI
</div>

<div class="login-subtitle">
AI Powered Drug Supply Chain Platform
</div>
""", unsafe_allow_html=True)
def show_login() -> None:

    st.subheader("🔐 Login")

    st.caption(
        "Sign in to your PharmaGuard AI account."
    )

    with st.form("login_form"):

        email = st.text_input(
            "Email",
            placeholder="john@example.com"
        )

        password = st.text_input(
            "Password",
            type="password"
        )

        remember_me = st.checkbox(
            "Remember Me"
        )

        login_btn = st.form_submit_button(

            "Login",

            use_container_width=True

        )

    if not login_btn:

        return

    # ======================================================
    # VALIDATION
    # ======================================================

    valid, message = validate_login(

        email,

        password

    )

    if not valid:

        st.error(message)

        return

    # ======================================================
    # GET USER
    # ======================================================

    user = get_user_by_email(email)

    if user is None:

        st.error(

            "Invalid email or password."

        )

        return

    # ======================================================
    # PASSWORD VERIFY
    # ======================================================

    if not verify_password(

        password,

        user["password"]

    ):

        st.error(

            "Invalid email or password."

        )

        return

    # ======================================================
    # LOGIN SESSION
    # ======================================================

    login(

        user,

        remember_me

    )

    # ======================================================
    # LOG ACTIVITY
    # ======================================================

    try:

        log_activity(

            user_id=user["id"],

            action="User Login"

        )

    except Exception:

        pass

    # ======================================================
    # SUCCESS
    # ======================================================

    st.success(

        f"Welcome back, {user['fullname']}!"

    )
    st.markdown("</div></div>", unsafe_allow_html=True)

    st.rerun()


# ==========================================================
# EXPORTS
# ==========================================================

__all__ = [

    "show_login"

]