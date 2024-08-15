# backend code for fetching weather data

import requests as rq 
from configparser import ConfigParser

# get key from config file 
configuration_file = "config.ini"
configuration = ConfigParser()
configuration.read(configuration_file)
api_key = configuration['weather_wizard']['api_key']
url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid={}'

# function to retrieve data from openweathermap

def fetchweather(city):
    result = rq.get(url.format(city,api_key))

    if result:
        json = result.json()
        city = json['name']
        country = json['sys']
        temp_kelvin = json['main']['temp']
        temp_celsius = temp_kelvin -273.15
        weather1 = json['weather'][0]['main']
        humidity = json['main']['humidity']
        visibility = json['visibility']
        wind_speed = json['wind']['speed']
        final = [city,country,temp_kelvin,temp_celsius,weather1,visibility,wind_speed,humidity]
        return final 
    else:
        print("No Content Found")



