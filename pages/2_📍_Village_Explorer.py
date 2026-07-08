import streamlit as st
import pandas as pd

st.title("📍 Village Explorer")

# Sample data (we'll replace this with real data later)
village_df = pd.DataFrame({
    "Village": [
        "Sadashivgad",
        "Majali",
        "Asnoti",
        "Mudgeri",
        "Kanasgiri",
        "Hotegali",
        "Hankon",
        "Joog"
    ],
    "IRI": [92, 76, 38, 61, 42, 35, 81, 28],
    "Priority": [
        "Developed",
        "Needs Improvement",
        "Critical",
        "Needs Improvement",
        "Critical",
        "Critical",
        "Developed",
        "Critical"
    ],
    "Budget": [5, 25, 50, 25, 50, 50, 5, 50]
})

selected = st.selectbox(
    "Select Village",
    village_df["Village"]
)

row = village_df[village_df["Village"] == selected].iloc[0]

st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    st.metric("Infrastructure Readiness Index", f"{row['IRI']}/100")

with col2:
    st.metric("Estimated Budget", f"₹{row['Budget']} Lakhs")

st.progress(int(row["IRI"]) / 100)

if row["Priority"] == "Critical":
    st.error("🔴 Critical")

elif row["Priority"] == "Needs Improvement":
    st.warning("🟡 Needs Improvement")

else:
    st.success("🟢 Developed")