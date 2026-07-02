"""
=========================================================
PharmaGuard AI
Session Management
=========================================================
Enterprise Edition v3
=========================================================
"""

from __future__ import annotations

from datetime import datetime, timedelta
from typing import Optional

import streamlit as st

from config import SESSION_TIMEOUT

# ==========================================================
# DEFAULT SESSION VALUES
# ==========================================================

DEFAULT_SESSION = {
    "logged_in": False,
    "user_id": None,
    "fullname": "",
    "email": "",
    "role": "",
    "login_time": None,
    "last_activity": None,
    "remember_me": False,
    "current_page": "dashboard"
}

# ==========================================================
# INITIALIZE
# ==========================================================

def initialize_session() -> None:
    """
    Initialize Streamlit session state.
    """

    for key, value in DEFAULT_SESSION.items():

        if key not in st.session_state:

            st.session_state[key] = value


# ==========================================================
# LOGIN
# ==========================================================

def login(
    user: dict,
    remember_me: bool = False
) -> None:
    """
    Save authenticated user inside session.
    """

    now = datetime.now()

    st.session_state.logged_in = True

    st.session_state.user_id = user["id"]

    st.session_state.fullname = user["fullname"]

    st.session_state.email = user["email"]

    st.session_state.role = user["role"]

    st.session_state.login_time = now

    st.session_state.last_activity = now

    st.session_state.remember_me = remember_me


# ==========================================================
# LOGOUT
# ==========================================================

def logout() -> None:
    """
    Destroy session.
    """

    for key in list(st.session_state.keys()):

        del st.session_state[key]

    initialize_session()

    st.rerun()


# ==========================================================
# LOGIN STATUS
# ==========================================================

def is_logged_in() -> bool:

    return bool(st.session_state.logged_in)


# ==========================================================
# USER
# ==========================================================

def get_current_user() -> Optional[dict]:

    if not is_logged_in():

        return None

    return {

        "id": st.session_state.user_id,

        "fullname": st.session_state.fullname,

        "email": st.session_state.email,

        "role": st.session_state.role

    }


# ==========================================================
# SESSION TIMER
# ==========================================================

def update_last_activity() -> None:

    if is_logged_in():

        st.session_state.last_activity = datetime.now()
        # ==========================================================
# SESSION TIMEOUT
# ==========================================================

def check_session_timeout() -> None:
    """
    Automatically logout inactive users.
    """

    if not is_logged_in():
        return

    last_activity = st.session_state.last_activity

    if last_activity is None:
        st.session_state.last_activity = datetime.now()
        return

    timeout = timedelta(minutes=SESSION_TIMEOUT)

    if datetime.now() - last_activity > timeout:

        logout()

    else:

        update_last_activity()


# ==========================================================
# ROLE CHECK
# ==========================================================

def has_role(role: str) -> bool:
    """
    Generic role checker.
    """

    if not is_logged_in():
        return False

    return st.session_state.role == role


def is_admin() -> bool:

    return has_role("Admin")


def is_hospital() -> bool:

    return has_role("Hospital")


def is_pharmacy() -> bool:

    return has_role("Pharmacy")


# ==========================================================
# PAGE
# ==========================================================

def set_current_page(page: str) -> None:

    st.session_state.current_page = page


def get_current_page() -> str:

    return st.session_state.current_page


# ==========================================================
# LOGIN INFO
# ==========================================================

def get_login_time():

    return st.session_state.login_time


def session_duration() -> int:
    """
    Returns session duration in minutes.
    """

    if not is_logged_in():
        return 0

    login_time = st.session_state.login_time

    if login_time is None:
        return 0

    return int(

        (datetime.now() - login_time).total_seconds() / 60

    )


# ==========================================================
# SESSION SUMMARY
# ==========================================================

def session_info() -> dict:

    return {

        "logged_in": is_logged_in(),

        "user_id": st.session_state.user_id,

        "fullname": st.session_state.fullname,

        "email": st.session_state.email,

        "role": st.session_state.role,

        "login_time": st.session_state.login_time,

        "last_activity": st.session_state.last_activity,

        "remember_me": st.session_state.remember_me,

        "duration_minutes": session_duration()

    }


# ==========================================================
# EXPORTS
# ==========================================================
# ==========================================================
# SESSION DURATION
# ==========================================================

def session_duration() -> int:
    """
    Calculate current session duration in minutes.
    
    Returns
    -------
    int
        Session duration in minutes
    """
    from datetime import datetime
    
    if "last_activity" in st.session_state and st.session_state.last_activity:
        diff = datetime.now() - st.session_state.last_activity
        return int(diff.total_seconds() / 60)
    
    return 0
__all__ = [
    "initialize_session",
    "login",
    "logout",
    "is_logged_in",
    "is_admin",
    "is_hospital",
    "is_pharmacy",
    "check_session_timeout",
    "get_current_user",
    "session_duration"  # <-- اضافه کن
]