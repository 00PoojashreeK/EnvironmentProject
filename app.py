import streamlit as st
import pandas as pd
import os

from auth import login, signup
from tracker import show_tracker
from dashboard import show_dashboard
from goals import show_goals
from weather import get_weather
from profile import show_profile
from ui import apply_ui

apply_ui()
st.set_page_config(layout="wide")

# CREATE FILES
def create_file(file, cols):
    if not os.path.exists(file):
        pd.DataFrame(columns=cols).to_csv(file, index=False)

create_file("users.csv",["username","password","name","age","email"])
create_file("data.csv",["username","carbon","waste","energy","eco"])
create_file("goals.csv",["username","goal","type","days"])

# SESSION
if "login" not in st.session_state:
    st.session_state.login=False
    st.session_state.user=""
    st.session_state.page="Home"

# LOGIN / SIGNUP
if not st.session_state.login:

    st.title("🌱 EcoSphere")

    menu = st.selectbox("",["Login","Signup"])

    if menu=="Signup":
        u=st.text_input("Username")
        p=st.text_input("Password",type="password")
        n=st.text_input("Name")
        a=st.number_input("Age")
        e=st.text_input("Email")

        if st.button("Signup"):
            if signup(u,p,n,a,e):
                st.success("Account created!")

    if menu=="Login":
        u=st.text_input("Username")
        p=st.text_input("Password",type="password")

        if st.button("Login"):
            user = login(u,p)
            if not user.empty:
                st.session_state.login=True
                st.session_state.user=u
                st.session_state.page="Home"
                st.rerun()

# AFTER LOGIN
if st.session_state.login:

    df = pd.read_csv("users.csv")
    user_data = df[df.username==st.session_state.user].iloc[0]

    # TOP BAR
    st.markdown(f"### 🌱 EcoSphere | 👤 {user_data['name']}")

    # SIDEBAR
    st.sidebar.markdown(f"### 👤 {user_data['name']}")

    if st.sidebar.button("Profile"):
        st.session_state.page="Profile"

    # WEATHER
    st.sidebar.subheader("🌦 Weather")
    city = st.sidebar.text_input("City","Bangalore")

    if st.sidebar.button("Check Weather"):
        temp, desc = get_weather(city)
        if temp:
            st.sidebar.success(f"{temp}°C - {desc}")

    if st.sidebar.button("Logout"):
        st.session_state.login=False
        st.rerun()

    # BACK BUTTON
    if st.session_state.page!="Home":
        if st.button("⬅ Back"):
            st.session_state.page="Home"
            st.rerun()

    # HOME
    if st.session_state.page=="Home":

        st.info("💡 Use Tracker daily to improve your eco score!")

        col1,col2,col3 = st.columns(3)

        with col1:
            st.image("https://cdn-icons-png.flaticon.com/512/2921/2921822.png", width=80)
            if st.button("Tracker"):
                st.session_state.page="Tracker"
                st.rerun()

        with col2:
            st.image("https://cdn-icons-png.flaticon.com/512/1828/1828884.png", width=80)
            if st.button("Dashboard"):
                st.session_state.page="Dashboard"
                st.rerun()

        with col3:
            st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=80)
            if st.button("Goals"):
                st.session_state.page="Goals"
                st.rerun()

    elif st.session_state.page=="Tracker":
        show_tracker(st.session_state.user)

    elif st.session_state.page=="Dashboard":
        show_dashboard(st.session_state.user)

    elif st.session_state.page=="Goals":
        show_goals(st.session_state.user)

    elif st.session_state.page=="Profile":
        show_profile(st.session_state.user)