"""
=========================================================
PharmaGuard AI
CSV Export Utilities
=========================================================
Enterprise Edition v3
=========================================================
"""

from __future__ import annotations

import pandas as pd

# ==========================================================
# DATAFRAME TO CSV
# ==========================================================

def dataframe_to_csv(

    dataframe: pd.DataFrame

) -> str:
    """
    Convert DataFrame to CSV string.
    """

    return dataframe.to_csv(

        index=False

    )


# ==========================================================
# PREDICTIONS
# ==========================================================

def export_predictions(

    dataframe: pd.DataFrame

) -> str:

    return dataframe.to_csv(

        index=False

    )


# ==========================================================
# DRUGS
# ==========================================================

def export_drugs(

    dataframe: pd.DataFrame

) -> str:

    return dataframe.to_csv(

        index=False

    )


# ==========================================================
# USERS
# ==========================================================

def export_users(

    dataframe: pd.DataFrame

) -> str:

    return dataframe.to_csv(

        index=False

    )


# ==========================================================
# DASHBOARD
# ==========================================================

def export_dashboard(

    dataframe: pd.DataFrame

) -> str:

    return dataframe.to_csv(

        index=False

    )


# ==========================================================
# HISTORY
# ==========================================================

def export_history(

    dataframe: pd.DataFrame

) -> str:

    return dataframe.to_csv(

        index=False

    )


# ==========================================================
# SAVE CSV
# ==========================================================

def save_csv(

    dataframe: pd.DataFrame,

    filename: str

):

    dataframe.to_csv(

        filename,

        index=False

    )


# ==========================================================
# EXPORTS
# ==========================================================

__all__ = [

    "dataframe_to_csv",

    "export_predictions",

    "export_drugs",

    "export_users",

    "export_dashboard",

    "export_history",

    "save_csv"

]