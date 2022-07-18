import streamlit as st
from multiapp import MultiApp
from apps import home, compare, volume, twitter, news_module, price, contact_form
from PIL import Image

app = MultiApp()

img  = Image.open('img/logo.png')
st.set_page_config(page_title="Cryptodab", page_icon=img, layout='wide',initial_sidebar_state='collapsed')


# selected  = option_menu(
#     menu_title = None,
#     options=["Home","Predict","Compare","Volume","Twitter","News","Price","Contact","Feedback"],
#     icons= ["house","calendar4-week","activity","align-bottom","twitter","newspaper","book","envelope","body-text"],
#     orientation="horizontal",
# )
# if selected == "Predict":
#     app.add_app("Predict",predict.app)
#     app.run()
# if selected == "Compare":
#     app.add_app("Compare",compare.app)
#     app.run()
# if selected == "Volume":
#     app.add_app("Volume",volume.app)
#     app.run()
# if selected == "Twitter":
#     app.add_app("Twitter",twitter.app)
#     app.run()
# if selected == "News":
#     app.add_app("News",news_module.app)
#     app.run()
# if selected == "Price":
#     app.add_app("Price",price.app)
#     app.run()
# if selected == "Contact":
#     app.add_app("Contact",contact_form.app)
#     app.run()
# if selected == "Feedback":
#     app.add_app("Feedback",feedback.app)
#     app.run()



app.add_app('Home',home.app)
# app.add_app("Predict",predict.app)
app.add_app("Compare",compare.app)
app.add_app("Volume",volume.app)
app.add_app("Twitter",twitter.app)
app.add_app("News",news_module.app)
app.add_app("Price",price.app)
app.add_app("Contact",contact_form.app)
# app.add_app("Feedback",feedback.app)


app.run()
