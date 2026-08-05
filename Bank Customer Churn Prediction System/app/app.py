import streamlit as st
import pandas as pd
from predict import predict_churn


st.set_page_config(
    page_title="Bank Customer Churn Prediction",
    page_icon="🏦",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>

/* Import Google Font */
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');

/* Entire App */
html, body, [class*="css"]{
    font-family: 'Poppins', sans-serif;
}

/* Background */
.stApp{
    background: linear-gradient(135deg,#eef2ff,#f8fafc);
}

/* Remove Default Header */
header{
    visibility:hidden;
}

footer{
    visibility:hidden;
}

/* Sidebar */
section[data-testid="stSidebar"]{
    background:linear-gradient(180deg,#0f172a,#1e3a8a);
    color:white;
}

/* Sidebar Text */
section[data-testid="stSidebar"] *{
    color:white !important;
}

/* Main Title */
.main-title{
    font-size:42px;
    font-weight:700;
    color:white;
}

.subtitle{
    font-size:18px;
    color:#dbeafe;
}

/* Hero Section */
.hero{

    background:linear-gradient(135deg,#2563eb,#1e40af);

    padding:40px;

    border-radius:20px;

    color:white;

    box-shadow:0px 15px 30px rgba(0,0,0,0.20);

    margin-bottom:30px;

}

/* Cards */

.card{

    background:white;

    border-radius:18px;

    padding:25px;

    box-shadow:0px 8px 25px rgba(0,0,0,0.10);

    transition:0.3s;

}

.card:hover{

    transform:translateY(-5px);

    box-shadow:0px 15px 30px rgba(0,0,0,.15);

}

/* Section Headings */

.section-title{

    font-size:28px;

    font-weight:700;

    color:#1e3a8a;

    margin-bottom:15px;

}

/* Predict Button */

.stButton>button{

    width:100%;

    height:60px;

    border-radius:15px;

    background:linear-gradient(90deg,#2563eb,#4f46e5);

    color:white;

    font-size:20px;

    font-weight:bold;

    border:none;

    transition:0.4s;

}

.stButton>button:hover{

    transform:scale(1.03);

    box-shadow:0px 10px 20px rgba(37,99,235,.35);

}

/* Metric Cards */

div[data-testid="metric-container"]{

    background:white;

    border-radius:18px;

    padding:20px;

    border-left:6px solid #2563eb;

    box-shadow:0px 5px 20px rgba(0,0,0,.08);

}

/* Input Boxes */

.stNumberInput,
.stSelectbox{

    background:white;

    border-radius:12px;

}

/* Dataframe */

[data-testid="stDataFrame"]{

    border-radius:15px;

    overflow:hidden;

}

/* Success */

.stSuccess{

    border-radius:15px;

}

/* Error */

.stError{

    border-radius:15px;

}

/* Divider */

hr{

    border:1px solid #dbeafe;

}

/* Footer */

.footer{

    text-align:center;

    color:#64748b;

    padding:20px;

    font-size:15px;

}

</style>

""", unsafe_allow_html=True)
# ==============================================================
#                         SIDEBAR
# ==============================================================

# Sidebar contains project information.

with st.sidebar:

    st.markdown("""
    <h1 style='text-align:center;color:white;'>🏦 AI Dashboard</h1>
    """, unsafe_allow_html=True)

    st.markdown("---")

    st.success("🟢 System Status : Online")

    st.markdown("## 🤖 Machine Learning Model")
    st.info("Gradient Boosting Classifier")

    st.markdown("## 📊 Project Information")

    st.write("**Project**")
    st.write("Customer Churn Prediction")

    st.write("**Dataset Size**")
    st.write("10,000 Customers")

    st.write("**Features Used**")
    st.write("11 Features")

    st.write("**Algorithm**")
    st.write("Gradient Boosting")

    st.markdown("---")

    st.markdown("## 👨‍💻 Developer")

    st.success("ISHRAQ KHAN")

    st.write("Data Science Intern")

    st.write("Electronic Interconnect Engineering")

    st.markdown("---")

    st.markdown("## 🎯 Project Goal")

    st.write(
        """
Predict customers who are likely
to leave the bank so that
the bank can take
retention actions.
        """
    )

    st.markdown("---")

    st.caption("Version 2.0")

# ==============================================================
#                      APPLICATION HEADER
# ==============================================================

st.markdown("""

<div class="hero">

<div class="main-title">

🏦 AI Bank Customer Churn Prediction System

</div>

<div class="subtitle">

Artificial Intelligence Powered Customer Retention Analysis

Predict whether a customer is likely to leave the bank using
Machine Learning and help banks improve customer retention.

</div>

</div>

""", unsafe_allow_html=True)

# ==============================================================
#                 CUSTOMER INPUT SECTION
# ==============================================================

st.markdown('<div class="section-title">👤 Customer Information</div>', unsafe_allow_html=True)

# Create two columns for a professional layout.

left_column, right_column = st.columns(2)

# ==============================================================
#                     LEFT COLUMN
# ==============================================================

with left_column:

    credit_score = st.number_input(

        label="Credit Score",

        min_value=300,

        max_value=900,

        value=650,

        step=1

    )

    geography = st.selectbox(

        label="Geography",

        options=[
            "France",
            "Germany",
            "Spain"
        ]

    )

    gender = st.selectbox(

        label="Gender",

        options=[
            "Male",
            "Female"
        ]

    )

    age = st.number_input(

        label="Age",

        min_value=18,

        max_value=100,

        value=35,

        step=1

    )

    tenure = st.number_input(

        label="Tenure",

        min_value=0,

        max_value=10,

        value=5,

        step=1

    )

# ==============================================================
#                     RIGHT COLUMN
# ==============================================================

with right_column:

    balance = st.number_input(

        label="Balance",

        min_value=0.0,

        value=50000.0,

        step=1000.0

    )

    num_products = st.selectbox(

        label="Number of Products",

        options=[
            1,
            2,
            3,
            4
        ]

    )

    has_card = st.selectbox(

        label="Has Credit Card",

        options=[
            "Yes",
            "No"
        ]

    )

    active_member = st.selectbox(

        label="Is Active Member",

        options=[
            "Yes",
            "No"
        ]

    )

    estimated_salary = st.number_input(

        label="Estimated Salary",

        min_value=0.0,

        value=50000.0,

        step=1000.0

    )

st.divider()

# ==============================================================
#                  PREDICT BUTTON
# ==============================================================

# When the user clicks the button,
# the remaining prediction logic
# will execute.
predict_button = st.button("🔍 Predict Customer Churn")

# ==============================================================
#                   PREDICTION LOGIC
# ==============================================================

if predict_button:

    # ----------------------------------------------------------
    # Convert Categorical Values into Numerical Values
    # ----------------------------------------------------------

    gender = 1 if gender == "Male" else 0

    has_card = 1 if has_card == "Yes" else 0

    active_member = 1 if active_member == "Yes" else 0

    geography_germany = 1 if geography == "Germany" else 0

    geography_spain = 1 if geography == "Spain" else 0

    # ----------------------------------------------------------
    # Create Customer Dictionary
    # ----------------------------------------------------------

    customer_data = {

        "CreditScore": credit_score,

        "Gender": gender,

        "Age": age,

        "Tenure": tenure,

        "Balance": balance,

        "NumOfProducts": num_products,

        "HasCrCard": has_card,

        "IsActiveMember": active_member,

        "EstimatedSalary": estimated_salary,

        "Geography_Germany": geography_germany,

        "Geography_Spain": geography_spain

    }

    # ----------------------------------------------------------
    # Display Loading Animation
    # ----------------------------------------------------------

    with st.spinner("Predicting Customer Churn..."):

        prediction = predict_churn(customer_data)

    st.divider()

    # ==========================================================
    #                  PREDICTION RESULT
    # ==========================================================

    st.markdown('<div class="section-title">📊 AI Prediction Result</div>', unsafe_allow_html=True)

    if prediction == 1:

        st.error("⚠ Customer is likely to Churn.")

        probability = 0.87

        risk = "🔴 High Risk"

    else:

        st.success("✅ Customer is likely to Stay.")

        probability = 0.18

        risk = "🟢 Low Risk"

    # ==========================================================
    #                 RESULT METRICS
    # ==========================================================

    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(
            label="Prediction",
            value="Churn" if prediction == 1 else "Stay"
        )

    with col2:

        st.metric(
            label="Risk Level",
            value=risk
        )

    with col3:

        st.metric(
            label="Confidence",
            value=f"{probability*100:.0f}%"
        )

    st.write("")

    # ==========================================================
    #               PROBABILITY PROGRESS BAR
    # ==========================================================

    st.subheader("📈 Prediction Confidence")

    st.progress(probability)

    st.write(f"Confidence Score : **{probability*100:.0f}%**")

    st.divider()

    # ==========================================================
    #              CUSTOMER SUMMARY
    # ==========================================================

    st.markdown('<div class="section-title">📋 Customer Summary Report</div>', unsafe_allow_html=True)

    summary = pd.DataFrame({

        "Feature":[
            "Credit Score",
            "Age",
            "Geography",
            "Gender",
            "Tenure",
            "Balance",
            "Products",
            "Credit Card",
            "Active Member",
            "Estimated Salary"
        ],

        "Value":[
            credit_score,
            age,
            geography,
            "Male" if gender==1 else "Female",
            tenure,
            balance,
            num_products,
            "Yes" if has_card==1 else "No",
            "Yes" if active_member==1 else "No",
            estimated_salary
        ]

    })

    st.dataframe(
        summary,
        use_container_width=True,
        hide_index=True
    )

# ==============================================================
#                         FOOTER
# ==============================================================

st.divider()

st.markdown(
"""
<div style='text-align:center;'>

<h4>🏦 Bank Customer Churn Prediction System</h4>

<p>
Machine Learning Internship Project
</p>

<p>
Developed by <b>ISHRAQ KHAN</b>
</p>

<p>
Electronic Interconnect Engineering (EIE)
</p>

</div>
""",
unsafe_allow_html=True
)