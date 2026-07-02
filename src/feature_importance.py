"""
=========================================================
PharmaGuard AI
Feature Importance
=========================================================
Enterprise Edition v3
=========================================================
"""

from __future__ import annotations

import pandas as pd
import streamlit as st

from ai.model_loader import get_model

# ==========================================================
# FEATURE NAMES
# ==========================================================

FEATURES = [

    "Availability",

    "Stock Level",

    "Daily Consumption",

    "Revenue",

    "Shipping Cost",

    "Lead Time",

    "Order Quantity",

    "Shipping Time",

    "Manufacturing Time"

]

# ==========================================================
# GET FEATURE IMPORTANCE
# ==========================================================

def get_feature_importance() -> pd.DataFrame:
    """
    Extract feature importance from trained model.
    """

    model = get_model()

    if not hasattr(

        model,

        "feature_importances_"

    ):

        raise AttributeError(

            "Current model does not support feature importance."

        )

    importance = model.feature_importances_

    df = pd.DataFrame(

        {

            "Feature": FEATURES,

            "Importance": importance

        }

    )

    df = df.sort_values(

        by="Importance",

        ascending=False

    ).reset_index(

        drop=True

    )

    return df


# ==========================================================
# SHOW FEATURE IMPORTANCE
# ==========================================================

def show_feature_importance():

    st.title(

        "📈 Feature Importance"

    )

    try:

        df = get_feature_importance()

    except Exception as e:

        st.error(str(e))

        return

    st.subheader(

        "Feature Ranking"

    )

    st.dataframe(

        df,

        use_container_width=True,

        hide_index=True

    )

    st.subheader(

        "Importance Chart"

    )

    chart = df.set_index(

        "Feature"

    )

    st.bar_chart(

        chart,

        use_container_width=True

    )

    most = df.iloc[0]

    st.success(

        f"Most influential feature: "

        f"{most['Feature']} "

        f"({most['Importance']:.3f})"

    )


# ==========================================================
# EXPORTS
# ==========================================================

__all__ = [

    "get_feature_importance",

    "show_feature_importance"

]