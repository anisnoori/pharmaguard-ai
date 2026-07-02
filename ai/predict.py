"""
=========================================================
PharmaGuard AI
Prediction Engine
=========================================================
Enterprise Edition v3
=========================================================
"""

from __future__ import annotations

import pandas as pd

from ai.model_loader import get_model

# ==========================================================
# MODEL FEATURES
# ==========================================================

FEATURES = [

    "Availability",

    "Stock levels",

    "Number of products sold",

    "Lead times",

    "Shipping times",

    "Order quantities",

    "Production volumes",

    "Defect rates",

    "Manufacturing lead time"

]

# ==========================================================
# PREPARE FEATURES
# ==========================================================

def prepare_features(

    availability: float,

    stock: float,

    sold: float,

    revenue: float,

    shipping_cost: float,

    lead_time: float,

    order_quantity: float,

    shipping_time: float,

    manufacturing_time: float

) -> pd.DataFrame:
    """
    Build DataFrame for model prediction.
    
    Note: Model was trained with these exact features:
    - Availability
    - Stock levels
    - Number of products sold
    - Lead times
    - Shipping times
    - Order quantities
    - Production volumes
    - Defect rates
    - Manufacturing lead time
    """

    return pd.DataFrame(

        [[

            availability,          # Availability
            stock,                 # Stock levels
            sold,                  # Number of products sold
            lead_time,             # Lead times
            shipping_time,         # Shipping times
            order_quantity,        # Order quantities
            stock,                 # Production volumes (using stock as proxy)
            2.0,                   # Defect rates (default value)
            manufacturing_time     # Manufacturing lead time

        ]],

        columns=FEATURES

    )


# ==========================================================
# PREDICT
# ==========================================================

def predict_risk(

    availability: float,

    stock: float,

    sold: float,

    revenue: float,

    shipping_cost: float,

    lead_time: float,

    order_quantity: float,

    shipping_time: float,

    manufacturing_time: float

) -> float:
    """
    Predict disruption risk score.
    """

    model = get_model()

    features = prepare_features(

        availability,

        stock,

        sold,

        revenue,

        shipping_cost,

        lead_time,

        order_quantity,

        shipping_time,

        manufacturing_time

    )

    prediction = model.predict(

        features

    )

    score = float(

        prediction[0]

    )

    score = max(

        0,

        min(

            100,

            round(score, 2)

        )

    )

    return score


# ==========================================================
# CONFIDENCE
# ==========================================================

def predict_with_confidence(

    availability: float,

    stock: float,

    sold: float,

    revenue: float,

    shipping_cost: float,

    lead_time: float,

    order_quantity: float,

    shipping_time: float,

    manufacturing_time: float

):
    """
    Predict risk with optional confidence.
    """

    score = predict_risk(

        availability,

        stock,

        sold,

        revenue,

        shipping_cost,

        lead_time,

        order_quantity,

        shipping_time,

        manufacturing_time

    )

    confidence = None

    try:

        model = get_model()

        if hasattr(model, "predict_proba"):

            df = prepare_features(

                availability,

                stock,

                sold,

                revenue,

                shipping_cost,

                lead_time,

                order_quantity,

                shipping_time,

                manufacturing_time

            )

            confidence = float(

                model.predict_proba(df).max()

            )

    except Exception:

        confidence = None

    return {

        "risk_score": score,

        "confidence": confidence

    }


# ==========================================================
# EXPORTS
# ==========================================================

__all__ = [

    "FEATURES",

    "prepare_features",

    "predict_risk",

    "predict_with_confidence"

]