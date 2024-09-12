from model.pilot import Pilot
from model.target import Target
from model.aircraft import Aircraft
from model.weather import Weather_info
from model.mission import Mission
from toolz import get_in


def json_to_poilt(json):
    return Pilot(
        name=json["name"],
        skill=json["skill"]
    )

def create_target(json, weather_info):
    return Target(
        city=json["Target City"],
        priority=json["Priority"],
        lat=json["lat"],
        lon=json["lon"],
        weather_info=weather_info

    )

def json_to_aircraft(json):
    return Aircraft(
        type=json["type"],
        fuel_capacity=json["fuel_capacity"],
        speed=json["speed"]
    )


def json_to_weather_info(json):
    weather_list = json["list"]
    midnight_weather = next(weather for weather in weather_list if "00:00:00" in weather["dt_txt"])
    main = get_in([0, "main"], midnight_weather)
    clouds = get_in(["clouds", "all"], midnight_weather)
    wind_speed = get_in(["wind", "speed"], midnight_weather)
    return Weather_info(
        main=main,
        clouds=clouds,
        wind_speed=wind_speed
    )


def json_to_geo_location(json):
    return (json["lat"], json["lon"])



def create_mission(origin_location, aircraft, pilot, target):
    return Mission(
        origin=origin_location,
        aircraft=aircraft,
        pilot=pilot,
        target=target
    )
