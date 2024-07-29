import streamlit as st

from st_pages import get_nav_from_toml, add_page_title

# st.write(get_nav_from_toml(path = ".streamlit/sample_section_page.toml"))
#
# for section,pages in get_nav_from_toml(path = ".streamlit/sample_section_page.toml").items():
#     st.write(section)
#     for page in pages:
#         st.write(section.title(),page.title)
nav = get_nav_from_toml(".streamlit/sample_section_page.toml")
pg = st.navigation(nav)
add_page_title(pg)
try:
    pg.run()
except Exception as e:
    st.info(e)
