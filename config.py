"""
=========================================================
PharmaGuard AI
Configuration File
=========================================================
"""

from pathlib import Path

# =========================================================
# Project Information
# =========================================================

APP_NAME = "PharmaGuard AI"
APP_VERSION = "1.0.0"
APP_DESCRIPTION = "AI-Driven Early Warning System for Pharmaceutical Supply Chain Disruptions"

# =========================================================
# Directories
# =========================================================

BASE_DIR = Path(__file__).resolve().parent
ASSETS_DIR = BASE_DIR / "assets"
DATA_DIR = BASE_DIR / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"
MODELS_DIR = BASE_DIR / "models"
DATABASE_DIR = BASE_DIR / "database"
LOG_DIR = BASE_DIR / "logs"
EXPORT_DIR = BASE_DIR / "exports"
UPLOAD_DIR = BASE_DIR / "uploads" / "profile_pictures"  # <-- این خط رو اضافه کن

# =========================================================
# Files
# =========================================================

DATABASE_FILE = DATABASE_DIR / "pharmaguard.db"
MODEL_FILE = MODELS_DIR / "risk_prediction_model.pkl"
DATASET_FILE = PROCESSED_DATA_DIR / "processed_supply_chain.csv"
CSS_FILE = ASSETS_DIR / "style.css"

# =========================================================
# Theme Colors
# =========================================================

PRIMARY_COLOR = "#0F4C81"
SUCCESS_COLOR = "#2ECC71"
WARNING_COLOR = "#F39C12"
DANGER_COLOR = "#E74C3C"
BACKGROUND_COLOR = "#F4F7FC"
CARD_RADIUS = 14

# =========================================================
# Security
# =========================================================

SESSION_TIMEOUT = 60
PASSWORD_MIN_LENGTH = 8

# =========================================================
# AI Configuration
# =========================================================

RISK_THRESHOLD_LOW = 40
RISK_THRESHOLD_MEDIUM = 70
CONFIDENCE_THRESHOLD = 0.80

# =========================================================
# Dashboard
# =========================================================

DEFAULT_PAGE_SIZE = 20
MAX_UPLOAD_SIZE = 25  # MB

# =========================================================
# Create Required Folders
# =========================================================

REQUIRED_DIRECTORIES = [
    RAW_DATA_DIR,
    PROCESSED_DATA_DIR,
    MODELS_DIR,
    DATABASE_DIR,
    LOG_DIR,
    EXPORT_DIR,
    UPLOAD_DIR  # <-- این رو هم به لیست اضافه کن
]

for directory in REQUIRED_DIRECTORIES:
    directory.mkdir(parents=True, exist_ok=True)