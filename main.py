from weather import get_weather
from ai_summary import summarize_with_ai

def main():
    print("Weather Summary Tool - type 'exit' to quit")

    while True:
        city = input("\nEnter a city name: ")

        if city.lower() == "exit":
            print("See you next time")
            break

        weather_data = get_weather(city)
        if weather_data is None:
            print("Couldn't fetch weather for that cityt. Try again later.")
            continue

        summary = summarize_with_ai(weather_data, city)
        print(f"\n{summary}")

if __name__ == "__main__":
    main()