"""
=========================================================
PharmaGuard AI
Security Module
=========================================================
"""

from __future__ import annotations

import re
import secrets
import string
import base64
from pathlib import Path
from typing import Tuple

import bcrypt

from config import PASSWORD_MIN_LENGTH, UPLOAD_DIR

# ==========================================================
# CONSTANTS
# ==========================================================

VALID_ROLES = {"Admin", "Hospital", "Pharmacy"}

COMMON_PASSWORDS = {
    "password", "password123", "123456", "12345678",
    "qwerty", "abc123", "admin", "admin123",
    "letmein", "welcome"
}

EMAIL_PATTERN = re.compile(r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$")
FULLNAME_PATTERN = re.compile(r"^[A-Za-zÀ-ÿ\s'-]{3,100}$")


# ==========================================================
# SANITIZATION
# ==========================================================

def sanitize_text(value: str) -> str:
    return " ".join(value.strip().split())


def normalize_email(email: str) -> str:
    return sanitize_text(email).lower()


# ==========================================================
# PASSWORD HASHING
# ==========================================================

def hash_password(password: str) -> str:
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt(rounds=12)).decode("utf-8")


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return bcrypt.checkpw(plain_password.encode("utf-8"), hashed_password.encode("utf-8"))


def change_password(user_id: int, new_password: str) -> bool:
    from database.database import update_user_password
    return update_user_password(user_id, hash_password(new_password))


# ==========================================================
# VALIDATION
# ==========================================================

def validate_email(email: str) -> bool:
    return EMAIL_PATTERN.fullmatch(normalize_email(email)) is not None


def validate_fullname(fullname: str) -> Tuple[bool, str]:
    fullname = sanitize_text(fullname)
    if fullname == "":
        return False, "Full name is required."
    if len(fullname.split()) < 2:
        return False, "Please enter first and last name."
    if not FULLNAME_PATTERN.fullmatch(fullname):
        return False, "Invalid full name."
    return True, "OK"


def validate_password(password: str) -> Tuple[bool, str]:
    if len(password) < PASSWORD_MIN_LENGTH:
        return False, f"Password must contain at least {PASSWORD_MIN_LENGTH} characters."
    if password.lower() in COMMON_PASSWORDS:
        return False, "Password is too common."
    if " " in password:
        return False, "Password cannot contain spaces."
    if not re.search(r"[A-Z]", password):
        return False, "Password must contain one uppercase letter."
    if not re.search(r"[a-z]", password):
        return False, "Password must contain one lowercase letter."
    if not re.search(r"\d", password):
        return False, "Password must contain one number."
    if not re.search(r"[!@#$%^&*()_+\-=\[\]{};':\"\\|,.<>/?]", password):
        return False, "Password must contain one special character."
    return True, "Valid Password"


def validate_role(role: str) -> bool:
    return role in VALID_ROLES


def validate_registration(fullname: str, email: str, password: str, role: str) -> Tuple[bool, str]:
    status, message = validate_fullname(fullname)
    if not status:
        return status, message
    if not validate_email(email):
        return False, "Invalid email address."
    status, message = validate_password(password)
    if not status:
        return status, message
    if not validate_role(role):
        return False, "Invalid role."
    return True, "Validation Successful"


# ==========================================================
# LOGIN VALIDATION
# ==========================================================

def validate_login(email: str, password: str) -> Tuple[bool, str]:
    """Validate login credentials."""
    if sanitize_text(email) == "":
        return False, "Email is required."
    if sanitize_text(password) == "":
        return False, "Password is required."
    if not validate_email(email):
        return False, "Invalid email format."
    return True, "OK"


# ==========================================================
# PROFILE PICTURE
# ==========================================================

def save_profile_picture(user_id: int, file) -> str:
    file_extension = file.name.split('.')[-1]
    file_path = UPLOAD_DIR / f"user_{user_id}.{file_extension}"
    with open(file_path, "wb") as f:
        f.write(file.getbuffer())
    return str(file_path)


def get_profile_picture(user_id: int) -> str:
    for ext in ['png', 'jpg', 'jpeg', 'gif']:
        file_path = UPLOAD_DIR / f"user_{user_id}.{ext}"
        if file_path.exists():
            with open(file_path, "rb") as f:
                return base64.b64encode(f.read()).decode()
    return None


def delete_profile_picture(user_id: int) -> bool:
    for ext in ['png', 'jpg', 'jpeg', 'gif']:
        file_path = UPLOAD_DIR / f"user_{user_id}.{ext}"
        if file_path.exists():
            file_path.unlink()
            return True
    return False


# ==========================================================
# EXPORTS
# ==========================================================

__all__ = [
    "hash_password",
    "verify_password",
    "change_password",
    "validate_email",
    "validate_fullname",
    "validate_password",
    "validate_role",
    "validate_registration",
    "validate_login",
    "sanitize_text",
    "normalize_email",
    "save_profile_picture",
    "get_profile_picture",
    "delete_profile_picture"
]