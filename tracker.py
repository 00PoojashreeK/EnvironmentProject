import streamlit as st
import pandas as pd

def show_tracker(user):

    st.header("🌍 Tracker")

    # -------- TRAVEL INPUT --------
    travel = st.selectbox("Travel Mode", ["Car","Bike","Bus","Walk"])

    unit = st.selectbox("Distance Unit", ["Kilometers (km)", "Meters (m)"])
    distance = st.number_input("Enter Distance", min_value=0.0)

    # Convert to KM
    if unit == "Meters (m)":
        distance = distance / 1000

    # -------- OTHER INPUTS --------
    food = st.selectbox("Food Type", ["Veg","Non-Veg"])
    plastic = st.selectbox("Plastic Usage", ["Low","Medium","High"])

    # -------- ENERGY (REALISTIC) --------
    st.subheader("⚡ Energy Usage")

    ac_hours = st.number_input("AC Usage (hours)", 0, 24)
    fan_hours = st.number_input("Fan Usage (hours)", 0, 24)
    devices = st.number_input("Devices Used", 0, 10)

    # 🔥 Balanced energy formula
    energy = (ac_hours * 1.2) + (fan_hours * 0.2) + (devices * 0.3)

    # -------- CARBON CALCULATION --------
    if travel == "Car":
        carbon = distance * 2
    elif travel == "Bike":
        carbon = distance * 1.2
    elif travel == "Bus":
        carbon = distance * 0.6
    else:
        carbon = distance * 0.05

    # -------- WASTE --------
    waste = (2 if food=="Veg" else 5) + (4 if plastic=="High" else 2 if plastic=="Medium" else 1)

    # -------- ECO SCORE (FIXED 🔥) --------
    eco = 100 - (carbon * 1.2 + waste * 2 + energy * 1.5)

    # ✅ LIMIT RANGE
    eco = max(10, min(100, eco))

    # -------- OUTPUT --------
    if st.button("Calculate"):

        st.metric("🌱 Eco Score", int(eco))
        st.progress(int(eco))

        st.write("### 💡 Suggestions")

        if carbon > 20:
            st.warning("🚗 Reduce travel or use public transport")
        else:
            st.success("👍 Travel is eco-friendly")

        if waste > 8:
            st.warning("♻️ Reduce plastic usage")
        else:
            st.success("✅ Waste level is good")

        if energy > 15:
            st.warning("⚡ High energy usage, reduce AC/devices")
        else:
            st.success("💡 Energy usage is efficient")

        # -------- BADGES --------
        if eco >= 85:
            st.success("👑 Eco Champion")
        elif eco >= 65:
            st.success("🌳 Eco Hero")
        elif eco >= 40:
            st.info("🌿 Eco Friend")
        else:
            st.warning("🌱 Beginner")

        # -------- SAVE DATA --------
        df = pd.read_csv("data.csv")
        new = pd.DataFrame([[user, carbon, waste, energy, eco]], columns=df.columns)
        pd.concat([df, new]).to_csv("data.csv", index=False)