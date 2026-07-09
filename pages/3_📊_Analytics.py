import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(page_title="Analytics", layout="wide")

# -----------------------------
# Sample Data
# -----------------------------
df = pd.DataFrame({
    "Village": ["Sadashivgad","Mhalunge","Karve","Devgad","Kalmath","Shirgaon"],
    "IRI":[92,81,74,63,56,48],
    "Budget":[5,8,12,9,6,11],
    "Schools":[2,1,3,1,2,1],
    "Hospitals":[1,1,0,1,0,0]
})

# -----------------------------
# Title
# -----------------------------
st.title("📊 Analytics Dashboard")
st.caption("Infrastructure insights across villages")

# -----------------------------
# KPI Cards
# -----------------------------
c1,c2,c3,c4=st.columns(4)

c1.metric("🏘 Villages",len(df))
c2.metric("📈 Avg IRI",round(df["IRI"].mean(),1))
c3.metric("💰 Total Budget",f"₹{df['Budget'].sum()} L")
c4.metric("🚨 Critical",len(df[df["IRI"]<60]))

st.divider()

# -----------------------------
# Charts Row 1
# -----------------------------
left,right=st.columns([2,1])

with left:

    fig=px.bar(
        df,
        x="Village",
        y="IRI",
        color="IRI",
        title="Road Infrastructure Readiness Index",
        color_continuous_scale="Blues"
    )

    st.plotly_chart(fig,width="stretch")

with right:

    pie=px.pie(
        values=[
            df["Schools"].sum(),
            df["Hospitals"].sum(),
            df["Budget"].sum()
        ],
        names=[
            "Schools",
            "Hospitals",
            "Budget"
        ],
        title="Infrastructure Distribution"
    )

    st.plotly_chart(pie,width="stretch")

st.divider()

# -----------------------------
# Charts Row 2
# -----------------------------
col1,col2=st.columns(2)

with col1:

    line=px.line(
        df,
        x="Village",
        y="IRI",
        markers=True,
        title="Village Infrastructure Trend"
    )

    st.plotly_chart(line,width="stretch")

with col2:

    grouped=go.Figure()

    grouped.add_trace(
        go.Bar(
            x=df["Village"],
            y=df["Schools"],
            name="Schools"
        )
    )

    grouped.add_trace(
        go.Bar(
            x=df["Village"],
            y=df["Hospitals"],
            name="Hospitals"
        )
    )

    grouped.update_layout(
        title="Schools vs Hospitals",
        barmode="group"
    )

    st.plotly_chart(grouped,width="stretch")

st.divider()

# -----------------------------
# Ranking Table
# -----------------------------
st.subheader("🏆 Village Ranking")

ranking=df.sort_values(
    "IRI",
    ascending=False
)

st.dataframe(
    ranking,
    width="stretch"
)

csv=ranking.to_csv(index=False).encode()

st.download_button(
    "📥 Download Report",
    csv,
    "analytics.csv",
    "text/csv"
)