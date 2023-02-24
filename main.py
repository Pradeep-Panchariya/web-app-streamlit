import streamlit as st
import pandas as pd
from datetime import datetime
import requests
import os, json
import traceback

##title with color and emoji
#emoji : https://streamlit-emoji-shortcodes-streamlit-app-gwckff.streamlit.app/
st.title(":green[Hello, Let's build some interesting stuff] :smile:")

#---------------------------

# Set background color
st.markdown(
    """
    <style>
    body {
        background-color: #00FF00;
    }
    </style>
    """,
    unsafe_allow_html=True
)

################################

st.text("♥️"*70)
st.subheader("1. Get the Country Code")

###Get the country code
def  get_country_code():
    url = "https://api.apilayer.com/number_verification/countries"
    secret_country = os.environ['COUNTRY_API_KEY']
    payload = {}
    headers = {"apikey": secret_country}
    
    try:
        response = requests.request("GET", url, headers=headers, data=payload)
        result = response.text
        result = json.loads(result)
        country_code_dic= {}
        for code in result:
            country_code_dic[result[code]['country_name']] = result[code]['dialling_code']
            
            
        select_country = st.selectbox('Select Country Name',country_code_dic.keys())
        st.write(f"{select_country} Country Code : <b>{country_code_dic[select_country]}</b>",unsafe_allow_html=True)
    except Exception as e:
        st.error(traceback.format_exc())

#Calling the country function
get_country_code()
st.text("♥️"*70)

st.subheader("2. Get the Exchange Rate")
## get the exchange rate of currency

def get_symbol_exchange_rate():

    get_symbol_url = "https://api.apilayer.com/exchangerates_data/symbols"
    
    exchange_secret_key = os.environ["EXCHANGE_SECRET_KEY"]
    payload = {}
    headers= {
      "apikey": exchange_secret_key
    }

    try:
        response = requests.request("GET", get_symbol_url, headers=headers, data = payload)
        response = json.loads(response.text)
        return response
    except Exception as e:
        st.error(traceback.format_exc())
    
def get_exchange_rate():

    
    get_symbol_url = url = "https://api.apilayer.com/exchangerates_data/convert"
    exchange_secret_key = os.environ["EXCHANGE_SECRET_KEY"]

    currency_symbol = get_symbol_exchange_rate()['symbols']
    symbol_lst = []
    for currency_code, currency_name in currency_symbol.items():
        symbol_lst.append(currency_code +" : " +currency_name)

    from_currency_dropdown = st.selectbox("From : ",symbol_lst)
    to_currency_dropdown = st.selectbox("To : ",symbol_lst)
    amount = st.text_input("Enter Amount :",1)
# Convert the input to an integer and handle errors
    amount_input = 1
    try:
        amount_input = int(amount)
    except ValueError:
        st.warning("Please enter an integer value")
    except Exception as e:
        st.error(traceback.format_exc())

    submit_button = st.button("Submit")  
    payload = {
        "to" : to_currency_dropdown.split(':')[0].strip(),
        "from" : from_currency_dropdown.split(':')[0].strip(),
        "amount": amount_input
    }
    headers= {
      "apikey": exchange_secret_key
    }
    
    try:
        response = requests.get(url, headers=headers, params = (payload))
        response = json.loads(response.text)

        if submit_button:
            
            indx =['Date','From','To','Amount','Rate','Result']
            result_lst = []
            result_lst.append(response['date'])
            result_lst.append(response['query']["from"])
            result_lst.append(response['query']['to'])
            result_lst.append(response['query']['amount'])
            result_lst.append(f"{response['info']['rate']:.2f}")
            result_lst.append(f"{response['result']:.2f}")
            df = pd.DataFrame(data = [result_lst],columns=indx,index=['Output'])
            st.write("Exchange Result : ⬇️")
            st.write(df)
            st.text('♥️'*70)
            
        
    except Exception as e:
        st.error(traceback.format_exc())

get_exchange_rate()