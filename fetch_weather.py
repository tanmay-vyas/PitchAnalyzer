import requests


API_KEY = "YOUR_OPENWEATHERMAP_API_KEY"

def get_weather(city_name):
    try:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}&units=metric"
        response = requests.get(url)
        data = response.json()

        # 🧠 Handle if city is not found or API limit exceeded
        if response.status_code != 200 or "main" not in data:
            print("Weather API error:", data)
            return None, None, None

        humidity = data["main"]["humidity"]
        temp = data["main"]["temp"]
        desc = data["weather"][0]["description"].capitalize()

        return humidity, temp, desc

    except Exception as e:
        print("Error fetching weather:", e)
        return None, None, None
