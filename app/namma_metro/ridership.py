import os
import requests
import streamlit as st
import pandas as pd
from dotenv import load_dotenv
load_dotenv()

st.title("🚇 Namma Metro")
st.set_page_config(page_title="Namma Metro Ridership", layout="wide")

base_url = os.environ.get("TDB_API_BASE_URL")
url = f"{base_url}/metro/ridership"

# Function to fetch data
def fetch_data():
    response = requests.get(url)
    response.raise_for_status()
    return pd.DataFrame(response.json())

# Initialize session state
if "df" not in st.session_state:
    st.session_state.df = fetch_data()

# Refresh button
if st.button("Refresh"):
    st.session_state.df = fetch_data()

# Apply background gradient to numeric columns
styled_df = st.session_state.df.style.background_gradient(
    cmap="RdYlGn",
    axis=0,
    subset=st.session_state.df.select_dtypes(include='number').columns
)

st.dataframe(styled_df, use_container_width=True)