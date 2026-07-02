"""
=========================================================
PharmaGuard AI
Main Layout
=========================================================
Enterprise Edition v3
=========================================================
"""

from __future__ import annotations

import streamlit as st

from auth.session import (
    get_current_user,
    logout
)

# ==========================================================
# MENU
# ==========================================================

MENU_ITEMS = {

    "🏠 Dashboard": "dashboard",

    "💊 Add Drug": "add_drug",

    "🤖 Prediction": "prediction",

    "📜 History": "history",

    "📊 Reports": "reports",

    "👤 Profile": "profile",

    "⚙️ Settings": "settings"

}

# ==========================================================
# HEADER
# ==========================================================

def render_header(title: str) -> None:

    col1, col2 = st.columns([5, 1])

    with col1:

        st.title(title)

    with col2:

        user = get_current_user()

        if user:

            st.caption(f"👤 {user['fullname']}")

# ==========================================================
# SIDEBAR
# ==========================================================

def render_sidebar():

    with st.sidebar:

        st.markdown("# 💊 PharmaGuard AI")

        st.caption("AI-Driven Supply Chain Platform")

        st.divider()

        user = get_current_user()

        if user:

            st.success(user["fullname"])

            st.caption(user["role"])

            st.caption(user["email"])

        st.divider()

        page = st.radio(

            "Navigation",

            list(MENU_ITEMS.keys()),

            label_visibility="collapsed"

        )

        st.divider()

        if st.button(

            "🚪 Logout",

            use_container_width=True

        ):

            logout()

        return MENU_ITEMS[page]

# ==========================================================
# FOOTER
# ==========================================================

def render_footer():

    st.divider()

    st.caption(

        "© 2026 PharmaGuard AI | AI-Driven Early Warning System"

    )

# ==========================================================
# COMPLETE LAYOUT
# ==========================================================

def render_layout(page_title: str):

    render_header(page_title)

    page = render_sidebar()


    return page


# ==========================================================
# EXPORTS
# ==========================================================

__all__ = [

    "render_layout",

    "render_header",

    "render_sidebar",

    "render_footer"

]