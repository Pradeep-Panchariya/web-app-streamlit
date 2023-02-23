import streamlit as st
import pandas as pd
from datetime import datetime
import requests
import os

##title with color and emoji
#emoji : https://streamlit-emoji-shortcodes-streamlit-app-gwckff.streamlit.app/
st.title(":green[Hello, Let's build something interesting stuff] :smile:")

#subheader
st.subheader("This is a sub header")

#select_slider
import streamlit as st

selected_value = st.select_slider('Select a value',
                                  options=['Option 1', 'Option 2', 'Option 3'])

st.write('You selected:', selected_value)

###Get the country code

url = "https://api.apilayer.com/number_verification/countries"
secret = os.environ['WEATHER_API_KEY']
payload = {}
headers = {"apikey": secret}

response = requests.request("GET", url, headers=headers, data=payload)

if response.status_code != 200:
    print("Some Error Occured")
else:
    result = response.text
    st.text(result)
