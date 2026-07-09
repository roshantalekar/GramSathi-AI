import streamlit as st
import pandas as pd
import random

st.set_page_config(
    page_title="AI Prediction",
    layout="wide"
)

# --------------------------
# Sample Data
# --------------------------

villages = {

"Sadashivgad":92,

"Karve":74,

"Mhalunge":83,

"Devgad":58,

"Shirgaon":46,

"Kalmath":66

}

# --------------------------
# Header
# --------------------------

st.markdown("""
# 🤖 GramSathi AI Prediction Center

AI Powered Rural Infrastructure Assessment
""")

st.divider()

# --------------------------
# Village Selection
# --------------------------

village = st.selectbox(
    "🏘 Select Village",
    list(villages.keys())
)

st.write("")

if st.button("🚀 Predict Infrastructure"):

    score = villages[village]

    budget = round((100-score)*0.35+2,2)

    confidence = random.randint(94,99)

    months = random.randint(3,8)

    if score>=80:

        priority="🟢 LOW"

        rec=[
            "Maintain existing roads",
            "Improve bus connectivity",
            "Smart lighting installation"
        ]

    elif score>=60:

        priority="🟠 MEDIUM"

        rec=[
            "Repair damaged roads",
            "Improve drainage",
            "Construct sidewalks"
        ]

    else:

        priority="🔴 HIGH"

        rec=[
            "Immediate road reconstruction",
            "Construct Primary Health Centre",
            "Upgrade water facilities"
        ]

    st.divider()

    c1,c2,c3,c4 = st.columns(4)

    c1.metric(
        "Infrastructure Score",
        f"{score}%"
    )

    c2.metric(
        "Priority",
        priority
    )

    c3.metric(
        "Budget",
        f"₹ {budget} Lakh"
    )

    c4.metric(
        "Confidence",
        f"{confidence}%"
    )

    st.write("")

    st.subheader("Development Progress")

    st.progress(score/100)

    st.success(
        f"Estimated Completion Time : {months} Months"
    )

    st.divider()

    st.subheader("🤖 AI Recommendations")

    for i in rec:

        st.success("✔ "+i)

    st.divider()

    st.download_button(

        "📄 Download Development Report",

        data=f"""

Village : {village}

Infrastructure Score : {score}

Priority : {priority}

Budget : ₹ {budget} Lakhs

Confidence : {confidence}

Estimated Time : {months} Months

Recommendations

{chr(10).join(rec)}

""",

        file_name=f"{village}_AI_Report.txt"

    )