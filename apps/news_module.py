import streamlit as st
from .fetch_news import *

api_key='ed0b00cc442c4ad183e455e7df4a477c'

def app():
	# st.write("<h style=' color: #0078ff; font-size:50px;'>NEWS & More</h>", unsafe_allow_html=True)
	st.write("<h style='font-family:Montserrat; color: #FF0000; font-weight: bold; font-size:40px;'>:newspaper:NEWS & MORE</h>", unsafe_allow_html=True)
	st.markdown("<hr/>", unsafe_allow_html=True)

	# st.write("Select category")
	st.write("<h style='font-family:Montserrat; font-weight: bold; font-size:20px;'>SELECT CATEGORY</h>", unsafe_allow_html=True)
	selected_option = st.selectbox(" ",('business','health','technolgy'))
	
	if selected_option == 'health':
		retrieve_category_news("https://newsapi.org/v2/everything?q=health&language=en&apiKey="+api_key)
	elif selected_option == 'technolgy':
		retrieve_category_news("https://newsapi.org/v2/everything?q=stocks OR shares AND technolgy&language=en&apiKey="+api_key)
	else:
		retrieve_category_news("https://newsapi.org/v2/everything?q=stocks OR shares&language=en&apiKey="+api_key)
