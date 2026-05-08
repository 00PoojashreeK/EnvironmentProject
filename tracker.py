import streamlit as st
import pandas as pd

def show_tracker(user):

    st.header("🌍 Tracker")

    travel = st.selectbox("Travel",["Car","Bike","Bus","Walk"])
    distance = st.number_input("Distance",0)

    food = st.selectbox("Food",["Veg","Non-Veg"])
    plastic = st.selectbox("Plastic",["Low","Medium","High"])
    energy = st.slider("Energy",0,10)

    carbon = distance * (2 if travel=="Car" else 1 if travel=="Bike" else 0.5 if travel=="Bus" else 0)
    waste = (3 if food=="Veg" else 8) + (5 if plastic=="High" else 3 if plastic=="Medium" else 1)

    eco = max(0,100-(carbon+waste+energy*2))

    if st.button("Calculate"):

        st.metric("Eco Score",eco)
        st.progress(int(eco))

        st.write("### 💡 Suggestions")
        st.write("Use public transport 🚍" if carbon>10 else "Good travel 👍")
        st.write("Reduce plastic ♻️" if waste>8 else "Waste is good ✅")
        st.write("Save electricity ⚡" if energy>5 else "Energy efficient 💡")

        if eco>90:
            st.success("👑 Eco Champion")
        elif eco>70:
            st.success("🌳 Eco Hero")
        elif eco>50:
            st.info("🌿 Eco Friend")
        else:
            st.warning("🌱 Beginner")

        df = pd.read_csv("data.csv")
        new = pd.DataFrame([[user,carbon,waste,energy,eco]],columns=df.columns)
        pd.concat([df,new]).to_csv("data.csv",index=False)