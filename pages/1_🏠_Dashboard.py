import streamlit as st

st.title("📊 Dashboard")

st.write("## Project Overview")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Villages", "8")

with col2:
    st.metric("Road Segments", "3985")

with col3:
    st.metric("Schools", "5")

with col4:
    st.metric("Hospitals", "2")

st.markdown("---")

st.subheader("Project Summary")

st.info("""
GramSathi AI analyzes rural infrastructure using:

- 🛣️ Road Networks
- 🏫 Schools
- 🏥 Hospitals
- 💧 Water Facilities
- 🚏 Bus Stops
- 🏠 Buildings

using GIS and Machine Learning.
""")