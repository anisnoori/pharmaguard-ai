import streamlit as st


def show_sidebar():

    with st.sidebar:

        st.markdown("# 🏥 PharmaGuard AI")

        st.markdown("---")

        menu = st.radio(

            "Navigation",

            [

                "🏠 Dashboard",

                "💊 Add Drug",

                "🤖 AI Prediction",

                "📜 History",

                "📊 Reports",

                "👤 Profile",

                "⚙️ Settings"

            ]

        )

        st.markdown("---")

        st.info(

            f"Logged in as:\n\n{st.session_state.fullname}"

        )

        if st.button("🚪 Logout"):

            from auth.session import logout

            logout()

        return menu