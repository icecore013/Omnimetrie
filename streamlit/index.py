import streamlit as st

import os  # +Deployment
import inspect  # +Deployment
import results
import streamlit.components.v1 as components

currentdir = os.path.dirname(os.path.abspath(
    inspect.getfile(inspect.currentframe())))

logo = os.path.join(currentdir, 'ressources/logo_fire.png')
PAGE_CONFIG = {"page_title": "Omnimetrie", "page_icon": logo, "layout": "wide"}
st.set_page_config(**PAGE_CONFIG)

MENU_ = {
    "Résultats": results,
}

st.sidebar.title('Menu')
selection_page = st.sidebar.radio("", list(MENU_.keys()))


page = MENU_[selection_page]
page.app()
