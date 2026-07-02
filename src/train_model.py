"""
=========================================================
PharmaGuard AI
Train Machine Learning Model
=========================================================
Enterprise Edition v3
=========================================================
"""

from __future__ import annotations

from pathlib import Path

import joblib
import pandas as pd

from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)
from sklearn.model_selection import train_test_split

# ==========================================================
# PATHS
# ==========================================================

BASE_DIR = Path(__file__).resolve().parent.parent

DATASET = BASE_DIR / "data" / "processed" / "processed_supply_chain.csv"

MODEL_DIR = BASE_DIR / "models"

MODEL_PATH = MODEL_DIR / "risk_prediction_model.pkl"

# ==========================================================
# FEATURES
# ==========================================================

FEATURES = [

    "Availability",

    "Stock levels",

    "Number of products sold",

    "Revenue generated",

    "Shipping costs",

    "Lead times",

    "Order quantities",

    "Shipping times",

    "Manufacturing lead time"

]

TARGET = "Risk Score"

# ==========================================================
# LOAD DATA
# ==========================================================

def load_dataset():

    if not DATASET.exists():

        raise FileNotFoundError(

            f"Dataset not found:\n{DATASET}"

        )

    return pd.read_csv(

        DATASET

    )

# ==========================================================
# TRAIN MODEL
# ==========================================================

def train():

    df = load_dataset()

    X = df[FEATURES]

    y = df[TARGET]

    X_train, X_test, y_train, y_test = train_test_split(

        X,

        y,

        test_size=0.20,

        random_state=42

    )

    model = RandomForestRegressor(

        n_estimators=300,

        max_depth=15,

        random_state=42,

        n_jobs=-1

    )

    model.fit(

        X_train,

        y_train

    )

    prediction = model.predict(

        X_test

    )

    mae = mean_absolute_error(

        y_test,

        prediction

    )

    mse = mean_squared_error(

        y_test,

        prediction

    )

    rmse = mse ** 0.5

    r2 = r2_score(

        y_test,

        prediction

    )

    MODEL_DIR.mkdir(

        exist_ok=True

    )

    joblib.dump(

        model,

        MODEL_PATH

    )

    print("=" * 60)

    print("PharmaGuard AI Model Training")

    print("=" * 60)

    print(f"Dataset Shape : {df.shape}")

    print(f"Training Rows : {len(X_train)}")

    print(f"Testing Rows  : {len(X_test)}")

    print()

    print(f"MAE  : {mae:.4f}")

    print(f"MSE  : {mse:.4f}")

    print(f"RMSE : {rmse:.4f}")

    print(f"R²   : {r2:.4f}")

    print()

    print(f"Model Saved -> {MODEL_PATH}")

    print("=" * 60)

    return model

# ==========================================================
# MAIN
# ==========================================================

if __name__ == "__main__":

    train()