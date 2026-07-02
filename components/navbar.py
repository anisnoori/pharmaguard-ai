"""
=========================================================
PharmaGuard AI
Navbar Component
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

from config import (

    APP_NAME,

    APP_VERSION

)

# ==========================================================
# TOP NAVBAR
# ==========================================================

def render_navbar():

    user = get_current_user()

    col1, col2, col3 = st.columns(

        [5, 2, 1]

    )

    with col1:

        st.markdown(

            f"""

            ### 💊 {APP_NAME}

            """,

            unsafe_allow_html=True

        )

    with col2:

        if user:

            st.markdown(

                f"""

                **👤 {user['fullname']}**

                <br>

                {user['role']}

                """,

                unsafe_allow_html=True

            )

    with col3:

        if st.button(

            "🚪 Logout",

            use_container_width=True

        ):

            logout()


# ==========================================================
# VERSION
# ==========================================================

def show_version():

    st.caption(

        f"Version {APP_VERSION}"

    )


# ==========================================================
# SYSTEM STATUS
# ==========================================================

def system_badge():

    st.success(

        "🟢 System Online"

    )


# ==========================================================
# USER BADGE
# ==========================================================

def user_badge():

    user = get_current_user()

    if user:

        st.info(

            f"{user['fullname']} ({user['role']})"

        )


# ==========================================================
# EXPORTS
# ==========================================================

__all__ = [

    "render_navbar",

    "show_version",

    "system_badge",

    "user_badge"

]