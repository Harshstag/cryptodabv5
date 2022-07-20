import streamlit as st  # pip install streamlit
import webbrowser

def app():
    st.write("<h style='font-family:Montserrat; font-weight: bold; font-size:38px;'>:mailbox:GET IN TOUCH WITH ME!</h>", unsafe_allow_html=True)
    st.markdown("<hr/>", unsafe_allow_html=True)



    contact_form = """
    <form action="https://formsubmit.co/hrsharshsignh@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here"></textarea>
        <button type="submit">Send</button>
    </form>
    """

    st.markdown(contact_form, unsafe_allow_html=True)

    #   *******************************************************************************************************************************************************




    url = 'https://form.jotform.com/221963166587467'
    st.markdown("<hr/>", unsafe_allow_html=True)

    # st.write("<h style=' color: #0078ff; font-size:50px;'>Send Feedback</h>", unsafe_allow_html=True)    
    st.write("<h style='font-family:Montserrat; font-weight: bold; font-size:40px;'>SEND FEEDBACK</h>", unsafe_allow_html=True)
    st.markdown("<hr/>", unsafe_allow_html=True)


    st.write("<h style='  font-size:30px;'>Your feedback is highly appreciated and will help us to improve our ability to serve you and other users of our web sites. For your convenience, we provide you the following options:</h>", unsafe_allow_html=True)

    link = '[CLICK HERE TO GIVE FEEDBACK ](https://form.jotform.com/221963166587467)'
    st.markdown(link, unsafe_allow_html=True)

    # Use Local CSS File
    def local_css(file_name):
        with open(file_name) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    local_css("style/style.css")











