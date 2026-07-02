"""
=========================================================
PharmaGuard AI
Auth Module
=========================================================
"""

from .login import show_login
from .register import show_register
from .security import hash_password, verify_password, validate_email, validate_password
from .session import (
    initialize_session,
    login,
    logout,
    is_logged_in,
    is_admin,
    is_hospital,
    is_pharmacy,
    check_session_timeout,
    get_current_user,
    session_duration
)

__all__ = [
    "show_login",
    "show_register",
    "hash_password",
    "verify_password",
    "validate_email",
    "validate_password",
    "initialize_session",
    "login",
    "logout",
    "is_logged_in",
    "is_admin",
    "is_hospital",
    "is_pharmacy",
    "check_session_timeout",
    "get_current_user",
    "session_duration"
]