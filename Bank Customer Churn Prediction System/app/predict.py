import joblib
import pandas as pd

# Load Model
model = joblib.load("../models/best_model.pkl")

# Load Scaler
scaler = joblib.load("../models/scaler.pkl")

# Numerical columns used during scaling
numerical_features = [
    "CreditScore",
    "Age",
    "Tenure",
    "Balance",
    "NumOfProducts",
    "EstimatedSalary"
]

def predict_churn(customer_data):

    # Convert dictionary into DataFrame
    input_df = pd.DataFrame([customer_data])

    # Scale only numerical features
    input_df[numerical_features] = scaler.transform(
        input_df[numerical_features]
    )

    # Predict
    prediction = model.predict(input_df)

    return prediction[0]