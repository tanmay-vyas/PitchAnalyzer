# test_weather.py
from fetch_live_data import get_weather
import os

# Ensure any weather API key (e.g., OPENWEATHER_API_KEY) is set in your .env

city = "Vadodara" # Or any test city

print(f"Testing weather for {city}...")
temp, humidity, desc = get_weather(city)

if temp is not None:
    print(f"✅ Success! Weather: {desc}, Temp: {temp}°C, Humidity: {humidity}%")
else:
    print(f"❌ Failure. Check API key/URL in fetch_live_data.py. Result: {desc}")