import streamlit as st
import pandas as pd

st.title("📊 Infrastructure Analytics")

# Sample Infrastructure Data
data = pd.DataFrame({
    "Infrastructure": [
        "Roads",
        "Schools",
        "Hospitals",
        "Buildings",
        "Bus Stops",
        "Water Facilities"
    ],
    "Count": [
        3985,
        5,
        2,
        1240,
        18,
        27
    ]
})

st.subheader("Infrastructure Distribution")

st.bar_chart(
    data.set_index("Infrastructure")
)

st.subheader("Infrastructure Data")

st.dataframe(data, use_container_width=True)

st.markdown("---")

st.success("✅ Analytics Loaded Successfully")