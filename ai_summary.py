import requests, os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")



def summarize_with_ai(weather_text, city):
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-3-flash-preview:generateContent?key={API_KEY}"

    prompt = f"Here is the weather data for {city}: {weather_text}.Write one friendly, casual sentence telling the user what to expect today."

    payload = {
        "contents":
            [
                {"parts":
                 [
                     {"text": prompt}
                 ]
                }
            ]
    }
    try:
        response = requests.post(url, json=payload, timeout=10)
        response.raise_for_status()
        data = response.json()
        reply = data["candidates"][0]["content"]["parts"][0]["text"]
        return reply
    except requests.exceptions.RequestException as e:
        print(f"AI summary failed: {e}")
        return "Sorry, couldn't generate a summary right now."