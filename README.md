# Weather Buddy — AI Weather Summarizer

A CLI tool that fetches live weather data for any city and uses an LLM 
to explain it in a simple, friendly sentence instead of raw numbers.

## Why I built this
To practice combining a regular API (weather data) with an LLM API, 
and to understand prompt engineering for consistent output.

## How it works
1. User enters a city name
2. App fetches live weather data from OpenWeatherMap API
3. Data is sent to an LLM with a prompt asking for a plain-language summary
4. Friendly summary is printed to the user

## Tech stack
Python, requests, Gemini API, python-dotenv

## How to run
1. Clone this repo
2. Create a `.env` file with your API keys (see `.env.example`)
3. `pip install -r requirements.txt`
4. `python main.py`

## Example output
Enter a city: Kumbakonam
 It's a warm and humid day in Kumbakonam, around 32°C — light clothing
 and staying hydrated would be a good idea.


## What I learned
Handling nested JSON responses, writing prompts that give consistent 
output format, and chaining two APIs together in one pipeline.
