from email.policy import default
from enum import auto
from itertools import count
from operator import imod
from telnetlib import LOGOUT
import streamlit as st1
from streamlit_option_menu import option_menu
import pandas as pd
from tracemalloc import start
import yfinance as yf
from PIL import Image
from urllib.request import urlopen
import datetime as dt


def app():

    # Load market data from Binance API
    df= pd.read_json('https://api.binance.com/api/v3/ticker/24hr')
    # st1.markdown("<hr/>", unsafe_allow_html=True)
    st1.write("<h style='font-family:Montserrat; font-weight: bold; font-size:38px;'>COMPARE ANUAL RETURNS </h>", unsafe_allow_html=True)
    st1.markdown("<hr/>", unsafe_allow_html=True)


    # col1,col2,col3 = st.columns(3)
    # with col1:
    #     col1_selection = st.selectbox('Pick 1', df.symbol, list(df.symbol).index('BTCBUSD') )
    #     col2_selection = st.selectbox('Pick 2', df.symbol, list(df.symbol).index('ETHBUSD') )
    #     col3_selection = st.selectbox('Pick 3', df.symbol, list(df.symbol).index('BNBBUSD') ) 

    tickers = ('BTC-USD','DOTB-USD','BCH-USD','ETH_USD','BNB-USD','NEO-USD','LRC-USD','ZRX-BTC','BQX-BTC')
    dropdown1 = st1.multiselect('Pick your asssets',tickers,  key = 'BTC-USD')
   
    start = st1.date_input('Start',value = pd.to_datetime('2021-01-01'))
    end = st1.date_input('End',value = pd.to_datetime('today'))
    st1.markdown("<hr/>", unsafe_allow_html=True)


    def relativeret(df2):
        rel = df2.pct_change()
        cumret = (1+rel).cumprod()-1
        cumret = cumret.fillna(0)
        return cumret

    if len(dropdown1) > 0:
        df2 = relativeret(yf.download(dropdown1,start,end)['Adj Close'])
    
        st1.line_chart(df2)
    st1.markdown("<hr/>", unsafe_allow_html=True)
    st1.write("<h style='font-family:Montserrat; font-weight: bold; font-size:38px;'>⠀\n⠀\n⠀\n⠀\n⠀\n⠀\n⠀\n⠀\n⠀\n⠀\n⠀\n⠀\n⠀ </h>", unsafe_allow_html=True)
    # st1.markdown("<hr/>", unsafe_allow_html=True)
    
        

