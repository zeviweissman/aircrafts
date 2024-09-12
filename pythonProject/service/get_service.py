import api_service
import json_service
from functools import reduce, partial
from itertools import groupby
from utils.convert_utils import *
from utils.calc_utils import *

PILOTS_PATH = "../json/pilots.json"
AIRCRAFTS_PATH = "../json/aircraft.json"
TARGETS_PATH = "../json/targets.json"


def get_all_pilots():
    json_pilots = json_service.read_from_file(PILOTS_PATH)
    pilots = list(map(json_to_poilt, json_pilots))
    return pilots

def get_all_aircrafts():
    json_aircrafts = json_service.read_from_file(AIRCRAFTS_PATH)
    aircrafts = list(map(json_to_aircraft, json_aircrafts))
    return aircrafts

def get_all_targets():
    json_targets = json_service.read_from_file(TARGETS_PATH)
    targets = [_get_target(target) for target in json_targets]
    return targets

def _get_target(target_json):
    weather_json = api_service.get_weather_by_city(target_json["Target City"])
    weather_info = json_to_weather_info(weather_json)
    target = create_target(target_json, weather_info)
    return target

def get_geo_location_by_city(city):
    geo_location_json = api_service.get_geo_by_city(city)[0]
    geo_location = json_to_geo_location(geo_location_json)
    return geo_location



def create_missions_from_aircraft_and_target(aircraft, origin_location, target):
    pilots = get_all_pilots()
    missions = map(lambda pilot: create_mission(origin_location, aircraft, pilot, target), pilots)
    missions_with_scores = map(lambda mission:(mission, calc_score(mission)), missions)
    return list(missions_with_scores)


def create_missions_for_target(aircrafts, origin_location ,target):
    return reduce(lambda li, next_aircraft: li + create_missions_from_aircraft_and_target(next_aircraft,origin_location, target) ,aircrafts , [])


aircraft_could_reach_distance = lambda aircraft ,distance : aircraft.fuel_capacity - distance > 0

def get_all_available_missions_by_target(origin_location, target):
    distance = distance_between_geo_locations(origin_location, target)
    aircrafts = get_all_aircrafts()
    filtered_aircraft = [aircraft for aircraft in aircrafts if aircraft_could_reach_distance(aircraft, distance)]
    missions = create_missions_for_target(filtered_aircraft, origin_location, target)
    return missions



def get_all_available_missions_by_origin(origon_location):
    targets = get_all_targets()
    missions = reduce(lambda li, next_target: li + get_all_available_missions_by_target(origon_location,next_target), targets, [] )
    return missions


a = get_all_available_missions_by_origin((31.79592425, 35.21198075969497))
b = groupby(iter(a), key=lambda tu: tu[0].aircraft.type)
d = {k:list(g) for k,g in b}
c = [[k,list(g)] for k,g in b]
print(a)
print(c)
print(d)

