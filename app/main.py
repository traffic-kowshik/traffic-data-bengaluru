import streamlit as st

pages = {
    "BMTC": [
        st.Page("bmtc/routes.py", title="Routes")
    ],
    "Namma Metro": [
        st.Page("namma_metro/ridership.py", title="Ridership")
    ],
}

pg = st.navigation(pages)
pg.run()