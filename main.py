import streamlit as st
from prediction_helper import predict  # Linked to prediction_helper.py

# --- Page Configurations ---
st.set_page_config(
    page_title="Tomato Finance: Credit Risk Modelling", 
    page_icon="📊", 
    layout="wide"  # Uses the full screen width for a cleaner dashboard look
)

st.title("📊 Tomato Finance: Credit Risk Modelling")
st.markdown("---")

# --- Form Grid Layout ---
# Row 1: Primary Financial Demographics
row1 = st.columns(3)
with row1[0]:
    age = st.number_input('Age', min_value=18, max_value=100, step=1, value=28)
with row1[1]:
    income = st.number_input('Annual Income (₹)', min_value=0, value=1200000, step=10000)
with row1[2]:
    loan_amount = st.number_input('Requested Loan Amount (₹)', min_value=0, value=2560000, step=10000)

# Calculate dynamic background KPIs
loan_to_income_ratio = loan_amount / income if income > 0 else 0.0

# Row 2: Ratios & Tenure
row2 = st.columns(3)
with row2[0]:
    # Styled cleanly as a professional financial metric component
    st.metric(label="Loan to Income Ratio", value=f"{loan_to_income_ratio:.2f}")
with row2[1]:
    loan_tenure_months = st.number_input('Loan Tenure (Months)', min_value=1, step=1, value=36)
with row2[2]:
    avg_dpd_per_delinquency = st.number_input('Avg DPD (Days Past Due)', min_value=0, value=20)

# Row 3: Credit History Records
row3 = st.columns(3)
with row3[0]:
    delinquency_ratio = st.number_input('Delinquency Ratio (%)', min_value=0, max_value=100, step=1, value=30)
with row3[1]:
    credit_utilization_ratio = st.number_input('Credit Utilization Ratio (%)', min_value=0, max_value=100, step=1, value=30)
with row3[2]:
    num_open_accounts = st.number_input('Open Loan Accounts', min_value=1, max_value=20, step=1, value=2)

# Row 4: Categorical Applications
row4 = st.columns(3)
with row4[0]:
    residence_type = st.selectbox('Residence Type', ['Owned', 'Rented', 'Mortgage'])
with row4[1]:
    loan_purpose = st.selectbox('Loan Purpose', ['Education', 'Home', 'Auto', 'Personal'])
with row4[2]:
    loan_type = st.selectbox('Loan Type', ['Unsecured', 'Secured'])

st.markdown("---")

# --- Action & Output Block ---
if st.button('🚀 Calculate Credit Risk', use_container_width=True):
    
    # Run predictions via helper module
    probability, credit_score, rating = predict(
        age, income, loan_amount, loan_tenure_months, avg_dpd_per_delinquency,
        delinquency_ratio, credit_utilization_ratio, num_open_accounts,
        residence_type, loan_purpose, loan_type
    )

    st.markdown("### 📋 Risk Assessment Results")
    
    # Draw results inside a 3-column structured receipt card
    res_col1, res_col2, res_col3 = st.columns(3)
    
    with res_col1:
        # High probabilities display with warning shades automatically
        if probability > 0.30:
            st.error(f"**Default Probability:**\n### {probability:.2%}")
        else:
            st.success(f"**Default Probability:**\n### {probability:.2%}")
            
    with res_col2:
        st.info(f"**Credit Score:**\n### {credit_score}")
        
    with res_col3:
        st.success(f"**Risk Rating Assigned:**\n### Grade {rating}")