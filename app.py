import streamlit as st
from predict_page import show_predict_page
from explore_page import show_explore_page
import pandas as pd
import pickle 
from pathlib import Path
import streamlit_authenticator as stauth

#Here just load the custom CSS for styling
def load_css(file_path):
    with open(file_path) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css("styles.css")

# Authentication constants
ADMIN_USER = "admin"
ADMIN_PASS = "password"

#The function to handle user authentication
def creds_entered():
    if (st.session_state["user"].strip() == ADMIN_USER and
        st.session_state["pass"].strip() == ADMIN_PASS):
        st.session_state["authenticated"] = True
    else:
        st.session_state["authenticated"] = False
        st.error("Invalid username or password")

#The function to manage user authentication input
def authenticate_user():
    if "authenticated" not in st.session_state:
        st.text_input(label="Username:", value='', key="user")
        st.text_input(label="Password:", value='', key="pass", type="password", on_change=creds_entered)
        if st.button("Login"):
            creds_entered()
        return False
    elif st.session_state["authenticated"]:
        return True
    else:
        st.text_input(label="Username:", value='', key="user")
        st.text_input(label="Password:", value='', key="pass", type="password", on_change=creds_entered)
        if st.button("Login"):
            creds_entered()
        return False

#Hide Streamlit default elements
hide_streamlit_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

#For authenticating user
if not authenticate_user():
    st.stop()

# Page selection and display
page = st.sidebar.selectbox("Select a page:", ["Predict", "Explore"])
if page == "Predict":
    show_predict_page()
else:
    show_explore_page()
