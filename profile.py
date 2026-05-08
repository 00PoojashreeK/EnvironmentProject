import streamlit as st
import pandas as pd

def show_profile(user):

    df = pd.read_csv("users.csv")
    data = df[df.username==user].iloc[0]

    st.header("👤 Profile")
    st.write("Name:",data["name"])
    st.write("Age:",data["age"])
    st.write("Email:",data["email"])