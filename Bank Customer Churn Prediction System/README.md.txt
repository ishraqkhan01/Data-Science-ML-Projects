# 🏦 Bank Customer Churn Prediction System

A Machine Learning web application that predicts whether a bank customer is likely to leave (churn) or remain with the bank based on customer demographic and banking information.

---

# 📌 Project Overview

Customer churn is one of the biggest challenges in the banking industry. Losing existing customers increases operational costs because acquiring new customers is significantly more expensive than retaining current ones.

This project uses Machine Learning to analyze customer information and predict the likelihood of customer churn. The trained model is deployed using Streamlit to provide an interactive web application.

---

# 🎯 Objectives

- Predict customer churn accurately.
- Compare multiple Machine Learning models.
- Select the best-performing model.
- Deploy the model as an interactive web application.
- Help banks identify high-risk customers.

---

# 🛠 Technologies Used

| Category | Technology |
|----------|------------|
| Programming Language | Python |
| IDE | VS Code, Jupyter Notebook |
| Data Analysis | Pandas, NumPy |
| Machine Learning | Scikit-learn |
| Model Saving | Joblib |
| Web Framework | Streamlit |
| Version Control | Git & GitHub |

---

# 📂 Project Structure

```
Customer-Churn-Prediction/
│
├── app/
│   ├── app.py
│   └── predict.py
│
├── models/
│   ├── best_model.pkl
│   └── scaler.pkl
│
├── data/
│   └── Churn_Modelling.csv
│
├── notebooks/
│   └── Customer_Churn_Prediction.ipynb
│
├── requirements.txt
│
├── README.md
│
└── .gitignore
```

---

# 📊 Dataset Information

- **Dataset Name:** Bank Customer Churn Dataset
- **Source:** Kaggle
- **Records:** 10,000
- **Features:** 11
- **Target Variable:** Exited

### Input Features

- Credit Score
- Geography
- Gender
- Age
- Tenure
- Balance
- Number of Products
- Has Credit Card
- Is Active Member
- Estimated Salary

### Target

- 0 → Customer Stays
- 1 → Customer Churns

---

# 🚀 Machine Learning Workflow

```
Understand Problem
        ↓
Import Libraries
        ↓
Load Dataset
        ↓
Exploratory Data Analysis (EDA)
        ↓
Data Cleaning
        ↓
Feature Engineering
        ↓
Categorical Encoding
        ↓
Feature Scaling
        ↓
Feature Selection
        ↓
Train-Test Split
        ↓
Logistic Regression
        ↓
Ensemble Models
        ↓
Model Evaluation
        ↓
Model Comparison
        ↓
Feature Importance
        ↓
Business Insights
        ↓
Save Model
        ↓
Streamlit Deployment
```

---

# 🤖 Machine Learning Models

The following models were trained and evaluated:

- Logistic Regression
- Random Forest Classifier
- AdaBoost Classifier
- Gradient Boosting Classifier

### Best Model

🏆 **Gradient Boosting Classifier**

---

# 📈 Model Evaluation

Evaluation metrics used:

- Accuracy
- Precision
- Recall
- F1 Score
- Confusion Matrix

After comparing all models, the Gradient Boosting Classifier achieved the best overall performance and was selected for deployment.

---

# 💻 Streamlit Web Application

The project includes a Streamlit-based user interface where users can:

- Enter customer information
- Predict customer churn
- View prediction confidence
- View customer summary
- Get instant AI-based prediction

---

# 📸 Application Preview

You can add screenshots here after deployment.

Example:

```
screenshots/home.png

screenshots/result.png
```

---

# ⚙ Installation

Clone the repository:

```bash
git clone https://github.com/YourUsername/Customer-Churn-Prediction.git
```

Move into the project folder:

```bash
cd Customer-Churn-Prediction
```

Install the required libraries:

```bash
pip install -r requirements.txt
```

---

# ▶ Running the Application

Move to the app directory:

```bash
cd app
```

Run the Streamlit application:

```bash
streamlit run app.py
```

---

# 📊 Business Insights

Some important insights obtained from the project:

- Older customers are more likely to churn.
- Active members have a lower churn rate.
- Customers with fewer products tend to churn more frequently.
- Customer balance and geography significantly influence churn.

---

# 🚀 Future Improvements

- XGBoost Implementation
- LightGBM
- Deep Learning Model
- Cloud Deployment
- REST API
- User Authentication
- Database Integration
- Prediction History
- Downloadable Reports

---

# 👨‍💻 Developer

**ISHRAQ KHAN**

Data Science Intern

Electronic Interconnect Engineering (EIE)

---

# ⭐ If you found this project useful

Please consider giving this repository a ⭐ on GitHub.

---

# 📄 License

This project is developed for educational and internship purposes.