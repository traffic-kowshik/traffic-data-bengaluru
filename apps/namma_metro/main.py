import streamlit as st
import json
import pandas as pd
from pathlib import Path

from traffic_data_bengaluru.utils import *

data_directory = get_data_directory()
ridership_filepath = data_directory / "namma_metro" / "raw" / "ridership.jsonl"

st.title("🚇 Namma Metro")
st.set_page_config(page_title="Namma Metro Ridership", layout="wide")

records = []
with open(ridership_filepath, "r") as f:
    for line in f:
        item = json.loads(line)
        results = item.get("results", [])
        if results:
            records.append(results[0])

if not records:
    st.warning("No ridership data found.")
else:
    df = pd.DataFrame(records).sort_values(by='RidershipDate', ascending=False)
    st.dataframe(df)