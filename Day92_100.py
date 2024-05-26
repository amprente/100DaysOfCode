#  Create your own weather app.

import requests
import json

# Set your timezone, latitude, and longitude
timezone = "GMT"
latitude = 47.6377
longitude = 26.2595

# Get the weather data from the API
result = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&daily=weathercode,temperature_2m_max,temperature_2m_min&timezone={timezone.upper()}")
weather_data = result.json()

# Extract today's weather information
today_weather = weather_data['daily']['weathercode'][0]
today_max_temp = weather_data['daily']['temperature_2m_max'][0]
today_min_temp = weather_data['daily']['temperature_2m_min'][0]

# Define weather code meanings
def get_weather_description(code):
    if code == 0:
        return "Clear sky"
    elif code == 1:
        return "Mainly clear"
    elif code == 2:
        return "Partly cloudy"
    elif code == 3:
        return "Overcast"
    elif code == 45:
        return "Fog"
    elif code == 48:
        return "Depositing rime fog"
    elif code == 51:
        return "Drizzle: Light intensity"
    elif code == 53:
        return "Drizzle: Moderate intensity"
    elif code == 55:
        return "Drizzle: Dense intensity"
    elif code == 56:
        return "Freezing Drizzle: Light intensity"
    elif code == 57:
        return "Freezing Drizzle: Dense intensity"
    elif code == 61:
        return "Rain: Slight"
    elif code == 63:
        return "Rain: Moderate"
    elif code == 65:
        return "Rain: Heavy"
    elif code == 66:
        return "Freezing Rain: Light"
    elif code == 67:
        return "Freezing Rain: Heavy"
    elif code == 71:
        return "Snow fall: Slight"
    elif code == 73:
        return "Snow fall: Moderate"
    elif code == 75:
        return "Snow fall: Heavy"
    elif code == 77:
        return "Snow grains"
    elif code == 80:
        return "Rain showers: Slight"
    elif code == 81:
        return "Rain showers: Moderate"
    elif code == 82:
        return "Rain showers: Violent"
    elif code == 85:
        return "Snow showers slight"
    elif code == 86:
        return "Snow showers heavy"
    elif code == 95:
        return "Thunderstorm: Slight or moderate"
    elif code == 96:
        return "Thunderstorm with slight hail"
    elif code == 99:
        return "Thunderstorm with heavy hail"
    else:
        return "Unknown weather code"

# Get weather description for today's weather code
weather_description = get_weather_description(today_weather)

# Print the weather information in a nice way
print(f"Today's Weather Forecast for Suceava, Romania:\n")
print(f"Weather: {weather_description}")
print(f"Max Temperature: {today_max_temp}°C")
print(f"Min Temperature: {today_min_temp}°C")
