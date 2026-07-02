"""
=========================================================
PharmaGuard AI
Helper Functions
=========================================================
Enterprise Edition v3
=========================================================
"""

from __future__ import annotations

from datetime import datetime
from pathlib import Path
import uuid

# ==========================================================
# DATETIME
# ==========================================================

def current_datetime() -> str:
    """
    Current date & time.
    """

    return datetime.now().strftime(

        "%Y-%m-%d %H:%M:%S"

    )


# ==========================================================
# DATE
# ==========================================================

def current_date() -> str:

    return datetime.now().strftime(

        "%Y-%m-%d"

    )


# ==========================================================
# TIME
# ==========================================================

def current_time() -> str:

    return datetime.now().strftime(

        "%H:%M:%S"

    )


# ==========================================================
# FILE NAME
# ==========================================================

def generate_filename(

    prefix: str,

    extension: str

) -> str:

    timestamp = datetime.now().strftime(

        "%Y%m%d_%H%M%S"

    )

    return f"{prefix}_{timestamp}.{extension}"


# ==========================================================
# UUID
# ==========================================================

def generate_id() -> str:

    return str(

        uuid.uuid4()

    )


# ==========================================================
# PERCENT
# ==========================================================

def percent(

    value: float

) -> str:

    return f"{value:.2f}%"


# ==========================================================
# ROUND
# ==========================================================

def round2(

    value: float

) -> float:

    return round(

        value,

        2

    )


# ==========================================================
# SAFE STRING
# ==========================================================

def clean_text(

    text: str

) -> str:

    return text.strip()


# ==========================================================
# PATH
# ==========================================================

def ensure_directory(

    path

):

    Path(path).mkdir(

        parents=True,

        exist_ok=True

    )


# ==========================================================
# EXPORTS
# ==========================================================

__all__ = [

    "current_datetime",

    "current_date",

    "current_time",

    "generate_filename",

    "generate_id",

    "percent",

    "round2",

    "clean_text",

    "ensure_directory"

]