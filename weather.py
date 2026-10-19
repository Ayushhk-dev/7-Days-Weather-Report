# All Shit Imports

import requests
from datetime import datetime, timedelta
import pandas as pd
import matplotlib.pyplot as plt
import os


# Data From user
city = input("Enter city name: ")

# City Name -> Latitude,Longitude

geo_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1"
geo_response = requests.get(geo_url)
geo_data = geo_response.json()

# Exception
if "results" not in geo_data:
    print(f"City {city} not found.")
    exit()

latitude = geo_data["results"][0]["latitude"]
longitude = geo_data["results"][0]["longitude"]

# Calculate Dates
today = datetime.now()
week_ago = today - timedelta(days=7)

# Format Dates For API (YYYY-MM-DD)
start_date = week_ago.strftime("%Y-%m-%d")
end_date = today.strftime("%Y-%m-%d")

# Get Weather For Past Week
url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&start_date={start_date}&end_date={end_date}&daily=temperature_2m_max,temperature_2m_min"

response = requests.get(url)
data = response.json()
print(data)


# Extract the daily data
daily_data = data["daily"]

# Creating a DataFrame
df = pd.DataFrame(
    {
        "date": daily_data["time"],
        "max_temp": daily_data["temperature_2m_max"],
        "min_temp": daily_data["temperature_2m_min"],
    }
)

# Convert Date Strings To Datetime
df["date"] = pd.to_datetime(df["date"])

print(df)

# Make The Plot
plt.figure(figsize=(10, 6))
plt.plot(df["date"], df["max_temp"], marker="o", label="Max Temp")
plt.plot(df["date"], df["min_temp"], marker="o", label="Min Temp")

# Labels And Titles
plt.xlabel("Date")
plt.ylabel("Temperature (°C)")
plt.title(f"{city} - Past 7 Days")
plt.legend()

# Rotate x-axis for better understanding
plt.xticks(rotation=45)
plt.tight_layout()

# Save the plot
plt.savefig(f"{city}_chart.png")
plt.show()

if not os.path.exists("data"):
    os.makedirs("data")

# Save to CSV And Location
df.to_csv(f"data/{city}_weather.csv", index=False)
print(f"Data saved to data/{city} Weather.csv")

print("Files saved in 'data' folder")
