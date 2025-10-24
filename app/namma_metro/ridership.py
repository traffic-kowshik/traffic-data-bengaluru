import os

import requests
import streamlit as st
import pandas as pd
import altair as alt

from dotenv import load_dotenv
load_dotenv()

st.title("🎟️ Ridership")
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


# Daily ridership chart
chart = (
    alt.Chart(st.session_state.df)
    .mark_line(point=alt.OverlayMarkDef(size=80))
    .encode(
        x=alt.X(
            'ridership_date:T',
            title='',
            axis=alt.Axis(
                format='%Y-%m-%d (%a)'
            )
        ),
        y=alt.Y(
            'total_passengers:Q',
            title='Total Passengers'
        ),
        tooltip=[
            alt.Tooltip('ridership_date:T', title='Date', format='%Y-%m-%d (%a)'),
            alt.Tooltip('total_passengers:Q', title='Total Passengers', format=',')
        ]
    )
)

st.altair_chart(chart, use_container_width=True)


st.divider(width="stretch")

df = st.session_state.df.copy()
numeric_cols = df.select_dtypes(include="number").columns

show_percent = st.toggle("Show Percentage (%)", value=False)

if show_percent:
    df[numeric_cols] = df[numeric_cols].apply(lambda x: (x / x.max()) * 100)
    df[numeric_cols] = df[numeric_cols].round(1)

def smart_format(x):
    if pd.isna(x):
        return ""
    if x == int(x):
        return f"{int(x):,}"
    return f"{x:.1f}"

styled_df = (
    df.style
    .background_gradient(cmap="RdYlGn", axis=0, subset=numeric_cols)
    .format(smart_format, subset=numeric_cols)
)

st.dataframe(styled_df, width="stretch")


st.divider(width="stretch")


df_long = st.session_state.df.melt(
    id_vars='ridership_date',
    value_vars=['total_smart_cards', 'tokens', 'total_qr', 'total_ncmc', 'group_ticket'],
    var_name='ticket_type',
    value_name='count'
)

chart = (
    alt.Chart(df_long)
    .mark_area()
    .encode(
        x=alt.X(
            'ridership_date:T',
            title='',
            axis=alt.Axis(
                format='%Y-%m-%d (%a)'
            )
        ),
        y=alt.Y(
            'count:Q',
            title='Count'
        ),
        color=alt.Color(
            'ticket_type:N',
            title='Ticket Type'
        ),
        tooltip=[
            alt.Tooltip('ridership_date:T', title='Date', format='%Y-%m-%d (%a)'),
            alt.Tooltip('ticket_type:N', title='Ticket Type'),
            alt.Tooltip('count:Q', title='Count', format=',')
        ]
    )
)

st.altair_chart(chart, use_container_width=True)
