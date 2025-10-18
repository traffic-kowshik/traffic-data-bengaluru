import os
import requests
import streamlit as st
import pandas as pd
from dotenv import load_dotenv
load_dotenv()

st.title("🚌 BMTC")
st.set_page_config(page_title="Bengaluru BMTC Routes", layout="wide")
