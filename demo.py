import streamlit as st
from streamlit_js_eval import streamlit_js_eval, copy_to_clipboard, create_share_link, get_geolocation
import json

st.title('Mini App')
st.header('_Streamlit_ is :blue[cool] :sunglasses:', divider='rainbow')

age = st.slider('How old are you?', 0, 130, 25)
st.write("I'm ", age, 'years old')

picture = st.camera_input("Take a picture")

if picture:
    st.image(picture)

if st.checkbox("Check my location"):
    loc = get_geolocation()
    st.write(f"Your coordinates are {loc}")
