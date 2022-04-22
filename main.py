import streamlit as st
from utils.classes import *
from utils.const import *
from utils.functions import *

st.set_page_config(layout="wide", page_title="My app", menu_items={
    'About': "My app made with love"
})

st.title("Hello World")