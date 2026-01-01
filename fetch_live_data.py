import requests
import os
from dotenv import load_dotenv
# 🔹 CricAPI key
CRIC_API_KEY = "CRIC_API_KEY"
# 🔹 OpenWeather key
WEATHER_API_KEY = "WEATHER_API_KEY"
# ✅ Fetch recent match details
def get_match_details(team1, team2):
    url = f"https://api.cricapi.com/v1/currentMatches?apikey={CRIC_API_KEY}"
    try:
        response = requests.get(url)
        data = response.json()
        if "data" not in data:
            print("Error: No data field in response.")
            return None
        for match in data["data"]:
            if team1.lower() in match["teams"][0].lower() and team2.lower() in match["teams"][1].lower() or \
                team2.lower() in match["teams"][0].lower() and team1.lower() in match["teams"][1].lower():
                return {
                    "venue": match.get("venue", "Unknown"),
                    "date": match.get("date", "Unknown"),
                    "matchType": match.get("matchType", "N/A"),
                }
        return None
    except Exception as e:
        print("Match API error:", e)
        return None
# ✅ Fetch weather using OpenWeatherMap API
def get_weather(city_name):
    try:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={WEATHER_API_KEY}&units=metric"
        response = requests.get(url)
        data = response.json()
        # Check for common errors
        if data.get("cod") != 200:
            print("Weather API error:", data)
            return None, None, None
        humidity = data["main"]["humidity"]
        temp = data["main"]["temp"]
        desc = data["weather"][0]["description"]
        return humidity, temp, desc
    except Exception as e:

        print("Weather API exception:", e)

        return None, None, None