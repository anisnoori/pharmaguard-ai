"""
=========================================================
PharmaGuard AI
Database Module
=========================================================
"""

from __future__ import annotations

import sqlite3
from pathlib import Path
from datetime import datetime
from typing import Optional

from config import DATABASE_FILE

DB_PATH = Path(DATABASE_FILE)

# ==========================================================
# CONNECTION
# ==========================================================

def get_connection() -> sqlite3.Connection:
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


# ==========================================================
# INITIALIZE DATABASE
# ==========================================================

def initialize_database() -> None:
    conn = get_connection()
    cur = conn.cursor()

    # Users Table
    cur.execute("""
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        fullname TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL,
        role TEXT NOT NULL,
        created_at TEXT NOT NULL
    )
    """)

    # Drugs Table
    cur.execute("""
    CREATE TABLE IF NOT EXISTS drugs(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        drug_name TEXT NOT NULL,
        manufacturer TEXT,
        stock_level INTEGER,
        availability REAL,
        daily_consumption REAL,
        lead_time REAL,
        shipping_time REAL,
        created_by INTEGER,
        created_at TEXT,
        FOREIGN KEY(created_by) REFERENCES users(id)
    )
    """)

    # Predictions Table
    cur.execute("""
    CREATE TABLE IF NOT EXISTS predictions(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        drug_name TEXT,
        risk_score REAL,
        risk_level TEXT,
        predicted_by INTEGER,
        prediction_time TEXT,
        FOREIGN KEY(predicted_by) REFERENCES users(id)
    )
    """)

    # Activity Log Table
    cur.execute("""
    CREATE TABLE IF NOT EXISTS activity_log(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        action TEXT,
        created_at TEXT,
        FOREIGN KEY(user_id) REFERENCES users(id)
    )
    """)

    # Notification Preferences Table
    cur.execute("""
    CREATE TABLE IF NOT EXISTS notification_preferences(
        user_id INTEGER PRIMARY KEY,
        email_notifications INTEGER DEFAULT 1,
        high_risk_alerts INTEGER DEFAULT 1,
        weekly_reports INTEGER DEFAULT 0,
        FOREIGN KEY(user_id) REFERENCES users(id) ON DELETE CASCADE
    )
    """)

    conn.commit()
    conn.close()


# ==========================================================
# USER
# ==========================================================

def create_user(fullname: str, email: str, password: str, role: str) -> bool:
    conn = get_connection()
    cur = conn.cursor()
    try:
        cur.execute(
            "INSERT INTO users(fullname, email, password, role, created_at) VALUES(?,?,?,?,?)",
            (fullname, email, password, role, datetime.now().isoformat())
        )
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        conn.close()


def get_user_by_email(email: str) -> Optional[sqlite3.Row]:
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE email=?", (email,))
    row = cur.fetchone()
    conn.close()
    return row


def get_user_by_id(user_id: int) -> Optional[sqlite3.Row]:
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE id=?", (user_id,))
    row = cur.fetchone()
    conn.close()
    return row


def update_user_password(user_id: int, new_password: str) -> bool:
    conn = get_connection()
    cur = conn.cursor()
    try:
        cur.execute("UPDATE users SET password = ? WHERE id = ?", (new_password, user_id))
        conn.commit()
        return True
    except Exception:
        return False
    finally:
        conn.close()


# ==========================================================
# DRUGS
# ==========================================================

def add_drug(
    drug_name: str,
    manufacturer: str,
    stock_level: int,
    availability: float,
    daily_consumption: float,
    lead_time: float,
    shipping_time: float,
    created_by: int
) -> bool:
    conn = get_connection()
    cur = conn.cursor()
    try:
        cur.execute(
            """
            INSERT INTO drugs(
                drug_name, manufacturer, stock_level, availability,
                daily_consumption, lead_time, shipping_time, created_by, created_at
            ) VALUES(?,?,?,?,?,?,?,?,?)
            """,
            (drug_name, manufacturer, stock_level, availability,
             daily_consumption, lead_time, shipping_time, created_by,
             datetime.now().isoformat())
        )
        conn.commit()
        return True
    except Exception:
        return False
    finally:
        conn.close()


