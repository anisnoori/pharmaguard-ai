"""
=========================================================
PharmaGuard AI
app.py
Enterprise Edition v3
=========================================================
"""

from __future__ import annotations

import streamlit as st

from config import APP_NAME, APP_VERSION

from database.database import initialize_database

from auth.session import (

    initialize_session,

    check_session_timeout,

    is_logged_in

)

from auth.login import show_login

from auth.register import show_register

from components.layout import render_layout

from views.dashboard import show_dashboard

from views.add_drug import show_add_drug

from views.prediction import show_prediction

from views.history import show_history

from views.reports import show_reports

from views.profile import show_profile

from views.settings import show_settings

# ==========================================================
# PAGE CONFIG
# ==========================================================

st.set_page_config(

    page_title=APP_NAME,

    page_icon="💊",

    layout="wide",

    initial_sidebar_state="expanded"

)
# ==========================================================
# CSS
# ==========================================================

def load_css(filename: str):

    try:

        with open(filename, encoding="utf-8") as f:

            st.markdown(

                f"<style>{f.read()}</style>",

                unsafe_allow_html=True

            )

    except FileNotFoundError:

        pass
# ==========================================================
# INITIALIZATION
# ==========================================================

initialize_database()

initialize_session()

check_session_timeout()

# ----------------------------------------------------------
# Theme
# ----------------------------------------------------------

if "dark_mode" not in st.session_state:

    st.session_state["dark_mode"] = False

if st.session_state.get("dark_mode", False):

    load_css("assets/dark.css")

else:

    load_css("assets/style.css")
    import os


# ==========================================================
# LOGIN
# ==========================================================

if not is_logged_in():

    st.title(APP_NAME)

    st.caption(f"Version {APP_VERSION}")

    tab1, tab2 = st.tabs(

        [

            "Login",

            "Register"

        ]

    )

    with tab1:

        show_login()

    with tab2:

        show_register()

    st.stop()

# ==========================================================
# ROUTER
# ==========================================================

page = render_layout("Dashboard")

if page == "dashboard":

    show_dashboard()

elif page == "add_drug":

    show_add_drug()

elif page == "prediction":

    show_prediction()

elif page == "history":

    show_history()

elif page == "reports":

    show_reports()

elif page == "profile":

    show_profile()

elif page == "settings":

    show_settings()

# ==========================================================
# FOOTER
# ==========================================================

st.divider()

st.caption(

    f"{APP_NAME} © 2026 | Version {APP_VERSION}"

)
