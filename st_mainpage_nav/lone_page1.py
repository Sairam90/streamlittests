import streamlit as st

from st_pages import get_nav_from_toml, add_page_title


# nav = get_nav_from_toml(".streamlit/sample_section_page.toml")
lone_page1 = st.Page(page="lone_page1.py",title="lone page1")

nav = {"":[lone_page1]}
pg = st.navigation(nav)
# add_page_title(pg)
try:
    pg.run()
except Exception as e:
    st.info(e)
