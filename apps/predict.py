# from turtle import title
import streamlit as st
from datetime import date
import requests

import yfinance as yf
from fbprophet import Prophet
from fbprophet.plot import plot_plotly
from plotly import graph_objs as go
# from .fetch_news import retrieve_news



def app():

	START = "2015-01-01"
	TODAY = date.today().strftime("%Y-%m-%d")
    # st.headre('CryptoCurrency Price Prediction')
    
	st.write("<h style='font-family:Montserrat;  font-weight: bold; font-size:38px;'>CRYPTO CURRENCY  PRICE PREDICTION</h>", unsafe_allow_html=True)
    

	selected_stock = st.text_input("Enter ticker", "BTC-USD")

	n_years = st.slider("Years of prediction:", 1, 4)
	period = n_years * 365

	@st.cache
	def load_data(ticker):
		data = yf.download(ticker, START, TODAY)
		data.reset_index(inplace = True)
		return data

	data = load_data(selected_stock)
	if data.empty:
		st.error("not a valid ticker")
		raise Exception("not a valid ticker")

	stock = yf.Ticker(selected_stock)

	
	stock = yf.Ticker(selected_stock)
	data_load_state = st.info("Load data...")
	data = load_data(selected_stock)
	data_load_state.success("Loading data...done!")
	longname = stock.info['name']
	stock_name = selected_stock
	exchange = stock.info['exchange']
	timezone = stock.info['exchangeTimezoneName']

	
	st.markdown("<hr/>", unsafe_allow_html=True)

	

	# st.markdown("&nbsp")
	st.markdown(f"<h style='font-family:Montserrat;  font-weight: bold; font-size:30px; '>**SELECTED : {longname}**</h>", unsafe_allow_html=True)
	st.markdown(f"<h style='text-align: center; font-size:15px; color: #0078ff; '>**EXCHANGE : {exchange}: {stock_name}  |  {timezone}**</h>", unsafe_allow_html=True)
    	

	#Forecasting
	df_train = data[['Date', 'Close']]
	df_train = df_train.rename(columns={"Date": "ds", "Close": "y"})

	m = Prophet()
	m.fit(df_train)
	future = m.make_future_dataframe(periods=period)
	forecast = m.predict(future)

	st.markdown("<hr/>", unsafe_allow_html=True)
	st.markdown("&nbsp ")
	st.write("<h style='font-family:Montserrat; font-weight: bold; font-size:30px;'>FORCAST DATA</h>", unsafe_allow_html=True)
	fig1 = plot_plotly(m, forecast)
	st.plotly_chart(fig1)

	st.markdown("<hr/>", unsafe_allow_html=True)
	st.markdown("&nbsp ")
	st.write("<h style='font-family:Montserrat; font-weight: bold; font-size:30px;'>RAW DATA</h>", unsafe_allow_html=True)
	st.write(data.tail())

	st.markdown("<hr/>", unsafe_allow_html=True)
	st.markdown("&nbsp ")
	st.write("<h style='font-family:Montserrat; font-weight: bold; font-size:30px;'>RAW FORCAST DATA</h>", unsafe_allow_html=True)
	st.write(forecast.tail())

	st.markdown("<hr/>", unsafe_allow_html=True)
	st.markdown("&nbsp ")
	st.write("<h style='font-family:Montserrat; font-weight: bold; font-size:30px;'>FORCAST COMPONENT</h>", unsafe_allow_html=True)
	fig2 = m.plot_components(forecast)
	st.write(fig2)	
	st.markdown("<hr/>", unsafe_allow_html=True)

   