def get_all_drugs():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM drugs ORDER BY drug_name")
    rows = cur.fetchall()
    conn.close()
    return rows


def delete_drug(drug_id: int):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM drugs WHERE id=?", (drug_id,))
    conn.commit()
    conn.close()


# ==========================================================
# PREDICTIONS
# ==========================================================

def save_prediction(drug_name: str, risk_score: float, risk_level: str, predicted_by: int) -> bool:
    conn = get_connection()
    cur = conn.cursor()
    try:
        cur.execute(
            "INSERT INTO predictions(drug_name, risk_score, risk_level, predicted_by, prediction_time) VALUES(?,?,?,?,?)",
            (drug_name, risk_score, risk_level, predicted_by, datetime.now().isoformat())
        )
        conn.commit()
        return True
    finally:
        conn.close()


def get_prediction_history():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM predictions ORDER BY prediction_time DESC")
    rows = cur.fetchall()
    conn.close()
    return rows


# ==========================================================
# ACTIVITY LOG
# ==========================================================

def log_activity(user_id: int, action: str) -> None:
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO activity_log(user_id, action, created_at) VALUES(?,?,?)",
        (user_id, action, datetime.now().isoformat())
    )
    conn.commit()
    conn.close()


def get_activity_log(limit: int = 100):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        """
        SELECT activity_log.*, users.fullname
        FROM activity_log
        LEFT JOIN users ON users.id = activity_log.user_id
        ORDER BY created_at DESC
        LIMIT ?
        """,
        (limit,)
    )
    rows = cur.fetchall()
    conn.close()
    return rows


# ==========================================================
# NOTIFICATION PREFERENCES
# ==========================================================

def get_notification_preferences(user_id: int) -> dict:
    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute(
            "SELECT email_notifications, high_risk_alerts, weekly_reports FROM notification_preferences WHERE user_id = ?",
            (user_id,)
        )
        row = cur.fetchone()
        conn.close()
        if row:
            return {
                "email_notifications": bool(row[0]),
                "high_risk_alerts": bool(row[1]),
                "weekly_reports": bool(row[2])
            }
        return {"email_notifications": True, "high_risk_alerts": True, "weekly_reports": False}
    except Exception:
        return {"email_notifications": True, "high_risk_alerts": True, "weekly_reports": False}


def update_notification_preferences(
    user_id: int,
    email_notifications: bool,
    high_risk_alerts: bool,
    weekly_reports: bool
) -> bool:
    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute(
            """
            INSERT OR REPLACE INTO notification_preferences
            (user_id, email_notifications, high_risk_alerts, weekly_reports)
            VALUES (?, ?, ?, ?)
            """,
            (user_id, 1 if email_notifications else 0,
             1 if high_risk_alerts else 0, 1 if weekly_reports else 0)
        )
        conn.commit()
        conn.close()
        return True
    except Exception:
        return False


# ==========================================================
# DASHBOARD STATISTICS
# ==========================================================

def get_dashboard_statistics():
    conn = get_connection()
    cur = conn.cursor()
    stats = {}
    cur.execute("SELECT COUNT(*) FROM users")
    stats["users"] = cur.fetchone()[0]
    cur.execute("SELECT COUNT(*) FROM drugs")
    stats["drugs"] = cur.fetchone()[0]
    cur.execute("SELECT COUNT(*) FROM predictions")
    stats["predictions"] = cur.fetchone()[0]
    cur.execute("SELECT COUNT(*) FROM predictions WHERE risk_level='High'")
    stats["high_risk"] = cur.fetchone()[0]
    conn.close()
    return stats


# ==========================================================
# EXPORTS
# ==========================================================

__all__ = [
    "initialize_database",
    "get_connection",
    "create_user",
    "get_user_by_email",
    "get_user_by_id",
    "update_user_password",
    "add_drug",
    "get_all_drugs",
    "delete_drug",
    "save_prediction",
    "get_prediction_history",
    "log_activity",
    "get_activity_log",
    "get_notification_preferences",
    "update_notification_preferences",
    "get_dashboard_statistics"
]