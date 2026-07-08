import streamlit as st
from components.ui import *

st.set_page_config(layout="wide")

load_css()

hero()

col1, col2, col3, col4 = st.columns(4)

with col1:
    metric_card("🏘","Villages","8")

with col2:
    metric_card("📈","Average IRI","56.4")

with col3:
    metric_card("💰","Budget","₹2.1 Cr")

with col4:
    metric_card("🚨","Critical","3")