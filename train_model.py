import os
import pandas as pd
import joblib
from sklearn.ensemble import RandomForestRegressor

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATA_FILE = os.path.join(BASE_DIR, "data", "raw", "uber-raw-data-apr14.csv")
MODEL_FILE = os.path.join(BASE_DIR, "models", "uber_model.pkl")

df = pd.read_csv(DATA_FILE)

df['Date/Time'] = pd.to_datetime(df['Date/Time'])
df['hour'] = df['Date/Time'].dt.hour
df['day'] = df['Date/Time'].dt.day
df['month'] = df['Date/Time'].dt.month
df['day_of_week'] = df['Date/Time'].dt.dayofweek

hourly_df = df.groupby(['hour','day','month','day_of_week']).size().reset_index(name='demand')

X = hourly_df[['hour','day','month','day_of_week']]
y = hourly_df['demand']

model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X, y)

os.makedirs(os.path.dirname(MODEL_FILE), exist_ok=True)
joblib.dump(model, MODEL_FILE)

print("Model trained successfully ✅")
print("Saved at:", MODEL_FILE)