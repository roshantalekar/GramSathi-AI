import streamlit as st
import plotly.express as px
import pandas as pd

from components.ui import *

st.set_page_config(layout="wide")

load_css()

hero()

st.write("")

c1,c2,c3,c4=st.columns(4)

with c1:
    metric_card("🏘","Villages","8")

with c2:
    metric_card("🛣","Roads","3985")

with c3:
    metric_card("🏫","Schools","5")

with c4:
    metric_card("🏥","Hospitals","2")

st.write("")
st.write("")

left,right=st.columns([2,1])

with left:

    st.markdown("### 📈 Road Quality")

    df=pd.DataFrame({

        "Village":[
            "A",
            "B",
            "C",
            "D",
            "E",
            "F"
        ],

        "IRI":[45,62,58,80,41,72]

    })

    fig=px.bar(

        df,

        x="Village",

        y="IRI",

        color="IRI",

        text="IRI",

        height=400

    )

    fig.update_layout(

        template="plotly_white",

        margin=dict(l=20,r=20,t=30,b=20)

    )

    st.plotly_chart(fig,use_container_width=True)


with right:

    st.markdown("### 🚨 Critical Villages")

    st.info("""

🔴 Village C

Very Poor Roads


🟠 Village D

No Primary School


🟡 Village A

Water Facility Needed


🟢 Village B

Healthy Infrastructure

""")

st.write("")

st.markdown("### 🗺 Infrastructure Distribution")

dff=pd.DataFrame({

"Type":[

"Roads",

"Schools",

"Hospitals",

"Bus Stops",

"Buildings"

],

"Count":[3985,5,2,28,870]

})

fig2=px.pie(

dff,

values="Count",

names="Type",

hole=.65

)

fig2.update_layout(

height=450,

margin=dict(l=20,r=20,t=20,b=20)

)

st.plotly_chart(fig2,use_container_width=True)