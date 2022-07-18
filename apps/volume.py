# from turtle import color
import streamlit as st
import yfinance as yf
import mplfinance as mpf
import plotly.graph_objects as go
from datetime import date


def app():
    TODAY = date.today().strftime("%Y-%m-%d")

    # st.title('Crypto Volume Chart ')
    st.write("<h style='font-family:Montserrat; font-weight: bold; font-size:38px;'>CRYPTO VOLUME CHART</h>", unsafe_allow_html=True)
    st.markdown("<hr/>", unsafe_allow_html=True)

    title = st.text_input("Search Crypto","BTC-USD")

    df = yf.download({title},strat='2022-10-05',end=TODAY)

    kpi0, kpi1 = st.columns([1,1])
    with kpi0:
        st.area_chart(data=df, width=0, height=0, use_container_width=True)
    with kpi1:
        st.bar_chart(data=df, width=0, height=0, use_container_width=True)



    # st.title('Some Popular Crypto Volume')
    st.markdown("<hr/>", unsafe_allow_html=True)
    st.write("<h style='font-family:Montserrat; font-weight: bold; font-size:38px;'>SOME POPULAR CRYPTO VOLUMES</h>", unsafe_allow_html=True)
    st.markdown("<hr/>", unsafe_allow_html=True)

    kpi01, kpi02 = st.columns([1,1])
    with kpi01:
        
        st.subheader('XRP-USD')
        df1 = yf.download('XRP-USD',strat='2022-10-05',end=TODAY)
        st.area_chart(data=df1, width=0, height=0, use_container_width=True)
    
    with kpi02:
       
        st.subheader('⠀')
        df1 = yf.download('XRP-USD',strat='2022-10-05',end=TODAY)
        st.bar_chart(data=df1, width=0, height=0, use_container_width=True)
    st.markdown("<hr/>", unsafe_allow_html=True)



    kpi03, kpi04 = st.columns([1,1])
    with kpi03:
        
        st.subheader('ETH-USD')
        df1 = yf.download('ETH-USD',strat='2022-10-05',end=TODAY)
        st.area_chart(data=df1, width=0, height=0, use_container_width=True)
    
    with kpi04:
       
        st.subheader('⠀')
        df1 = yf.download('ETH-USD',strat='2022-10-05',end=TODAY)
        st.bar_chart(data=df1, width=0, height=0, use_container_width=True)
    st.markdown("<hr/>", unsafe_allow_html=True)



    kpi05, kpi06 = st.columns([1,1])
    with kpi05:
        
        st.subheader('DAI-USD')
        df1 = yf.download('DAI-USD',strat='2022-10-05',end=TODAY)
        st.area_chart(data=df1, width=0, height=0, use_container_width=True)
    
    with kpi06:
       
        st.subheader('⠀')
        df1 = yf.download('DAI-USD',strat='2022-10-05',end=TODAY)
        st.bar_chart(data=df1, width=0, height=0, use_container_width=True)
    st.markdown("<hr/>", unsafe_allow_html=True)



    kpi07, kpi08 = st.columns([1,1])
    with kpi07:
        
        st.subheader('DOT-USD')
        df1 = yf.download('DOT-USD',strat='2022-10-05',end=TODAY)
        st.area_chart(data=df1, width=0, height=0, use_container_width=True)
    
    with kpi08:
       
        st.subheader('⠀')
        df1 = yf.download('BOT-USD',strat='2022-10-05',end=TODAY)
        st.bar_chart(data=df1, width=0, height=0, use_container_width=True)
    st.markdown("<hr/>", unsafe_allow_html=True)