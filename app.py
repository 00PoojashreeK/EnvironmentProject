import streamlit as st

# ✅ MUST BE FIRST
st.set_page_config(layout="wide")

import pandas as pd
import os

from auth import login, signup
from tracker import show_tracker
from dashboard import show_dashboard
from goals import show_goals
from weather import get_weather
from profile import show_profile
from ui import apply_ui

# APPLY UI
apply_ui()

# ---------------- FILE CREATION ----------------
def create_file(file, cols):
    if not os.path.exists(file):
        pd.DataFrame(columns=cols).to_csv(file, index=False)

create_file("users.csv", ["username", "password", "name", "age", "email"])
create_file("data.csv", ["username", "carbon", "waste", "energy", "eco"])
create_file("goals.csv", ["username", "goal", "type", "days", "start_date"])

# ---------------- SESSION ----------------
if "login" not in st.session_state:
    st.session_state.login = False
    st.session_state.user = ""
    st.session_state.page = "Home"

# ---------------- AUTH PAGE ----------------
if not st.session_state.login:

    st.markdown("""
    <style>

    .stApp {
        background: linear-gradient(135deg,#d4ecdb,#f4fff7);
    }

    .center-box {
        display:flex;
        justify-content:center;
        align-items:flex-start;
        padding-top:40px;
    }

    .card {
        background:white;
        width:400px;
        padding:40px;
        border-radius:25px;
        box-shadow:0 15px 40px rgba(0,0,0,0.15);
    }

    .title {
        text-align:center;
        font-size:34px;
        font-weight:800;
        color:#27ae60;
        margin-bottom:10px;
    }

    .subtitle {
        text-align:center;
        color:gray;
        margin-bottom:25px;
    }

    div.stButton > button {
        width:100%;
        border-radius:12px;
        height:45px;
        background:#2ecc71;
        color:white;
        border:none;
        font-size:16px;
        font-weight:600;
        transition:0.3s;
    }

    div.stButton > button:hover {
        transform:scale(1.03);
        background:#27ae60;
    }

    </style>
    """, unsafe_allow_html=True)

    st.markdown("<div class='center-box'>", unsafe_allow_html=True)
    st.markdown("<div class='card'>", unsafe_allow_html=True)

    st.markdown("<div class='title'>🌱 EcoSphere</div>", unsafe_allow_html=True)
    st.markdown(
        "<div class='subtitle'>Track your eco lifestyle smarter</div>",
        unsafe_allow_html=True
    )

    menu = st.radio(
        "",
        ["Login", "Signup"],
        horizontal=True
    )

    # -------- SIGNUP --------
    if menu == "Signup":

        st.subheader("Create Account")

        u = st.text_input("Username")
        p = st.text_input("Password", type="password")
        n = st.text_input("Full Name")

        a = st.number_input(
            "Age",
            min_value=1,
            max_value=100,
            step=1,
            format="%d"
        )

        e = st.text_input("Email")

        if st.button("✨ Create Account"):
            if signup(u, p, n, int(a), e):
                st.success("Account created successfully!")
            else:
                st.error("Username already exists")

    # -------- LOGIN --------
    if menu == "Login":

        st.subheader("Welcome Back")

        u = st.text_input("Username")
        p = st.text_input("Password", type="password")

        if st.button("🚀 Login"):

            user = login(u, p)

            if not user.empty:
                st.session_state.login = True
                st.session_state.user = u
                st.session_state.page = "Home"
                st.rerun()

            else:
                st.error("Invalid Username or Password")

    st.markdown("</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

# ---------------- AFTER LOGIN ----------------
if st.session_state.login:

    df = pd.read_csv("users.csv")
    user_data = df[df.username == st.session_state.user].iloc[0]

    # TOP BAR
    st.markdown(f"### 🌱 EcoSphere | 👤 {user_data['name']}")

    # SIDEBAR
    st.sidebar.markdown(f"### 👤 {user_data['name']}")

    if st.sidebar.button("Profile"):
        st.session_state.page = "Profile"

    # WEATHER
    st.sidebar.subheader("🌦 Weather")

    city = st.sidebar.text_input("City", "Bangalore")

    if st.sidebar.button("Check Weather"):

        temp, desc = get_weather(city)

        if temp:
            st.sidebar.success(f"{temp}°C - {desc}")

    if st.sidebar.button("Logout"):
        st.session_state.login = False
        st.rerun()

    # BACK BUTTON
    if st.session_state.page != "Home":

        if st.button("⬅ Back"):
            st.session_state.page = "Home"
            st.rerun()

    # HOME PAGE
    if st.session_state.page == "Home":

        st.info("💡 Use Tracker daily to improve your eco score!")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.image(
                "https://cdn-icons-png.flaticon.com/512/2921/2921822.png",
                width=70
            )

            if st.button("Tracker"):
                st.session_state.page = "Tracker"
                st.rerun()

        with col2:
            st.image(
                "https://cdn-icons-png.flaticon.com/512/1828/1828884.png",
                width=70
            )

            if st.button("Dashboard"):
                st.session_state.page = "Dashboard"
                st.rerun()

        with col3:
            st.image(
                "https://cdn-icons-png.flaticon.com/512/3135/3135715.png",
                width=70
            )

            if st.button("Goals"):
                st.session_state.page = "Goals"
                st.rerun()

    elif st.session_state.page == "Tracker":
        show_tracker(st.session_state.user)

    elif st.session_state.page == "Dashboard":
        show_dashboard(st.session_state.user)

    elif st.session_state.page == "Goals":
        show_goals(st.session_state.user)

    elif st.session_state.page == "Profile":
        show_profile(st.session_state.user)