import streamlit as st
import plotly.express as px
import pandas as pd

st.set_page_config(layout="wide")

# ---------- CSS ----------

st.markdown("""
<style>

.stApp{
    background:#F4F7FC;
}

/* hide menu */

#MainMenu{visibility:hidden;}
footer{visibility:hidden;}
header{visibility:hidden;}

/* title */

.title{
font-size:52px;
font-weight:700;
color:#1E293B;
}

/* cards */

.card{
background:white;
padding:22px;
border-radius:18px;
box-shadow:0 10px 25px rgba(0,0,0,.08);
transition:.35s;
}

.card:hover{
transform:translateY(-8px);
box-shadow:0 20px 40px rgba(0,0,0,.15);
}

/* status */

.good{
background:#DCFCE7;
padding:12px;
border-radius:12px;
font-size:18px;
color:#166534;
font-weight:600;
}

.warning{
background:#FEF3C7;
padding:12px;
border-radius:12px;
font-size:18px;
color:#92400E;
font-weight:600;
}

.danger{
background:#FEE2E2;
padding:12px;
border-radius:12px;
font-size:18px;
color:#991B1B;
font-weight:600;
}

</style>
""", unsafe_allow_html=True)

# ---------------------------

villages={

"Sadashivgad":{

"iri":92,

"budget":"₹5 Lakhs",

"roads":95,

"schools":2,

"hospitals":1,

"water":90,

"status":"Developed"

},

"Khanapur":{

"iri":71,

"budget":"₹18 Lakhs",

"roads":70,

"schools":1,

"hospitals":0,

"water":68,

"status":"Needs Improvement"

},

"Nandgad":{

"iri":48,

"budget":"₹36 Lakhs",

"roads":45,

"schools":1,

"hospitals":0,

"water":40,

"status":"Critical"

},

"Halshi":{

"iri":80,

"budget":"₹12 Lakhs",

"roads":84,

"schools":2,

"hospitals":1,

"water":82,

"status":"Good"

}

}

# ---------------------------------

st.markdown("<div class='title'>📍 Village Explorer</div>",unsafe_allow_html=True)

st.write("")

village=st.selectbox(

"Select Village",

list(villages.keys())

)

data=villages[village]

# -----------------------

c1,c2,c3,c4=st.columns(4)

with c1:

    st.metric("Infrastructure Index",f"{data['iri']}/100")

with c2:

    st.metric("Estimated Budget",data["budget"])

with c3:

    st.metric("Schools",data["schools"])

with c4:

    st.metric("Hospitals",data["hospitals"])

st.write("")

st.progress(data["iri"]/100)

# -----------------------

if data["status"]=="Developed":

    st.markdown("<div class='good'>🟢 Developed Village</div>",unsafe_allow_html=True)

elif data["status"]=="Good":

    st.markdown("<div class='good'>🟢 Good Infrastructure</div>",unsafe_allow_html=True)

elif data["status"]=="Needs Improvement":

    st.markdown("<div class='warning'>🟡 Needs Improvement</div>",unsafe_allow_html=True)

else:

    st.markdown("<div class='danger'>🔴 Critical Infrastructure</div>",unsafe_allow_html=True)

st.write("")

# -----------------------

left,right=st.columns([2,1])

with left:

    st.subheader("Infrastructure Breakdown")

    df=pd.DataFrame({

        "Category":["Roads","Water","Schools","Hospitals"],

        "Score":[

            data["roads"],

            data["water"],

            data["schools"]*40,

            data["hospitals"]*50

        ]

    })

    fig=px.bar(

        df,

        x="Category",

        y="Score",

        color="Score",

        text="Score",

        color_continuous_scale="Blues"

    )

    fig.update_layout(

        height=420,

        paper_bgcolor="white",

        plot_bgcolor="white"

    )

    st.plotly_chart(fig,use_container_width=True)

with right:

    st.subheader("Village Details")

    st.info(f"""

📍 **Village**

{village}

---

🛣 Roads Score

{data['roads']}

---

💧 Water Score

{data['water']}

---

🏫 Schools

{data['schools']}

---

🏥 Hospitals

{data['hospitals']}

---

💰 Budget

{data['budget']}

""")

st.write("")

st.subheader("Recommended Development")

recommendations=[]

if data["roads"]<60:

    recommendations.append("🚧 Repair village roads")

if data["schools"]<2:

    recommendations.append("🏫 Build Primary School")

if data["hospitals"]==0:

    recommendations.append("🏥 Construct Health Centre")

if data["water"]<60:

    recommendations.append("💧 Improve Water Supply")

if len(recommendations)==0:

    recommendations.append("✅ Village is well developed")

for r in recommendations:

    st.success(r)