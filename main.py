import streamlit as st
import pandas as pd
from datetime import datetime
import requests
import os, json

##title with color and emoji
#emoji : https://streamlit-emoji-shortcodes-streamlit-app-gwckff.streamlit.app/
st.title(":green[Hello, Let's build something interesting stuff] :smile:")

#---------------------------

# Set background color
st.markdown(
    """
    <style>
    body {
        background-color: #FFFF00;
    }
    </style>
    """,
    unsafe_allow_html=True
)

################################

st.text("-"*70)
st.subheader("1. Get the Country Code")

###Get the country code
def  get_country_code():
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

#Calling the country function
get_country_code()
st.text("-"*70)

st.subheader("2. Get the Exchange Rate")
## get the exchange rate of currency
get_exchange_rat
def get_exchange_rate(from_currency, to_currency, amount):

    get_symbol_url = "https://api.apilayer.com/exchangerates_data/symbols"
    exchange_secret_ley = os.environ["EXCHANGE_SECRET_KEY"]
    payload = {}
    headers= {
      "apikey": exchange_secret_ley
    }
    
    response = requests.request("GET", url, headers=headers, data = payload)
    
    status_code = response.status_code
    result = response.text
    