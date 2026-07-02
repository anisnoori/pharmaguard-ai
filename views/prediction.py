"""
=========================================================
PharmaGuard AI
Prediction Page
=========================================================
Enterprise Edition v3
=========================================================
"""

from __future__ import annotations

from datetime import datetime

import streamlit as st

from ai.predict import predict_risk

from ai.recommendation import (

    build_prediction_result

)

from ai.explainability import (

    explain_prediction

)

from auth.session import (

    get_current_user

)

from database.database import (

    get_all_drugs,

    save_prediction,

    log_activity

)

# ==========================================================
# PAGE
# ==========================================================

def show_prediction():

    st.title("🤖 AI Risk Prediction")

    st.caption(

        "Predict pharmaceutical supply chain disruption risk."

    )

    drugs = get_all_drugs()

    if len(drugs) == 0:

        st.warning(

            "No registered drugs found."

        )

        return

    drug_names = [

        drug["drug_name"]

        for drug in drugs

    ]

    selected_name = st.selectbox(

        "Select Drug",

        drug_names

    )

    selected_drug = next(

        drug

        for drug in drugs

        if drug["drug_name"] == selected_name

    )

    # ======================================================
    # DRUG INFO
    # ======================================================

    st.divider()

    st.subheader("💊 Drug Information")

    col1, col2 = st.columns(2)

    with col1:

        st.write(

            "**Drug Name:**",

            selected_drug["drug_name"]

        )

        st.write(

            "**Manufacturer:**",

            selected_drug["manufacturer"]

        )

        st.write(

            "**Stock Level:**",

            selected_drug["stock_level"]

        )

        st.write(

            "**Availability:**",

            f"{selected_drug['availability']}%"

        )

    with col2:

        st.write(

            "**Daily Consumption:**",

            selected_drug["daily_consumption"]

        )

        st.write(

            "**Lead Time:**",

            selected_drug["lead_time"]

        )

        st.write(

            "**Shipping Time:**",

            selected_drug["shipping_time"]

        )

    st.divider()

    if not st.button(

        "🤖 Predict Risk",

        use_container_width=True,

        type="primary"

    ):

        return

    # ======================================================
    # AI PREDICTION
    # ======================================================

    score = predict_risk(

        availability=selected_drug["availability"],

        stock=selected_drug["stock_level"],

        sold=selected_drug["daily_consumption"],

        revenue=0,

        shipping_cost=0,

        lead_time=selected_drug["lead_time"],

        order_quantity=selected_drug["stock_level"],

        shipping_time=selected_drug["shipping_time"],

        manufacturing_time=selected_drug["lead_time"]

    )

    prediction = build_prediction_result(

        score

    )

        # ======================================================
    # RESULT
    # ======================================================

    st.divider()

    st.subheader("📊 Prediction Result")

    c1, c2, c3 = st.columns(3)

    with c1:

        st.metric(

            "Risk Score",

            prediction["risk_score"]

        )

    with c2:

        st.metric(

            "Risk Level",

            prediction["risk_level"]

        )

    with c3:

        st.metric(

            "Priority",

            prediction["priority"]

        )

    # ======================================================
    # STATUS CARD
    # ======================================================

    st.markdown(

        f"""

        <div style="

            background:{prediction['color']};

            color:white;

            padding:20px;

            border-radius:12px;

            text-align:center;

            font-size:24px;

            font-weight:bold;

        ">

            {prediction["icon"]}

            {prediction["risk_level"]}

        </div>

        """,

        unsafe_allow_html=True

    )

    st.info(

        prediction["impact"]

    )

    # ======================================================
    # RECOMMENDATIONS
    # ======================================================

    st.subheader("💡 AI Recommendations")

    for recommendation in prediction["recommendations"]:

        st.success(

            recommendation

        )

    # ======================================================
    # EXPLAINABILITY
    # ======================================================

    st.subheader(

        "🧠 AI Explanation"

    )

    explanations = explain_prediction(

        availability=selected_drug["availability"],

        stock=selected_drug["stock_level"],

        daily_consumption=selected_drug["daily_consumption"],

        lead_time=selected_drug["lead_time"],

        shipping_time=selected_drug["shipping_time"]

    )

    for item in explanations:

        if item.strip():

            st.info(item)

      # ======================================================
    # SAVE PREDICTION
    # ======================================================

    user = get_current_user()

    if user is not None:

        save_prediction(

            drug_name=selected_drug["drug_name"],

            risk_score=prediction["risk_score"],

            risk_level=prediction["risk_level"],

            predicted_by=user["id"]

        )

        log_activity(

            user["id"],

            f"Predicted risk for {selected_drug['drug_name']}"

        )

    # ======================================================
    # TIMESTAMP
    # ======================================================

    st.caption(

        "Prediction Time: "

        + datetime.now().strftime(

            "%Y-%m-%d %H:%M:%S"

        )

    )

    # ======================================================
    # EXPORT REPORT
    # ======================================================

    report = f"""
PharmaGuard AI Prediction Report

Drug Name: {selected_drug['drug_name']}
Manufacturer: {selected_drug['manufacturer']}

Risk Score: {prediction['risk_score']}
Risk Level: {prediction['risk_level']}
Priority: {prediction['priority']}

Business Impact:
{prediction['impact']}

Recommendations:
"""

    for rec in prediction["recommendations"]:

        report += f"\n- {rec}"

    st.download_button(

        "📄 Export Report",

        data=report,

        file_name=f"{selected_drug['drug_name']}_prediction.txt",

        mime="text/plain",

        use_container_width=True

    )

    # ======================================================
    # SUCCESS
    # ======================================================

    st.success(

        "Prediction completed successfully."

    )


# ==========================================================
# EXPORTS
# ==========================================================

__all__ = [

    "show_prediction"

]          