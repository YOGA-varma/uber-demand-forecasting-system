# 🚖 Uber Demand Forecasting Using Machine Learning

## 📌 Project Overview
This project predicts Uber ride demand using Machine Learning. It analyzes historical ride data and finds patterns based on time (hour, day, month, weekday). A Random Forest model is used to forecast demand, and a Streamlit web app is built for real-time prediction.

## 🎯 Objective
- Analyze Uber ride demand patterns  
- Identify peak hours and trends  
- Build ML prediction model  
- Create web app for live prediction  

## 🛠️ Technologies Used
- Python  
- Pandas  
- NumPy  
- Scikit-learn  
- Matplotlib  
- Seaborn  
- Streamlit  
- Joblib  

## 📂 Project Structure
uber-demand-forecasting-system/  
├── app/ → Streamlit web app  
├── src/ → Model training scripts  
├── notebook/ → Data analysis (EDA)  
├── data/ → Dataset files  
├── models/ → Trained ML model (.pkl)  
└── README.md  

## ⚙️ How to Run

Install dependencies:
pip install -r requirements.txt  

Train model:
python src/train_model.py  

Run app:
streamlit run app/app.py  

## 🤖 Machine Learning Model
Random Forest Regressor is used to predict Uber demand based on time features like hour, day, month, and weekday.

## ✨ Features
- Predict Uber demand in real-time  
- Analyze peak hour patterns  
- Interactive Streamlit UI  
- Simple and user-friendly design  

## 📈 Future Improvements
- Use XGBoost / LSTM for better accuracy  
- Add location-based prediction  
- Deploy on cloud (Streamlit / AWS)  
- Add dashboards  

## 👨‍💻 Author
Final Year Machine Learning Project
