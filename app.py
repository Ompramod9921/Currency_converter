import streamlit as st
from currency_converter import CurrencyConverter
from streamlit_lottie import st_lottie
import requests
import json
import pandas as pd
import openpyxl

c = CurrencyConverter()

st.set_page_config(page_title='Language Translator',page_icon='👽')

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

choice = st.sidebar.selectbox("Menu",("Home","Information"))
st.sidebar.write(" ")
st.sidebar.write("***")
st.sidebar.error('''CURRENCY DATA SOURCES :

This is a currency converter that uses historical rates against a reference currency (Euro).
The default source is the European Central Bank. This is the ECB historical rates for 42 currencies against the Euro since 1999.''')
st.sidebar.write("***")
st.sidebar.error("made with ❤️ by om pramod")

def load_lottiefile(filepath: str):
    with open(filepath, "r") as f :
        return json.load(f)

lottie_coding = load_lottiefile("monkey.json")

st_lottie(
    lottie_coding,
    speed= 2,
    reverse=False,
    loop=True,
    height=100,
    width= 700,
    key=None
)

if choice == "Home":
    st.markdown("<h1 style='text-align: center; color: red;'>Currency Converter</h1>", unsafe_allow_html=True)
    st.markdown("***")
    value = st.number_input("Enter the amount",step=1)
    choice1 = st.selectbox("From Currency",list(c.currencies))
    choice2 = st.selectbox("To Currency",list(c.currencies))
    res = round(c.convert(value,choice1,choice2),3)
    result = str(value)+" "+choice1+" = "+str(res)+" "+choice2
    if st.button("Convert") :
        st.markdown("***")
        st.error(result)

else:
    st.markdown("<h1 style='text-align: center; color: red;'>List of Countries,Their Currencies and Symbols</h1>", unsafe_allow_html=True)
    df = pd.read_excel("currency.xlsx")
    st.table(df)