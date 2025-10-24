pip install streamlit pandas
import streamlit as st
import panda as pd

# Title of App
st.title("Web Development Lab01")

# Assignment Data 
# TODO: Fill out your team number, section, and team members

st.header("CS 1301")
st.subheader("Web Development - Section E")
st.subheader("Maximilian Siry")

st.page_link("your_app.py", label="Home")
st.page_link("pages/info.py", label="Spongebob's Portfolio")
st.page_link("pages/Maximilian's Portfolio.py", label="Maximilian's Portfolio", disabled=True)


# Introduction
# TODO: Write a quick description for all of your pages in this lab below, in the form:
#       1. **Spongebob's Portfolio**: Spongebob's Example Portfolio
#       2. **Maximilian's Portfolio**: Maximilian's own portfolio
#       3. **Page Name**: Description
#       4. **Page Name**: Description

st.write("""
Welcome to our Streamlit Web Development Lab01 app! You can navigate between the pages using the sidebar to the left. The following pages are:

1. **Spongebob's Portfolio**: Spongebob's Own Portfolio
2. **Maximilian's Portfolio**: My Own Portfolio
3.
4.

""")

