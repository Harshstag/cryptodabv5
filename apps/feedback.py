import streamlit as st
import webbrowser
def app():

    url = 'https://form.jotform.com/221963166587467'

    # st.write("<h style=' color: #0078ff; font-size:50px;'>Send Feedback</h>", unsafe_allow_html=True)    
    st.write("<h style='font-family:Montserrat; font-weight: bold; font-size:50px;'>SEND FEEDBACK</h>", unsafe_allow_html=True)
    st.markdown("<hr/>", unsafe_allow_html=True)


    st.write("<h style='  font-size:30px;'>Your feedback is highly appreciated and will help us to improve our ability to serve you and other users of our web sites. For your convenience, we provide you the following options:</h>", unsafe_allow_html=True)

    if st.button('Click Here to send Feedback'):
        webbrowser.open_new_tab(url)   

  