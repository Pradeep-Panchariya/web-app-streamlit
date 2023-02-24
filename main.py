import streamlit as st
import pandas as pd
from datetime import datetime
import requests
import os, json

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
secret_country = os.environ['COUNTRY_API_KEY']
payload = {}
headers = {"apikey": secret_country}

response = requests.request("GET", url, headers=headers, data=payload)

try:
    if response.status_code != 200:
        print("Some Error Occured")
    result = response.text
    result = json.loads(result)
    country_code_dic= {}
    for code in result:
        country_code_dic[result[code]['country_name']] = result[code]['dialling_code']
        
        
    select_country = st.selectbox('Select Country Name',country_code_dic.keys())
    st.write("You Country Code :", country_code_dic[select_country])
except Exception as e:
    st.text(e)