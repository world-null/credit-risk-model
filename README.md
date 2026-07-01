# 📊 Tomato Finance: Credit Risk Modelling

An end-to-end data analytics and machine learning application that predicts loan default probabilities, assigns credit scores, and evaluates risk ratings for retail banking prospects. 

This interactive dashboard is built using **Python**, **Scikit-Learn**, and **Streamlit** to simulate a real-world automated credit underwriting engine.

---

## 🛠️ Tech Stack & Concepts Used

* **Frontend Dashboard:** Streamlit (Wide-layout responsive UI)
* **Data Manipulation:** Pandas, NumPy
* **Machine Learning Foundation:** Logistic Regression Coefficients / Linear Odds Mapping
* **Data Pipeline:** Preprocessing via `MinMaxScaler`
* **Model Serialization:** Joblib

---

## ⚙️ How the Risk Engine Works

1. **Automated Feature Engineering:** Dynamically computes the critical **Loan-to-Income Ratio** from the frontend input to feed the risk framework.
2. **Robust Scaler Realignment:** Integrates dummy placeholder pipelines (`number_of_dependants`, `enquiry_count`, etc.) to perfectly align single-row real-time production inputs with historical multi-column training dimensions without shape mismatches.
3. **Linear Score Mapping:** Manually calculates raw log-odds via dot products (`np.dot`), converts them to traditional sigmoid probabilities, and scales non-default weights linearly into a consumer credit-bureau score ranging from **300 to 900**.

---

## 📋 Risk Rating Thresholds

* **Excellent:** 750 – 900
* **Good:** 650 – 749
* **Average:** 500 – 649
* **Poor:** 300 – 499

