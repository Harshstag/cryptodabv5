from tracemalloc import start
import streamlit as st
import yfinance as yf
from PIL import Image
from urllib.request import urlopen
import datetime as dt

def app():
    startt = dt.datetime.now() - dt.timedelta(days=1)
    endd = dt.datetime.now()
    
    # st.markdown("<hr/>", unsafe_allow_html=True)
    # st.title("Cryptocurrency Daily Prices")
    st.write("<h style='font-family:Montserrat; font-weight: bold; font-size:38px;'>CRYPTOCURRENCY DAILY PRICES</h>", unsafe_allow_html=True)
    st.markdown("<hr/>", unsafe_allow_html=True)

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
    imageBTC = Image.open(urlopen("https://s2.coinmarketcap.com/static/img/coins/64x64/1.png"))
    st.image(imageBTC)

    #Display Dataframe
    st.table(BTC)

    #Display a chart
    st.bar_chart(BTHHis.Close)
    st.markdown("<hr/>", unsafe_allow_html=True)




    #ETH
    st.subheader("ETHERUM ($)")
    imageETH = Image.open(urlopen("https://s2.coinmarketcap.com/static/img/coins/64x64/1027.png"))
    st.image(imageETH)

    #Display Dataframe
    st.table(ETH)

    #Display a chart
    st.bar_chart(ETHHis.Close)
    st.markdown("<hr/>", unsafe_allow_html=True)




    #XRP
    st.subheader("RIPPLE ($)")
    imageXRP = Image.open(urlopen("https://s2.coinmarketcap.com/static/img/coins/64x64/52.png"))
    st.image(imageXRP)

    #Display Dataframe
    st.table(XRP)

    #Display a chart
    st.bar_chart(XRPHis.Close)
    st.markdown("<hr/>", unsafe_allow_html=True)




    #BITCOIN CASH
    st.subheader("BITCOIN CASH ($)")
    imageBCH = Image.open(urlopen("https://s2.coinmarketcap.com/static/img/coins/64x64/1831.png"))
    st.image(imageBCH)

    #Display Dataframe
    st.table(BCH)

    #Display a chart
    st.bar_chart(BCHHis.Close)
    st.markdown("<hr/>", unsafe_allow_html=True)

    


    #ADA BOY 
    st.subheader("ADA BOY ($)")
    imageadab = Image.open(urlopen("https://s2.coinmarketcap.com/static/img/coins/64x64/12796.png"))
    st.image(imageadab)

    #Display Dataframe
    st.table(ADAB)

    #Display a chart
    st.bar_chart(ADABHis.Close)
    st.markdown("<hr/>", unsafe_allow_html=True)





    #Dogecoin
    st.subheader("Dogecoin ($)")
    imageDOGE = Image.open(urlopen("https://s2.coinmarketcap.com/static/img/coins/64x64/74.png"))
    st.image(imageDOGE)

    #Display Dataframe
    st.table(DOGE)

    #Display a chart
    st.bar_chart(DOGEHis.Close)
    st.markdown("<hr/>", unsafe_allow_html=True)





    #SHIBA INU
    st.subheader("SHIBA INU ($)")
    imageSHIBB = Image.open(urlopen("https://s2.coinmarketcap.com/static/img/coins/64x64/5994.png"))
    st.image(imageSHIBB)

    #Display Dataframe
    st.table(SHIBB)

    #Display a chart
    st.bar_chart(SHIBBHis.Close)
    st.markdown("<hr/>", unsafe_allow_html=True)





    #Dotcoin  
    st.subheader("Dotcoin ($)")
    imageDOTB = Image.open(urlopen("https://s2.coinmarketcap.com/static/img/coins/64x64/6636.png"))
    st.image(imageDOTB)

    #Display Dataframe
    st.table(DOTB)

    #Display a chart
    st.bar_chart(DOTBHis.Close)
    st.markdown("<hr/>", unsafe_allow_html=True)





    #Polygon 
    st.subheader("Polygon ($)")
    imageMATICB = Image.open(urlopen("https://s2.coinmarketcap.com/static/img/coins/64x64/2010.png"))
    st.image(imageMATICB)

    #Display Dataframe
    st.table(MATICB)

    #Display a chart
    st.bar_chart(MATICBHis.Close)
    


