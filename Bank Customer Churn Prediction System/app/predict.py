import os
import joblib
import pandas as pd

# Current file (predict.py) ka folder path nikalna
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Relative paths ko absolute paths me convert karna
MODEL_PATH = os.path.join(BASE_DIR, "..", "models", "best_model.pkl")
SCALER_PATH = os.path.join(BASE_DIR, "..", "models", "scaler.pkl")

# Load Model
model = joblib.load(MODEL_PATH)

# Load Scaler
scaler = joblib.load(SCALER_PATH)

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
