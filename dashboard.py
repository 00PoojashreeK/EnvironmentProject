import streamlit as st
import pandas as pd
import plotly.express as px

def show_dashboard(user):

    st.header("📊 Smart Eco Dashboard")

    df = pd.read_csv("data.csv")
    user_df = df[df.username == user]

    if user_df.empty:
        st.warning("No data yet. Go to Tracker and add data.")
        return

    # -------- LATEST VALUES --------
    latest = user_df.iloc[-1]

    # -------- METRIC CARDS --------
    col1, col2, col3, col4 = st.columns(4)

    col1.metric("🌱 Eco Score", int(latest["eco"]))
    col2.metric("🌍 Carbon", round(latest["carbon"],2))
    col3.metric("♻️ Waste", round(latest["waste"],2))
    col4.metric("⚡ Energy", round(latest["energy"],2))

    st.markdown("---")

    # -------- ECO SCORE GRAPH --------
    st.subheader("🌱 Eco Score Trend")

    fig1 = px.line(
        user_df,
        y="eco",
        title="Eco Score Over Time",
        markers=True,
        color_discrete_sequence=["green"]
    )
    st.plotly_chart(fig1, use_container_width=True)

    # -------- SEPARATE GRAPHS --------
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("🌍 Carbon Trend")
        fig2 = px.line(user_df, y="carbon", color_discrete_sequence=["red"])
        st.plotly_chart(fig2, use_container_width=True)

    with col2:
        st.subheader("⚡ Energy Trend")
        fig3 = px.line(user_df, y="energy", color_discrete_sequence=["orange"])
        st.plotly_chart(fig3, use_container_width=True)

    st.subheader("♻️ Waste Trend")
    fig4 = px.line(user_df, y="waste", color_discrete_sequence=["blue"])
    st.plotly_chart(fig4, use_container_width=True)

    # -------- PIE CHART --------
    st.subheader("📊 Impact Distribution")

    pie_data = pd.DataFrame({
        "Category": ["Carbon","Waste","Energy"],
        "Value": [
            latest["carbon"],
            latest["waste"],
            latest["energy"]
        ]
    })

    fig5 = px.pie(
        pie_data,
        names="Category",
        values="Value",
        title="Your Environmental Impact",
        color_discrete_sequence=["red","blue","orange"]
    )

    st.plotly_chart(fig5, use_container_width=True)

    # -------- COMPARISON --------
    if len(user_df) > 1:
        st.subheader("📅 Daily Comparison")

        today = user_df.iloc[-1]["eco"]
        prev = user_df.iloc[-2]["eco"]

        col1, col2 = st.columns(2)
        col1.metric("Today", int(today))
        col2.metric("Yesterday", int(prev))

        if today > prev:
            st.success("👍 You improved today!")
        elif today < prev:
            st.warning("⚠️ Try to improve tomorrow!")
        else:
            st.info("😐 Same performance")

    # -------- INSIGHT --------
    st.subheader("💡 Insight")

    if latest["carbon"] > latest["waste"]:
        st.write("🚗 Travel is your biggest impact. Try reducing it.")
    else:
        st.write("♻️ Waste is higher. Reduce plastic usage.")
