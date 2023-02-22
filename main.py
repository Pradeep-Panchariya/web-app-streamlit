import streamlit as st
import pandas as pd
def print_hello():
    st.text("hello again")
st.title('Hello this is a web app')
st.button("Test",on_click=print_hello)