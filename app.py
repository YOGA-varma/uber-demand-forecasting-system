import os
import pandas as pd
import streamlit as st
import joblib

# =========================
# TITLE
# =========================
st.title("🚖 Uber Demand Forecasting App")

# =========================
# SAFE PATH SETUP
# =========================
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

model_path = os.path.join(BASE_DIR, "models", "uber_model.pkl")
data_path = os.path.join(BASE_DIR, "data", "raw", "uber-raw-data-apr14.csv")

# =========================
# LOAD MODEL
# =========================
if not os.path.exists(model_path):
    st.error("❌ Model not found. Please run train_model.py first.")
    st.stop()

model = joblib.load(model_path)

# =========================
# LOAD DATA (for reference only)
# =========================
if not os.path.exists(data_path):
    st.error("❌ Dataset not found.")
    st.stop()

df = pd.read_csv(data_path)

df['Date/Time'] = pd.to_datetime(df['Date/Time'])

df['hour'] = df['Date/Time'].dt.hour
df['day'] = df['Date/Time'].dt.day
df['month'] = df['Date/Time'].dt.month
df['day_of_week'] = df['Date/Time'].dt.dayofweek

# =========================
# UI SECTION
# =========================
st.subheader("📊 Predict Uber Demand")

hour = st.slider("Hour", 0, 23, 12)
day = st.slider("Day", 1, 31, 15)
month = st.slider("Month", 1, 12, 4)
day_of_week = st.slider("Day of Week (0=Mon, 6=Sun)", 0, 6, 2)

# =========================
# PREDICTION
# =========================
if st.button("Predict Demand"):
    prediction = model.predict([[hour, day, month, day_of_week]])
    st.success(f"🚖 Estimated Uber Demand: {int(prediction[0])} rides")

# =========================
# BASIC INSIGHTS (BONUS FOR MARKS)
# =========================
st.subheader("📈 Quick Insights")

col1, col2 = st.columns(2)

with col1:
    st.write("Peak Hour Demand")
    st.write(df.groupby('hour').size().sort_values(ascending=False).head(5))

with col2:
    st.write("Weekend vs Weekday")
    df['is_weekend'] = df['day_of_week'].apply(lambda x: 1 if x >= 5 else 0)
    st.write(df.groupby('is_weekend').size())