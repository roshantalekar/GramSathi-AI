import streamlit as st

# ==========================================
# GLOBAL CSS
# ==========================================

def load_css():
    st.write("UI Loaded")
    st.markdown("""
    <style>

    /* Main Background */

    .stApp{
        background:#F5F7FB;
    }

    /* Hide Streamlit Menu */

    #MainMenu{
        visibility:hidden;
    }

    footer{
        visibility:hidden;
    }

    header{
        visibility:hidden;
    }

    /* Hero */

    .hero{

        background:linear-gradient(135deg,#0F172A,#1E3A8A);

        color:white;

        padding:35px;

        border-radius:20px;

        margin-bottom:25px;

        box-shadow:0px 10px 35px rgba(0,0,0,.20);

    }

    .hero h1{

        font-size:40px;

        margin-bottom:5px;

    }

    .hero p{

        font-size:18px;

        opacity:.9;

    }

    /* Cards */

    .card{

        background:white;

        border-radius:18px;

        padding:25px;

        box-shadow:0px 8px 20px rgba(0,0,0,.08);

        transition:0.35s;

        cursor:pointer;

        text-align:center;

        margin-bottom:15px;

    }

    .card:hover{

        transform:translateY(-10px);

        box-shadow:0px 20px 40px rgba(0,0,0,.20);

    }

    .icon{

        font-size:38px;

    }

    .title{

        color:gray;

        font-size:16px;

    }

    .number{

        font-size:34px;

        font-weight:bold;

        color:#111827;

    }

    .badge{

        display:inline-block;

        background:#DCFCE7;

        color:#166534;

        padding:6px 12px;

        border-radius:50px;

        font-size:14px;

        margin-top:10px;

    }

    </style>
    """, unsafe_allow_html=True)


# ==========================================
# HERO
# ==========================================

def hero():

    st.markdown("""

    <div class='hero'>

    <h1>🌍 GramSathi AI</h1>

    <p>AI Powered Rural Infrastructure Planning Platform</p>

    <span class='badge'>🟢 Live Dashboard</span>

    </div>

    """, unsafe_allow_html=True)


# ==========================================
# CARD
# ==========================================

def metric_card(icon,title,value):

    st.markdown(f"""

    <div class='card'>

    <div class='icon'>{icon}</div>

    <div class='title'>{title}</div>

    <div class='number'>{value}</div>

    </div>

    """, unsafe_allow_html=True)