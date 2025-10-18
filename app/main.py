import streamlit as st

pages = {
    "Traffic Data Bengaluru": [
        st.Page('about.py', title="About")
    ],
    "BMTC": [
        st.Page("bmtc/routes.py", title="Routes", url_path="bmtc-routes")
    ],
    "Namma Metro": [
        st.Page("namma_metro/ridership.py", title="Ridership", url_path="namma-metro-ridership")
    ],
}

pg = st.navigation(pages)
pg.run()