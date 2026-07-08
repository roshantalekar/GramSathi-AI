import streamlit as st

st.title("🤖 AI Prediction Engine")

st.info("Machine Learning model integration is in progress.")

st.write("This page will soon use the trained Random Forest model.")

road_length = st.slider("Road Length", 0, 50, 10)
schools = st.slider("Schools", 0, 10, 2)
hospitals = st.slider("Hospitals", 0, 5, 1)

if st.button("Predict"):

    st.success("Prediction module will be connected to the trained model.")