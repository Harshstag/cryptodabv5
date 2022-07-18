import streamlit as st  # pip install streamlit

def app():
    # st.header(":mailbox: Get In Touch With Me!")
    st.markdown("<hr/>", unsafe_allow_html=True)

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

    # Use Local CSS File
    def local_css(file_name):
        with open(file_name) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


    local_css("style/style.css")
