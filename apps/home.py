from email.policy import default
from enum import auto
from operator import imod
from telnetlib import LOGOUT
import streamlit as st
# from streamlit_option_menu import option_menu
import pandas as pd
from tracemalloc import start
import yfinance as yf
from PIL import Image
from urllib.request import urlopen
import datetime as dt
import mplfinance as mpf
import plotly.graph_objects as go


def app():
    # color: #021945;
 


    kpi01, kpi02,kpi033 = st.columns([1,15,1])
    with kpi01: 
        logo = Image.open('img/logo.png')
        st.image(logo, caption=None, width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")

    with kpi02:   
        # st.title('Cryptodab')
        st.write("<h style='font-family:Montserrat; font-weight: bold; font-size:45px;'>CRYPTODAB</h>", unsafe_allow_html=True)   
        # st.info('Credit: Created by Harsh Singh - [Team HRS](https://github.com/Harshstag)')     
    with kpi033: 
        logo = Image.open('img/TeamHrs.png')
        st.image(logo, caption=None, width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")


    # st.caption('Credit: Created by Harsh Singh - [Team HRS](https://github.com/Harshstag) ')
    # st.markdown("<hr/>", unsafe_allow_html=True)

    st.caption("<h style='font-family:Montserrat; font-weight: bold; font-size:8px;'>CREADIT : CREATED BY HARSH SINGH & ARSHAD KHAN - [ BY [HARSHSTAG](https://github.com/Harshstag) & CP - [BIGDWAF43](https://github.com/bigdwarf43) ] </h>", unsafe_allow_html=True)    
        
    
   
    st.caption('Disclaimer: “Crypto products and [non-fungible tokens] are unregulated and can be highly risky. There may be no regulatory recourse for any loss from such transactions. The Website will not be responsible for any losses, damages or claims arising from cryptomarket.')
    # st.write("<h style=' font-size:20px;'>A cryptocurrency dashboard webapp from Binance and Yfinance.</h>", unsafe_allow_html=True)     
    # st.write("<h style=' color: #000000; font-size:15px;'>Disclaimer: “Crypto products and [non-fungible tokens] are unregulated and can be highly risky. There may be no regulatory recourse for any loss from such transactions. The Website will not be responsible for any losses, damages or claims arising from cryptomarket.”</h>", unsafe_allow_html=True)

    # st.header('**Selected Price**')
    st.markdown("<hr/>", unsafe_allow_html=True)

    st.write("<h style='font-family:Montserrat; font-weight: bold; font-size:30px;'>SELECTED PRICE</h>", unsafe_allow_html=True)


    # Load market data from Binance API
    df = pd.read_json('https://api.binance.com/api/v3/ticker/24hr')

    # Custom function for rounding values
    def round_value(input_value):
        if input_value.values > 1:
            a = float(round(input_value, 2))
        else:
            a = float(round(input_value, 8))
        return a

    col1, col2, col3 = st.columns(3)

    # Widget (Cryptocurrency selection box)
    with col1:
        col1_selection = st.sidebar.selectbox('Price 1', df.symbol, list(df.symbol).index('BTCBUSD') )
        col2_selection = st.sidebar.selectbox('Price 2', df.symbol, list(df.symbol).index('ETHBUSD') )
        col3_selection = st.sidebar.selectbox('Price 3', df.symbol, list(df.symbol).index('BNBBUSD') ) 
    with col2:
        col4_selection = st.sidebar.selectbox('Price 4', df.symbol, list(df.symbol).index('XRPBUSD') )
        col5_selection = st.sidebar.selectbox('Price 5', df.symbol, list(df.symbol).index('ADABUSD') )
        col6_selection = st.sidebar.selectbox('Price 6', df.symbol, list(df.symbol).index('DOGEBUSD') )
    with col3:
        col7_selection = st.sidebar.selectbox('Price 7', df.symbol, list(df.symbol).index('SHIBBUSD') )
        col8_selection = st.sidebar.selectbox('Price 8', df.symbol, list(df.symbol).index('DOTBUSD') )
        col9_selection = st.sidebar.selectbox('Price 9', df.symbol, list(df.symbol).index('MATICBUSD') )

    # DataFrame of selected Cryptocurrency
    col1_df = df[df.symbol == col1_selection]
    col2_df = df[df.symbol == col2_selection]
    col3_df = df[df.symbol == col3_selection]
    col4_df = df[df.symbol == col4_selection]
    col5_df = df[df.symbol == col5_selection]
    col6_df = df[df.symbol == col6_selection]
    col7_df = df[df.symbol == col7_selection]
    col8_df = df[df.symbol == col8_selection]
    col9_df = df[df.symbol == col9_selection]


    # st.write(col1_df)
    # st.write(col2_df)
    # st.write(col3_df)
    # st.write(col4_df)
    # st.write(col5_df)
    # st.write(col6_df)
    # st.write(col7_df)
    # st.write(col8_df)
    # st.write(col9_df)

    # Apply a custom function to conditionally round values
    with col1:
        col1_price = round_value(col1_df.weightedAvgPrice)
        col2_price = round_value(col2_df.weightedAvgPrice)
        col3_price = round_value(col3_df.weightedAvgPrice)
    with col2:
        col4_price = round_value(col4_df.weightedAvgPrice)
        col5_price = round_value(col5_df.weightedAvgPrice)
        col6_price = round_value(col6_df.weightedAvgPrice)
    with col3:
        col7_price = round_value(col7_df.weightedAvgPrice)
        col8_price = round_value(col8_df.weightedAvgPrice)
        col9_price = round_value(col9_df.weightedAvgPrice)

    # Select the priceChangePercent column
    col1_percent = f'{float(col1_df.priceChangePercent)}%'
    col2_percent = f'{float(col2_df.priceChangePercent)}%'
    col3_percent = f'{float(col3_df.priceChangePercent)}%'
    col4_percent = f'{float(col4_df.priceChangePercent)}%'
    col5_percent = f'{float(col5_df.priceChangePercent)}%'
    col6_percent = f'{float(col6_df.priceChangePercent)}%'
    col7_percent = f'{float(col7_df.priceChangePercent)}%'
    col8_percent = f'{float(col8_df.priceChangePercent)}%'
    col9_percent = f'{float(col9_df.priceChangePercent)}%'

    # Create a metrics price box
    with col1:
        st.metric(col1_selection, col1_price, col1_percent)
        st.metric(col2_selection, col2_price, col2_percent)
        st.metric(col3_selection, col3_price, col3_percent)
    with col2:
        st.metric(col4_selection, col4_price, col4_percent)
        st.metric(col5_selection, col5_price, col5_percent)
        st.metric(col6_selection, col6_price, col6_percent)
    with col3:
        st.metric(col7_selection, col7_price, col7_percent)
        st.metric(col8_selection, col8_price, col8_percent)
        st.metric(col9_selection, col9_price, col9_percent)

    # st.header('**All Price**')
    st.markdown("<hr/>", unsafe_allow_html=True)
    st.write("<h style='font-family:Montserrat; font-weight: bold; font-size:30px;'>ALL PRICES</h>", unsafe_allow_html=True)
    # st.markdown("<hr/>", unsafe_allow_html=True)


    st.dataframe(df)

    # *******************************************************************************************************************************************


    # TODAY = date.today().strftime("%Y-%m-%d")
    startt = dt.datetime.now() - dt.timedelta(days=1)
    TODAY = dt.datetime.now()

    # st.title('Crypto Volume Chart ')
    st.markdown("<hr/>", unsafe_allow_html=True)
    st.write("<h style='font-family:Montserrat; font-weight: bold; font-size:45px;'>QUICK ACCESS</h>", unsafe_allow_html=True)
    st.markdown("<hr/>", unsafe_allow_html=True)

    title = st.text_input("Search Crypto","BTC-USD")
    df = yf.download({title},strat='2022-10-05',end=TODAY)

    
    #Defining tikers variable
    Bitcoin = title
    # Acess data from Yahoo Finance
    BTC_Data = yf.Ticker(Bitcoin)
    #fetch history data from yahoo fin 
    BTHHis = BTC_Data.history(period="max")
    BTC = yf.download(Bitcoin,start= startt, end =TODAY)

    #Bitcoin 
    st.subheader(title)
    # st.write("<h style='font-family:Montserrat; font-weight: bold; font-size:30px;'>BITCOIN</h>", unsafe_allow_html=True)
    # imageBTC = Image.open(urlopen("https://s2.coinmarketcap.com/static/img/coins/64x64/1.png"))
    # st.image(imageBTC)

    #Display Dataframe
    st.table(BTC)
    

    st.markdown("<hr/>", unsafe_allow_html=True)
    st.write("<h style='font-family:Montserrat; font-weight: bold; font-size:20px;'>TODAY'S PRICE BY MARKET CAP</h>", unsafe_allow_html=True)
    kpi0, kpi1 = st.columns([1,1])
    with kpi0:
        st.bar_chart(BTHHis.Close,width=0, height=0, use_container_width=True)
        st.write("<h style='font-family:Montserrat; font-weight: bold; font-size:20px;'>PRICE CHART</h>", unsafe_allow_html=True)
    with kpi1:
        st.area_chart(data=df, width=0, height=0, use_container_width=True) #Display a chart
        st.write("<h style='font-family:Montserrat; font-weight: bold; font-size:20px;'>VOLUME CHART</h>", unsafe_allow_html=True)
    st.markdown("<hr/>", unsafe_allow_html=True)

