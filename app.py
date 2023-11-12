import streamlit as st
from data import data

new_data = data()
for image in new_data:
    st.image(image)
