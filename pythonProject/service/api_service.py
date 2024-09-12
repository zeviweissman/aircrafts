import requests
from functools import partial

API_KEY = "&appid=508ae454d0f001dea71b1861b24c3815"
WEATHER_URL = "https://api.openweathermap.org/data/2.5/forecast?q="
GEO_URL = "http://api.openweathermap.org/geo/1.0/direct?q="




def generate_url(url, api_key, city):
    city_with_no_space = city.replace(" ", "%20")
    return f"{url}{city_with_no_space}{api_key}"

generate_weather_url = partial(generate_url,WEATHER_URL,API_KEY)
generate_geo_url = partial(generate_url,GEO_URL,API_KEY)



def get_from_api(url):
    response = requests.request('GET', url)
    return response.json()


def get_weather_by_city(city):
    url = generate_weather_url(city)
    print(url)
    return get_from_api(url)


def get_geo_by_city(city):
    url = generate_geo_url(city)
    return get_from_api(url)

