import requests
import pandas as pd
from datetime import datetime
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# -------------------------------
# ETL Part: Pull weather data
# -------------------------------
API_URL = "https://api.open-meteo.com/v1/forecast?latitude=40.71&longitude=-74.01&hourly=temperature_2m"
response = requests.get(API_URL)
data = response.json()

# Convert to DataFrame
df = pd.DataFrame(data['hourly']['temperature_2m'], columns=['temperature'])
df['timestamp'] = pd.date_range(start=datetime.now(), periods=len(df), freq='h')

# Save to CSV
df.to_csv("weather_data.csv", index=False)
print("Weather data saved to weather_data.csv")

# -------------------------------
# ML Part: Predict temperature trends
# -------------------------------
# Prepare data for ML
df['hour'] = df.index  # Simple feature: hour index
X = df[['hour']]
y = df['temperature']

# Train a simple linear regression model
model = LinearRegression()
model.fit(X, y)

# Predict temperatures
df['predicted_temp'] = model.predict(X)

# Print results
print(df.head())

# Plot actual vs predicted temperatures
plt.plot(df['hour'], df['temperature'], label="Actual Temp")
plt.plot(df['hour'], df['predicted_temp'], label="Predicted Temp", linestyle='--')
plt.xlabel("Hour")
plt.ylabel("Temperature")
plt.title("Weather Temperature Prediction")
plt.legend()

# ✅ ADD THIS LINE
plt.savefig("temperature_plot.png")

plt.show()
