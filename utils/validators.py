"""
=========================================================
PharmaGuard AI
Validation Utilities
=========================================================
Enterprise Edition v3
=========================================================
"""

from __future__ import annotations

import re

# ==========================================================
# REQUIRED
# ==========================================================

def validate_required(value) -> bool:

    if value is None:

        return False

    if isinstance(value, str):

        return value.strip() != ""

    return True


# ==========================================================
# EMAIL
# ==========================================================

EMAIL_PATTERN = re.compile(

    r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"

)

def validate_email(

    email: str

) -> bool:

    return EMAIL_PATTERN.match(email) is not None


# ==========================================================
# POSITIVE NUMBER
# ==========================================================

def validate_positive(

    value

) -> bool:

    return value >= 0


# ==========================================================
# STOCK
# ==========================================================

def validate_stock(

    stock: int

):

    if stock < 0:

        return False, "Stock cannot be negative."

    if stock > 100000:

        return False, "Stock value is unrealistic."

    return True, ""


# ==========================================================
# AVAILABILITY
# ==========================================================

def validate_availability(

    availability: float

):

    if availability < 0:

        return False, "Availability cannot be negative."

    if availability > 100:

        return False, "Availability cannot exceed 100%."

    return True, ""


# ==========================================================
# LEAD TIME
# ==========================================================

def validate_lead_time(

    days: float

):

    if days < 0:

        return False, "Lead time cannot be negative."

    if days > 365:

        return False, "Lead time is too large."

    return True, ""


# ==========================================================
# SHIPPING TIME
# ==========================================================

def validate_shipping_time(

    days: float

):

    if days < 0:

        return False, "Shipping time cannot be negative."

    if days > 180:

        return False, "Shipping time is too large."

    return True, ""


# ==========================================================
# CONSUMPTION
# ==========================================================

def validate_consumption(

    value: float

):

    if value < 0:

        return False, "Consumption cannot be negative."

    return True, ""


# ==========================================================
# DRUG NAME
# ==========================================================

def validate_drug_name(

    name: str

):

    if len(name.strip()) < 2:

        return False, "Drug name is too short."

    return True, ""


# ==========================================================
# MANUFACTURER
# ==========================================================

def validate_manufacturer(

    manufacturer: str

):

    if len(manufacturer.strip()) < 2:

        return False, "Manufacturer name is too short."

    return True, ""


# ==========================================================
# EXPORTS
# ==========================================================

__all__ = [

    "validate_required",

    "validate_email",

    "validate_positive",

    "validate_stock",

    "validate_availability",

    "validate_lead_time",

    "validate_shipping_time",

    "validate_consumption",

    "validate_drug_name",

    "validate_manufacturer"

]