import streamlit as st

def apply_ui():
    st.markdown("""
    <style>
    body {
        background: linear-gradient(120deg, #84fab0, #8fd3f4);
    }

    .title {
        text-align: center;
        font-size: 40px;
        font-weight: bold;
        color: #2c3e50;
        animation: fadeIn 1.2s ease-in-out;
    }

    .card {
        background: white;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0px 6px 15px rgba(0,0,0,0.2);
        margin: 10px 0;
        animation: fadeIn 0.8s ease-in-out;
    }

    .stButton>button {
        background-color: #27ae60;
        color: white;
        border-radius: 10px;
        padding: 10px;
        font-size: 16px;
    }

    @keyframes fadeIn {
        from {opacity:0; transform: translateY(20px);}
        to {opacity:1; transform: translateY(0);}
    }
    </style>
    """, unsafe_allow_html=True)