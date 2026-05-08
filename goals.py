import streamlit as st
import pandas as pd
import os
from datetime import datetime, timedelta

def show_goals(user):

    st.header("🎯 Smart Goals")

    # -------- FILE FIX --------
    required_cols = ["username","goal","type","days","start_date"]

    if not os.path.exists("goals.csv"):
        df = pd.DataFrame(columns=required_cols)
        df.to_csv("goals.csv", index=False)
    else:
        df = pd.read_csv("goals.csv")

        # 🔥 FIX OLD FILE (ADD MISSING COLUMNS)
        for col in required_cols:
            if col not in df.columns:
                if col == "start_date":
                    df[col] = datetime.today().strftime("%Y-%m-%d")
                else:
                    df[col] = ""

        df = df[required_cols]
        df.to_csv("goals.csv", index=False)

    # -------- ADD GOAL --------
    st.subheader("➕ Create New Goal")

    goal_type = st.selectbox("Goal Type",[
        "Improve Eco Score",
        "Reduce Carbon",
        "Reduce Waste",
        "Save Energy"
    ])

    goal_value = st.number_input("Target Value", 0, 100, 80)
    days = st.number_input("Duration (days)", 1, 365, 7)

    if st.button("Save Goal"):
        today = datetime.today().strftime("%Y-%m-%d")

        new = pd.DataFrame(
            [[user,goal_value,goal_type,days,today]],
            columns=required_cols   # 🔥 ALWAYS CORRECT
        )

        df = pd.concat([df,new], ignore_index=True)
        df.to_csv("goals.csv", index=False)

        st.success("✅ Goal Saved!")
        st.balloons()

    st.markdown("---")

    # -------- SHOW GOALS --------
    user_goals = df[df.username == user]

    if not user_goals.empty:

        st.subheader("📋 Your Goals")

        for i, row in user_goals.iterrows():

            st.markdown(f"### 🎯 {row['type']}")
            st.write(f"Target: {row['goal']}")
            st.write(f"Duration: {row['days']} days")

            # -------- SAFE DATE HANDLING --------
            try:
                start_date = datetime.strptime(str(row["start_date"]), "%Y-%m-%d")
            except:
                start_date = datetime.today()

            deadline = start_date + timedelta(days=int(row["days"]))
            remaining = (deadline - datetime.today()).days

            st.write(f"⏳ Days Left: {max(0, remaining)}")

            # -------- PROGRESS --------
            data = pd.read_csv("data.csv")
            user_data = data[data.username == user]

            if not user_data.empty:

                avg = int(user_data["eco"].mean())
                progress = min(100, int((avg / max(1,row["goal"])) * 100))

                st.progress(progress)
                st.write(f"Progress: {progress}%")

                # -------- BADGES --------
                if progress >= 100:
                    st.success("🏆 Eco Champion")
                elif progress >= 75:
                    st.info("🌳 Eco Hero")
                elif progress >= 50:
                    st.info("🌿 Eco Friend")
                else:
                    st.warning("🌱 Beginner")

            st.markdown("---")

    else:
        st.info("No goals yet. Create one above 👆")