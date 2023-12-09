from dotenv import load_dotenv
from pprint import pprint
import requests
import os

load_dotenv()


def get_current_weather(city="Minneapolis"):
    requests_url= f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&appid={os.getenv('API_KEY')}"

    weather_data= requests.get(requests_url).json()

    return weather_data



if __name__ == "__main__":
    print('\n*** Get Current Weather Conditions ***\n')

    city= input("\nPlease enter a city name:")

    # Check for empty string or string with only spaces
    if not bool(city.strip()):
        city= "Minneapolis"

    weather_data= get_current_weather(city)

    print("\n")
    pprint(weather_data)

