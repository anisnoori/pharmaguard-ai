"""
=========================================================
PharmaGuard AI
Add Drug Page
=========================================================
Enterprise Edition v3
=========================================================
"""

from __future__ import annotations

import streamlit as st

from auth.session import get_current_user

from database.database import (

    add_drug,

    get_all_drugs,

    delete_drug,

    log_activity

)

# ==========================================================
# PAGE
# ==========================================================

def show_add_drug():

    st.title("💊 Drug Management")

    st.caption(

        "Register and manage pharmaceutical products."

    )

    # ======================================================
    # FORM
    # ======================================================

    with st.form(

        "drug_form",

        clear_on_submit=True

    ):

        drug_name = st.text_input(

            "Drug Name"

        )

        manufacturer = st.text_input(

            "Manufacturer"

        )

        col1, col2 = st.columns(2)

        with col1:

            stock_level = st.number_input(

                "Stock Level",

                min_value=0,

                value=100

            )

            availability = st.slider(

                "Availability (%)",

                0,

                100,

                80

            )

        with col2:

            daily_consumption = st.number_input(

                "Daily Consumption",

                min_value=0,

                value=50

            )

            lead_time = st.number_input(

                "Lead Time (Days)",

                min_value=0,

                value=7

            )

        shipping_time = st.number_input(

            "Shipping Time (Days)",

            min_value=0,

            value=5

        )

        submit = st.form_submit_button(

            "➕ Add Drug",

            use_container_width=True

        )

    # ======================================================
    # SAVE
    # ======================================================

    if submit:

        if drug_name.strip() == "":

            st.error(

                "Drug name is required."

            )

            return

        user = get_current_user()

        success = add_drug(

            drug_name=drug_name,

            manufacturer=manufacturer,

            stock_level=stock_level,

            availability=availability,

            daily_consumption=daily_consumption,

            lead_time=lead_time,

            shipping_time=shipping_time,

            created_by=user["id"]

        )

        if success:

            log_activity(

                user["id"],

                f"Added drug: {drug_name}"

            )

            st.success(

                "Drug added successfully."

            )

            st.rerun()

        else:

            st.error(

                "Unable to add drug."

            )
    # ======================================================
    # REGISTERED DRUGS
    # ======================================================

    st.divider()

    st.subheader("📋 Registered Drugs")

    drugs = get_all_drugs()

    if len(drugs) == 0:

        st.info(

            "No drugs have been registered."

        )

        return

    for drug in drugs:

        with st.container(border=True):

            col1, col2 = st.columns([5, 1])

            with col1:

                st.markdown(

                    f"### 💊 {drug['drug_name']}"

                )

                st.write(

                    f"**Manufacturer:** {drug['manufacturer']}"

                )

                st.write(

                    f"**Stock Level:** {drug['stock_level']}"

                )

                st.write(

                    f"**Availability:** {drug['availability']}%"

                )

                st.write(

                    f"**Daily Consumption:** {drug['daily_consumption']}"

                )

                st.write(

                    f"**Lead Time:** {drug['lead_time']} Days"

                )

                st.write(

                    f"**Shipping Time:** {drug['shipping_time']} Days"

                )

            with col2:

                if st.button(

                    "🗑 Delete",

                    key=f"delete_{drug['id']}",

                    use_container_width=True

                ):

                    delete_drug(

                        drug["id"]

                    )

                    user = get_current_user()

                    if user:

                        log_activity(

                            user["id"],

                            f"Deleted drug: {drug['drug_name']}"

                        )

                    st.success(

                        "Drug deleted successfully."

                    )

                    st.rerun()


# ==========================================================
# EXPORTS
# ==========================================================

__all__ = [

    "show_add_drug"

]