import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from joblib import dump
import os

# Create folders if not exist
os.makedirs("model", exist_ok=True)
os.makedirs("data", exist_ok=True)

# Load dataset
df = pd.read_csv("data/telco_churn.csv")

# ---------------------------
# DATA CLEANING
# ---------------------------

# Target variable
df['Churn'] = df['Churn'].map({'Yes': 1, 'No': 0})

# Encode categorical columns
df['gender'] = df['gender'].map({'Female': 0, 'Male': 1})
df['SeniorCitizen'] = df['SeniorCitizen'].map({'No': 0, 'Yes': 1}) \
    if df['SeniorCitizen'].dtype == object else df['SeniorCitizen']

# Fix TotalCharges
df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
df['TotalCharges'] = df['TotalCharges'].fillna(0)

# ---------------------------
# FEATURES (ONLY NUMERIC)
# ---------------------------
features = [
    'gender',
    'SeniorCitizen',
    'tenure',
    'MonthlyCharges',
    'TotalCharges'
]

X = df[features]
y = df['Churn']

# ---------------------------
# TRAIN TEST SPLIT
# ---------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# ---------------------------
# MODEL PIPELINE
# ---------------------------
pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('model', LogisticRegression(max_iter=1000))
])

pipeline.fit(X_train, y_train)

# Save model
dump(pipeline, "model/churn_model.pkl")

print("✅ Model trained and saved successfully")
