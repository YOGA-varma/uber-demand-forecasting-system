🚖 Uber Demand Forecasting Using Machine Learning
Project Overview

This project predicts Uber ride demand using Machine Learning. It analyzes historical ride data and finds patterns based on time such as hour, day, month, and weekday. A Random Forest model is used to predict future demand, and a Streamlit app is built for real-time prediction.

Objective
Analyze Uber ride data
Identify demand patterns
Build prediction model
Create web app for live prediction
Technologies Used
Python
Pandas
NumPy
Scikit-learn
Matplotlib
Seaborn
Streamlit
Joblib
Project Structure

uber-demand-forecasting-system/
├── app/ (Streamlit app)
├── src/ (Model training code)
├── notebook/ (EDA analysis)
├── data/ (Dataset)
├── models/ (Saved ML model)
└── README.md

How to Run

Install dependencies:
pip install -r requirements.txt

Train model:
python src/train_model.py

Run app:
streamlit run app/app.py

Model Used

Random Forest Regressor is used for prediction of Uber demand based on time features.

Features
Predict Uber demand
Analyze peak hours
Interactive Streamlit UI
Real-time prediction
