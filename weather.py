import requests    # imported to query internet
from dotenv import load_dotenv #2
import os
from dataclasses import dataclass

load_dotenv()
api_key = os.getenv('API_KEY')  # it imports the value from .env folder e.g. here API_KEY will be retrived

@dataclass
class WeatherData:
    main: str
    description: str
    icon: str
    temperatur: int
    feels_like: int
    min_temp: int 
    max_temp: int
    humidity: int
    wind_speed: float

    

def get_lat_lon(city_name,state_code,country_code,API_key):
    resp = requests.get(f'http://api.openweathermap.org/geo/1.0/direct?q={city_name},{state_code},{country_code}&appid={API_key}').json()  #1. converted to a f-string 
    print(resp)
    print("-----------------------------------------------------")
    data = resp[0]
    lat, lon = data.get('lat'), data.get('lon') 
    return lat, lon



def get_current_weather(lat, lon, API_key):
    resp = requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_key}&units=metric').json()
    print(resp)
   
    data = WeatherData(
        main = resp.get('weather')[0].get('main'),
        description = resp.get('weather')[0].get('description'),
        icon = resp.get('weather')[0].get('icon'),
        temperatur = int(resp.get('main').get('temp')),
        feels_like = int(resp.get('main').get('feels_like')),
        min_temp = int(resp.get('main').get('temp_min')),
        max_temp = int(resp.get('main').get('temp_max')),
        humidity = resp.get('main').get('humidity'),
        wind_speed = resp.get('wind').get('speed')

    )
    return data

def main(city_name,state_name,country_name):
    print('----------------------------------------------------')
    lat, lon = get_lat_lon(city_name, state_name ,country_name , api_key)
    weather_data = get_current_weather(lat, lon, api_key)
    return weather_data
