import math

# Function to calculate the distance between two coordinates using the Haversine formula
def _haversine_distance(lat1, lon1, lat2, lon2):
     r = 6371.0 # Radius of the Earth in kilometers
     # Convert degrees to radians
     lat1_rad = math.radians(lat1)
     lon1_rad = math.radians(lon1)
     lat2_rad = math.radians(lat2)
     lon2_rad = math.radians(lon2)
     # Calculate differences between the coordinates
     dlat = lat2_rad - lat1_rad
     dlon = lon2_rad - lon1_rad
     # Apply Haversine formula
     a = math.sin(dlat / 2)**2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(dlon /2)**2
     c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
     # Calculate the distance
     distance = r * c
     return distance

weather_scores = {"clear":1.0 ,"clouds":0.7, "rain":0.4, "stormy":0.2}
def calc_weather_score(weather):
    return weather_scores.get(weather,0)



def distance_between_geo_locations(geo_location_tuple, target_city):
     return _haversine_distance(geo_location_tuple[0],geo_location_tuple[1], target_city.lat, target_city.lon)




def calc_score(mission):
     origin = mission.origin
     target = mission.target
     distance = distance_between_geo_locations(origin, target)
     speed = mission.aircraft.speed
     execuation_time = distance / speed
     weather = mission.target.weather_info
     weather_score = calc_weather_score(weather)
     pilot_skill = mission.pilot.skill
     fuel_capacity = mission.aircraft.fuel_capacity
     return weather_score + pilot_skill - execuation_time - (fuel_capacity/1000)





