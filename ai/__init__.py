"""
=========================================================
PharmaGuard AI
AI Module
=========================================================
"""

from .predict import predict_risk, predict_with_confidence
from .recommendation import build_prediction_result
from .explainability import explain_prediction
from .model_loader import get_model, model_exists, get_model_information

__all__ = [
    "predict_risk",
    "predict_with_confidence",
    "build_prediction_result",
    "explain_prediction",
    "get_model",
    "model_exists",
    "get_model_information"
]