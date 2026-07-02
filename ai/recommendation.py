"""
=========================================================
PharmaGuard AI
Recommendation Engine
=========================================================
"""

from __future__ import annotations

# ==========================================================
# RISK LEVEL
# ==========================================================

def get_risk_level(score: float) -> str:
    if score < 35:
        return "Low"
    elif score < 70:
        return "Medium"
    return "High"


# ==========================================================
# COLOR
# ==========================================================

def get_risk_color(level: str) -> str:
    colors = {
        "Low": "#2ECC71",
        "Medium": "#F39C12",
        "High": "#E74C3C"
    }
    return colors.get(level, "#95A5A6")


# ==========================================================
# ICON
# ==========================================================

def get_risk_icon(level: str) -> str:
    icons = {
        "Low": "🟢",
        "Medium": "🟡",
        "High": "🔴"
    }
    return icons.get(level, "⚪")


# ==========================================================
# PRIORITY
# ==========================================================

def get_priority(level: str) -> str:
    priorities = {
        "Low": "Low Priority",
        "Medium": "Medium Priority",
        "High": "Critical"
    }
    return priorities.get(level, "Unknown")


# ==========================================================
# IMPACT
# ==========================================================

def get_impact(level: str) -> str:
    impacts = {
        "Low": "Supply chain is stable. Continue regular monitoring.",
        "Medium": "Moderate risk. Monitor closely and consider preventive measures.",
        "High": "High risk of supply disruption. Immediate action required."
    }
    return impacts.get(level, "Status unknown.")


# ==========================================================
# RECOMMENDATIONS
# ==========================================================

def generate_recommendations(level: str):
    if level == "Low":
        return [
            "Inventory level is stable.",
            "Continue routine monitoring.",
            "No immediate action required."
        ]
    elif level == "Medium":
        return [
            "Review inventory weekly.",
            "Monitor supplier performance.",
            "Prepare backup supplier."
        ]
    return [
        "Increase inventory immediately.",
        "Notify supply chain manager.",
        "Contact alternative suppliers.",
        "Place emergency purchase order.",
        "Monitor stock daily."
    ]


# ==========================================================
# COMPLETE RESULT
# ==========================================================

def build_prediction_result(score: float):
    level = get_risk_level(score)
    return {
        "risk_score": round(score, 2),
        "risk_level": level,
        "priority": get_priority(level),
        "color": get_risk_color(level),
        "icon": get_risk_icon(level),
        "recommendations": generate_recommendations(level),
        "impact": get_impact(level)
    }


# ==========================================================
# EXPORTS
# ==========================================================

__all__ = [
    "build_prediction_result",
    "get_risk_level",
    "get_risk_color",
    "get_risk_icon",
    "get_impact",
    "generate_recommendations",
    "get_priority"
]