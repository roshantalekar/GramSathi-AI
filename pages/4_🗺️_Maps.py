import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

st.title("🗺️ Village GIS Map")

# Sample village locations
villages = pd.DataFrame({
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
    "Latitude": [
        14.843,
        14.831,
        14.810,
        14.900,
        14.780,
        14.760,
        14.620,
        14.720
    ],
    "Longitude": [
        74.126,
        74.140,
        74.180,
        74.200,
        74.250,
        74.300,
        74.280,
        74.350
    ]
})

# Create map
m = folium.Map(
    location=[14.80, 74.22],
    zoom_start=10
)

# Add markers
for _, row in villages.iterrows():
    folium.Marker(
        location=[row["Latitude"], row["Longitude"]],
        popup=row["Village"],
        tooltip=row["Village"],
        icon=folium.Icon(color="blue", icon="info-sign")
    ).add_to(m)

# Display map
st_folium(m, width=1000, height=600)