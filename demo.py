import streamlit as st
from streamlit_js_eval import streamlit_js_eval, copy_to_clipboard, create_share_link, get_geolocation
import json

st.title('Mini App')
st.header('_Streamlit_ is :blue[cool] :sunglasses:', divider='rainbow')

with st.sidebar:
    with st.echo():
        st.write("This code will be printed to the sidebar.")

    with st.spinner("Loading..."):
        time.sleep(5)
    st.success("Done!")

variable_output = st.text_input("Enter some text", value="Streamlit is awesome")
font_size = st.slider("Enter a font size", 1, 300, value=30)

html_str = f"""
<style>
p.a {{
  font: bold {font_size}px Courier;
}}
</style>
<p class="a">{variable_output}</p>
"""

st.markdown(html_str, unsafe_allow_html=True)

age = st.slider('How old are you?', 0, 130, 25)
st.write("I'm ", age, 'years old')

picture = st.camera_input("Take a picture")

if picture:
    st.image(picture)

if st.checkbox("Check my location"):
    loc = get_geolocation()
    st.write(f"Your coordinates are {loc}")
