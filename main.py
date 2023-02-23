import streamlit as st
import pandas as pd
from datetime import datetime

##title with color and emoji
#emoji : https://streamlit-emoji-shortcodes-streamlit-app-gwckff.streamlit.app/
st.title(":green[Hello, Let's build something interesting stuff] :smile:")


#subheader
st.subheader("This is a sub header")


#select_slider
import streamlit as st

selected_value = st.select_slider(
    'Select a value',
    options=['Option 1', 'Option 2', 'Option 3']
)

st.write('You selected:', selected_value)
