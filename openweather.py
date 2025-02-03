import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

def get_weather_data(api_key, cities):
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    raining_cities = []
    
    for city in cities:
        params = {"q": city, "appid": api_key, "units": "metric"} # For temperature in Celsius use units=metric
        response = requests.get(base_url, params=params)
        
        if response.status_code == 200:
            data = response.json()
            weather_conditions = data.get("weather")
            
            if any("rain" in condition.get("main", "").lower() for condition in weather_conditions):
                raining_cities.append((city, data["main"]["temp"], weather_conditions[0]["description"]))
        else:
            print(f"Failed to get weather data for {city}: {response.status_code}")
    
    return raining_cities

def generate_report(raining_cities):
    if not raining_cities:
        print("No cities are experiencing rain at the moment.")
        return
    
    print("Cities currently experiencing rain:")
    for city, temp, description in raining_cities:
        print(f"- {city}: {description}, {temp}°C")

if __name__ == "__main__":
    API_KEY = os.getenv("API_KEY")
    
    f1_2025_cities = [
        "Melbourne",        # Australia
        "Shanghai",         # China
        "Suzuka",           # Japan
        "Sakhir",           # Bahrain
        "Jeddah",           # Saudi Arabia
        "Miami",            # USA
        "Imola",            # Italy
        "Monaco",           # Monaco
        "Barcelona",        # Spain
        "Montreal",         # Canada
        "Spielberg",        # Austria
        "Silverstone",      # United Kingdom
        "Spa",              # Belgium
        "Budapest",         # Hungary
        "Zandvoort",        # Netherlands
        "Monza",            # Italy
        "Baku",             # Azerbaijan
        "Singapore",        # Singapore
        "Austin",           # USA
        "Mexico City",      # Mexico
        "Sao Paulo",        # Brazil
        "Las Vegas",        # USA
        "Lusail",           # Qatar
        "Yas Marina"        # Abu Dhabi
    ]
    
    raining_cities = get_weather_data(API_KEY, f1_2025_cities)
    generate_report(raining_cities)
