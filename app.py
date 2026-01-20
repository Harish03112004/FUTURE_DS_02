import streamlit as st
import numpy as np
from joblib import load

# ================= PAGE CONFIG =================
st.set_page_config(
    page_title="Telecom Churn Prediction Dashboard",
    layout="wide"
)

# ================= LOAD CSS =================
with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# ================= LOAD MODEL =================
model = load("model/churn_model.pkl")

# ================= HEADER =================
st.markdown(
    "<div class='title'> Telecom Churn Prediction Dashboard</div>",
    unsafe_allow_html=True
)

st.divider()

# ================= INPUT SECTION =================
left, right = st.columns(2)

# ---------- LEFT COLUMN ----------
with left:
    gender = st.selectbox(
        "Gender (0 = Female, 1 = Male)",
        [0, 1]
    )

    days_subscribed = st.number_input(
        "No. of Days Subscribed",
        min_value=0,
        value=2
    )

    mail_subscribed = st.selectbox(
        "Mail Subscribed",
        ["Yes", "No"]
    )

    weekly_max_night_minutes = st.number_input(
        "Weekly Max Night Minutes",
        min_value=0,
        value=4
    )

    max_days_inactive = st.number_input(
        "Maximum Days Inactive",
        min_value=0,
        value=0
    )

# ---------- RIGHT COLUMN ----------
with right:
    age = st.number_input(
        "Age",
        min_value=10,
        max_value=100,
        value=34
    )

    multi_screen = st.selectbox(
        "Multi Screen",
        ["Yes", "No"]
    )

    weekly_minutes = st.number_input(
        "Weekly Minutes Watched",
        min_value=0,
        value=200
    )

    videos_watched = st.number_input(
        "Videos Watched",
        min_value=0,
        value=14
    )

    support_calls = st.number_input(
        "Customer Support Calls",
        min_value=0,
        value=2
    )

st.divider()

# ================= PREDICTION =================
if st.button("Predict Churn"):
    input_data = np.array([[
        gender,
        0,
        days_subscribed,
        weekly_minutes,
        weekly_minutes * 4
    ]])

    prediction = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)[0][1]

    if prediction == 1:
        st.error(
            f"❌ Customer likely to CHURN\n , Risk Probability: {probability:.2%}"
        )
    else:
        st.success(
            f"✅ Customer likely to STAY\n , Risk Probability: {probability:.2%}"
        )
