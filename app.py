import streamlit as st

st.title("Welcome to the Quiz App")
st.session_state.name = st.text_input("Enter your name:")
if st.button("Start Quiz"):
    st.switch_page("pages/quiz_page.py")  # Will switch to the quiz page
