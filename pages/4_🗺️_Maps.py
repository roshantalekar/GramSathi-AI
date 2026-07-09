import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

st.set_page_config(page_title="Map Explorer", layout="wide")

st.title("🗺️ GramSathi GIS Explorer")
st.caption("Interactive Rural Infrastructure Mapping")

# ----------------------------
# Sample Data
# ----------------------------

villages = pd.DataFrame({

    "Village":[
        "Sadashivgad",
        "Karve",
        "Mhalunge",
        "Devgad",
        "Shirgaon",
        "Kalmath"
    ],

    "Latitude":[
        16.548,
        16.532,
        16.556,
        16.521,
        16.540,
        16.563
    ],

    "Longitude":[
        73.448,
        73.461,
        73.476,
        73.491,
        73.440,
        73.458
    ],

    "IRI":[92,74,81,56,48,63],

    "Budget":[
        "₹4.5 L",
        "₹7.2 L",
        "₹5.8 L",
        "₹9.4 L",
        "₹11.2 L",
        "₹6.5 L"
    ],

    "Hospital":[
        "Yes",
        "No",
        "Yes",
        "Yes",
        "No",
        "No"
    ],

    "School":[
        "Yes",
        "Yes",
        "Yes",
        "Yes",
        "Yes",
        "Yes"
    ]
})

# ----------------------------
# Sidebar Filters
# ----------------------------

st.sidebar.header("Filters")

selected = st.sidebar.selectbox(
    "Select Village",
    ["All"] + villages["Village"].tolist()
)

# ----------------------------
# Map
# ----------------------------

m = folium.Map(
    location=[16.545,73.460],
    zoom_start=12,
    tiles="CartoDB positron"
)

for _,row in villages.iterrows():

    if selected!="All" and row["Village"]!=selected:
        continue

    if row["IRI"]>=80:
        color="green"
        status="Excellent"

    elif row["IRI"]>=60:
        color="orange"
        status="Moderate"

    else:
        color="red"
        status="Critical"

    popup=f"""
    <h4>{row['Village']}</h4>

    <b>IRI:</b> {row['IRI']}<br>

    <b>Status:</b> {status}<br>

    <b>Budget:</b> {row['Budget']}<br>

    <b>School:</b> {row['School']}<br>

    <b>Hospital:</b> {row['Hospital']}<br><br>

    <b>🤖 AI Recommendation</b><br>

    Repair damaged roads.<br>

    Improve drainage.<br>

    Increase public transport.
    """

    folium.Marker(

        location=[
            row["Latitude"],
            row["Longitude"]
        ],

        popup=popup,

        tooltip=row["Village"],

        icon=folium.Icon(
            color=color,
            icon="info-sign"
        )

    ).add_to(m)

st_folium(
    m,
    width="stretch",
    height=650
)

st.divider()

c1,c2,c3=st.columns(3)

with c1:
    st.success("🟢 Excellent Villages")

    st.write(
        villages[villages["IRI"]>=80]["Village"]
    )

with c2:
    st.warning("🟠 Moderate Villages")

    st.write(
        villages[
            (villages["IRI"]>=60) &
            (villages["IRI"]<80)
        ]["Village"]
    )

with c3:
    st.error("🔴 Critical Villages")

    st.write(
        villages[villages["IRI"]<60]["Village"]
    )