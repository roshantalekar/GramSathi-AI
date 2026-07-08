import streamlit as st


def load_css():

    st.markdown("""

<style>

html{
scroll-behavior:smooth;
}

.stApp{
background:#F4F7FC;
}

/* Hide Streamlit */

#MainMenu{visibility:hidden;}
footer{visibility:hidden;}
header{visibility:hidden;}

/* Sidebar */

section[data-testid="stSidebar"]{
background:#0F172A;
}

section[data-testid="stSidebar"] *{
color:white;
}


/* Hero */

.hero{

background:linear-gradient(135deg,#0F172A,#1E3A8A);

padding:45px;

border-radius:25px;

color:white;

box-shadow:0px 15px 45px rgba(0,0,0,.25);

animation:fade 1s ease;

}

.hero h1{

font-size:48px;

margin-bottom:10px;

}

.hero p{

font-size:20px;

opacity:.9;

}


/* Dashboard Cards */

.card{

background:white;

border-radius:22px;

padding:28px;

text-align:center;

box-shadow:0px 10px 25px rgba(0,0,0,.08);

transition:.35s;

cursor:pointer;

margin-bottom:20px;

}

.card:hover{

transform:translateY(-12px) scale(1.03);

box-shadow:0px 25px 45px rgba(0,0,0,.18);

}

.icon{

font-size:42px;

margin-bottom:10px;

}

.title{

font-size:16px;

color:#64748B;

}

.number{

font-size:40px;

font-weight:bold;

margin-top:5px;

color:#111827;

}


/* Glass Panel */

.glass{

background:rgba(255,255,255,.55);

backdrop-filter:blur(18px);

padding:25px;

border-radius:20px;

box-shadow:0px 10px 30px rgba(0,0,0,.08);

}


/* Buttons */

.stButton>button{

border:none;

background:#2563EB;

color:white;

padding:12px 25px;

border-radius:12px;

transition:.3s;

}

.stButton>button:hover{

background:#1D4ED8;

transform:scale(1.05);

}


/* Fade Animation */

@keyframes fade{

from{

opacity:0;

transform:translateY(30px);

}

to{

opacity:1;

transform:translateY(0px);

}

}

</style>

""",unsafe_allow_html=True)


def hero():

    st.markdown("""

<div class="hero">

<h1>🌍 GramSathi AI</h1>

<p>
AI Powered Rural Infrastructure Planning Platform
</p>

</div>

""",unsafe_allow_html=True)



def metric_card(icon,title,value):

    st.markdown(f"""

<div class="card">

<div class="icon">{icon}</div>

<div class="title">{title}</div>

<div class="number">{value}</div>

</div>

""",unsafe_allow_html=True)