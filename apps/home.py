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







    # ***************************************************************************************************************************************************************





    startt = dt.datetime.now() - dt.timedelta(days=1)
    endd = dt.datetime.now()
    

    # st.title("Today's Cryptocurrency Prices by Market Cap")
    st.markdown("<hr/>", unsafe_allow_html=True)

    st.write("<h style='font-family:Montserrat; font-weight: bold; font-size:35px;'>TODAY'S PRICE BY MARKET CAP</h>", unsafe_allow_html=True)
    st.markdown('A cryptocurrency dashboard webapp from Binance and Yfinance.')
    # st.header("Main Dashboard")
    # st.subheader("you can add more crypto ")




    #Defining tikers variable
    Bitcoin = 'BTC-USD'
    Ethereum = 'ETH-USD'
    Ripple = 'XRP-USD'
    Bitcoincash = 'BTC-USD'
    Adabcoin = 'ADABOY-USD'
    Dogecoin = 'DOGE-USD'
    Shibbcoin = 'SHIB-USD'
    Dotbcoin = 'DOT-USD'
    Matibcbcoin = 'MATIC-USD'




    # Acess data from Yahoo Finance
    BTC_Data = yf.Ticker(Bitcoin)
    ETH_Data = yf.Ticker(Ethereum)
    XRP_Data = yf.Ticker(Ripple)
    BCH_Data = yf.Ticker(Bitcoincash)
    ADAB_Data = yf.Ticker(Adabcoin)
    DOGE_Data = yf.Ticker(Dogecoin)
    SHIBB_Data = yf.Ticker(Shibbcoin)
    DOTB_Data = yf.Ticker(Dotbcoin)
    MATICB_Data = yf.Ticker(Matibcbcoin)



    #fetch history data from yahoo fin 
    BTHHis = BTC_Data.history(period="max")
    ETHHis = ETH_Data.history(period="max")
    XRPHis = XRP_Data.history(period="max")
    BCHHis = BCH_Data.history(period="max")
    ADABHis = ADAB_Data.history(period="max")
    DOGEHis = DOGE_Data.history(period="max")
    SHIBBHis = SHIBB_Data.history(period="max")
    DOTBHis = DOTB_Data.history(period="max")
    MATICBHis = MATICB_Data.history(period="max")



    BTC = yf.download(Bitcoin,start= startt, end = endd)
    ETH = yf.download(Ethereum, start= startt, end = endd)
    XRP = yf.download(Ripple, start= startt, end = endd)
    BCH = yf.download(Bitcoincash, start= startt, end = endd)
    ADAB = yf.download(Bitcoincash, start= startt, end = endd)
    DOGE = yf.download(Bitcoincash, start= startt, end = endd)
    SHIBB = yf.download(Bitcoincash, start= startt, end = endd)
    DOTB = yf.download(Bitcoincash, start= startt, end = endd)
    MATICB = yf.download(Bitcoincash, start= startt, end = endd)



    #Bitcoin 
    st.subheader("BUTCOIN ($)")
    # st.write("<h style='font-family:Montserrat; font-weight: bold; font-size:30px;'>BITCOIN</h>", unsafe_allow_html=True)
    imageBTC = Image.open(urlopen("https://s2.coinmarketcap.com/static/img/coins/64x64/1.png"))
    st.image(imageBTC)

    #Display Dataframe
    st.table(BTC)

    #Display a chart
    c1,c2 = st.columns([1,1])
    with c1:
        st.bar_chart(BTHHis.Close,width=0, height=0, use_container_width=True)
    with c2:
        st.line_chart(BTHHis.Close,width=0, height=0, use_container_width=True)




    #ETH
    st.markdown("<hr/>", unsafe_allow_html=True)
    st.subheader("ETHERUM ($)")
    imageETH = Image.open(urlopen("https://s2.coinmarketcap.com/static/img/coins/64x64/1027.png"))
    st.image(imageETH)

    #Display Dataframe
    st.table(ETH)

    #Display a chart
    c3,c4 = st.columns([1,1])
    with c3:
        st.bar_chart(ETHHis.Close,width=0, height=0, use_container_width=True)
    with c4:
        st.line_chart(ETHHis.Close,width=0, height=0, use_container_width=True)



    #XRP
    st.markdown("<hr/>", unsafe_allow_html=True)
    st.subheader("RIPPLE ($)")
    imageXRP = Image.open(urlopen("https://s2.coinmarketcap.com/static/img/coins/64x64/52.png"))
    st.image(imageXRP)

    #Display Dataframe
    st.table(XRP)

    #Display a chart
    c5,c6 = st.columns([1,1])
    with c5:
        st.bar_chart(XRPHis.Close,width=0, height=0, use_container_width=True)
    with c6:
        st.line_chart(XRPHis.Close,width=0, height=0, use_container_width=True)






    #BITCOIN CASH
    st.markdown("<hr/>", unsafe_allow_html=True)
    st.subheader("BITCOIN CASH ($)")
    imageBCH = Image.open(urlopen("https://s2.coinmarketcap.com/static/img/coins/64x64/1831.png"))
    st.image(imageBCH)

    #Display Dataframe
    st.table(BCH)

    #Display a chart
    c7,c8 = st.columns([1,1])
    with c7:
        st.bar_chart(BCHHis.Close,width=0, height=0, use_container_width=True)
    with c8:
        st.line_chart(BCHHis.Close,width=0, height=0, use_container_width=True)


    


    #ADA BOY 
    st.markdown("<hr/>", unsafe_allow_html=True)
    st.subheader("ADA BOY ($)")
    imageadab = Image.open(urlopen("https://s2.coinmarketcap.com/static/img/coins/64x64/12796.png"))
    st.image(imageadab)

    #Display Dataframe
    st.table(ADAB)

    #Display a char
    c7,c8 = st.columns([1,1])
    with c7:
        st.bar_chart(ADABHis.Close,width=0, height=0, use_container_width=True)
    with c8:
        st.line_chart(ADABHis.Close,width=0, height=0, use_container_width=True)







    #Dogecoin
    st.markdown("<hr/>", unsafe_allow_html=True)
    st.subheader("Dogecoin ($)")
    imageDOGE = Image.open(urlopen("https://s2.coinmarketcap.com/static/img/coins/64x64/74.png"))
    st.image(imageDOGE)

    #Display Dataframe
    st.table(DOGE)

    #Display a chart
    c9,c10 = st.columns([1,1])
    with c9:
        st.bar_chart(DOGEHis.Close,width=0, height=0, use_container_width=True)
    with c10:
        st.line_chart(DOGEHis.Close,width=0, height=0, use_container_width=True)





    #SHIBA INU
    st.markdown("<hr/>", unsafe_allow_html=True)
    st.subheader("SHIBA INU ($)")
    imageSHIBB = Image.open(urlopen("https://s2.coinmarketcap.com/static/img/coins/64x64/5994.png"))
    st.image(imageSHIBB)

    #Display Dataframe
    st.table(SHIBB)

    #Display a chart
    c11,c12 = st.columns([1,1])
    with c11:
        st.bar_chart(SHIBBHis.Close,width=0, height=0, use_container_width=True)
    with c12:
        st.line_chart(SHIBBHis.Close,width=0, height=0, use_container_width=True)
    





    #Dotcoin  
    st.markdown("<hr/>", unsafe_allow_html=True)
    st.subheader("Dotcoin ($)")
    imageDOTB = Image.open(urlopen("https://s2.coinmarketcap.com/static/img/coins/64x64/6636.png"))
    st.image(imageDOTB)

    #Display Dataframe
    st.table(DOTB)

    #Display a chart
    c13,c14 = st.columns([1,1])
    with c13:
        st.bar_chart(DOTBHis.Close,width=0, height=0, use_container_width=True)
    with c14:
        st.line_chart(DOTBHis.Close,width=0, height=0, use_container_width=True)




    #Polygon 
    st.markdown("<hr/>", unsafe_allow_html=True)
    st.subheader("Polygon ($)")
    imageMATICB = Image.open(urlopen("https://s2.coinmarketcap.com/static/img/coins/64x64/2010.png"))
    st.image(imageMATICB)

    #Display Dataframe
    st.table(MATICB)

    #Display a chart
    c15,c16 = st.columns([1,1])
    with c15:
        st.bar_chart(MATICBHis.Close,width=0, height=0, use_container_width=True)
    with c16:
        st.line_chart(MATICBHis.Close,width=0, height=0, use_container_width=True)




    # st.markdown("""
    # <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
    # <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous"></script>
    # <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
    # """, unsafe_allow_html=True)



