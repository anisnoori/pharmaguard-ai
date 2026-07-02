"""
=========================================================
PharmaGuard AI
AI Model Loader
=========================================================
Enterprise Edition v3
=========================================================
"""

from __future__ import annotations

from pathlib import Path
from typing import Optional

import joblib
import streamlit as st

from config import MODEL_FILE

# ==========================================================
# MODEL PATH
# ==========================================================

MODEL_PATH = Path(MODEL_FILE)

# ==========================================================
# LOAD MODEL
# ==========================================================

@st.cache_resource(show_spinner=False)
def load_model():
    """
    Load trained ML model only once.

    Returns
    -------
    sklearn estimator
    """

    if not MODEL_PATH.exists():

        raise FileNotFoundError(

            f"Model file not found:\n{MODEL_PATH}"

        )

    try:

        model = joblib.load(MODEL_PATH)

    except Exception as e:

        raise RuntimeError(

            f"Unable to load model.\n{e}"

        )

    return model


# ==========================================================
# GET MODEL
# ==========================================================

def get_model():

    return load_model()


# ==========================================================
# MODEL EXISTS
# ==========================================================

def model_exists() -> bool:

    return MODEL_PATH.exists()


# ==========================================================
# MODEL INFORMATION
# ==========================================================

def get_model_information() -> dict:

    info = {

        "exists": model_exists(),

        "path": str(MODEL_PATH),

        "filename": MODEL_PATH.name,

        "size_mb": 0,

        "algorithm": "Unknown"

    }

    if not model_exists():

        return info

    info["size_mb"] = round(

        MODEL_PATH.stat().st_size /

        (1024 * 1024),

        2

    )

    try:

        model = get_model()

        info["algorithm"] = type(model).__name__

    except Exception:

        pass

    return info


# ==========================================================
# RELOAD MODEL
# ==========================================================

def reload_model():

    load_model.clear()

    return load_model()


# ==========================================================
# EXPORTS
# ==========================================================

__all__ = [

    "load_model",

    "get_model",

    "reload_model",

    "model_exists",

    "get_model_information"

]