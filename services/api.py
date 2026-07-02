"""
=========================================================
PharmaGuard AI
OpenFDA API Service
=========================================================
"""

from __future__ import annotations

import requests

BASE_URL = "https://api.fda.gov/drug/drugsfda.json"


def test_connection() -> bool:
    """
    Test OpenFDA API connection.
    """

    try:

        response = requests.get(

            BASE_URL,

            params={

                "limit": 1

            },

            timeout=10

        )

        return response.status_code == 200

    except Exception:

        return False
    
def fetch_drugs(limit: int = 20):
    """
    Fetch real drug information from OpenFDA.
    """

    try:

        response = requests.get(

            BASE_URL,

            params={

                "limit": limit

            },

            timeout=20

        )

        response.raise_for_status()

        data = response.json()

        return data.get("results", [])

    except Exception as e:

        print("API Error:", e)

        return []
    
def simplify_drug(drug):

    return {

        "application_number": drug.get("application_number"),

        "manufacturer":

            drug.get("openfda", {})

            .get("manufacturer_name", ["Unknown"])[0],

        "brand":

            drug.get("openfda", {})

            .get("brand_name", ["Unknown"])[0],

    }