"""
=========================================================
PharmaGuard AI
Explainability Engine
=========================================================
Enterprise Edition v3
=========================================================
"""

from __future__ import annotations

from typing import List


# ==========================================================
# EXPLAIN PREDICTION
# ==========================================================

def explain_prediction(

    availability: float,

    stock: float,

    daily_consumption: float,

    lead_time: float,

    shipping_time: float

) -> List[str]:
    """
    Generate human-readable explanations
    for the AI prediction.
    """

    explanations: List[str] = []

    # ======================================================
    # Availability
    # ======================================================

    if availability < 20:

        explanations.append(

            "🔴 Product availability is critically low."

        )

    elif availability < 50:

        explanations.append(

            "🟡 Product availability is below the recommended threshold."

        )

    else:

        explanations.append(

            "🟢 Product availability is satisfactory."

        )

    # ======================================================
    # Stock
    # ======================================================

    if stock < 100:

        explanations.append(

            "📦 Current inventory is low."

        )

    elif stock < 300:

        explanations.append(

            "📦 Inventory level is moderate."

        )

    else:

        explanations.append(

            "📦 Inventory level is healthy."

        )

    # ======================================================
    # Daily Consumption
    # ======================================================

    if daily_consumption > 200:

        explanations.append(

            "📈 High demand may rapidly reduce inventory."

        )

    elif daily_consumption > 100:

        explanations.append(

            "📈 Moderate product demand detected."

        )

    else:

        explanations.append(

            "📈 Product demand is currently stable."

        )

    # ======================================================
    # Lead Time
    # ======================================================

    if lead_time > 30:

        explanations.append(

            "🏭 Manufacturing lead time is very long."

        )

    elif lead_time > 15:

        explanations.append(

            "🏭 Manufacturing lead time is moderate."

        )

    else:

        explanations.append(

            "🏭 Manufacturing lead time is acceptable."

        )

    # ======================================================
    # Shipping Time
    # ======================================================

    if shipping_time > 20:

        explanations.append(

            "🚚 Shipping delays significantly increase disruption risk."

        )

    elif shipping_time > 10:

        explanations.append(

            "🚚 Shipping time is slightly above normal."

        )

    else:

        explanations.append(

            "🚚 Shipping performance is within acceptable limits."

        )

    # ======================================================
    # SUMMARY
    # ======================================================

    risk_factors = 0

    if availability < 50:
        risk_factors += 1

    if stock < 100:
        risk_factors += 1

    if daily_consumption > 150:
        risk_factors += 1

    if lead_time > 20:
        risk_factors += 1

    if shipping_time > 15:
        risk_factors += 1

    explanations.append("")

    explanations.append("🧠 AI Summary")

    if risk_factors == 0:

        explanations.append(

            "Overall supply chain indicators are healthy."

        )

    elif risk_factors <= 2:

        explanations.append(

            "Some indicators require monitoring, but no immediate action is needed."

        )

    elif risk_factors <= 4:

        explanations.append(

            "Multiple risk indicators were detected. Preventive action is recommended."

        )

    else:

        explanations.append(

            "Critical supply chain conditions detected. Immediate intervention is strongly recommended."

        )

    return explanations


# ==========================================================
# EXPORTS
# ==========================================================

__all__ = [

    "explain_prediction"

]