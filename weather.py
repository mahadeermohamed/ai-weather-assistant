import requests, os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("WEATHER_API_KEY")

def get_weather(city):
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"
    }

    try:
        response =requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
        temp = data["main"]["temp"]
        description = data["weather"][0]["description"]
        return f"Temperature: {temp}°C, Condition: {description}"
    except requests.exceptions.RequestException as e:
        print(f"Couldn't fetch weather: {e}")
        return None

