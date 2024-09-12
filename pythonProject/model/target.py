class Target:

    def __init__(self, city, priority, lat, lon, weather_info):
        self.city = city
        self.priority = priority
        self.lat = lat
        self.lon = lon
        self.weather_info = weather_info

    def __repr__(self):
        return f"{self.city}: priority={self.priority}, wind={self.weather_info.wind_speed}"