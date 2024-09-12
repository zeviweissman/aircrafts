class Mission:

    def __init__(self, origin, aircraft, pilot, target):
        self.origin = origin
        self.aircraft = aircraft
        self.pilot = pilot
        self.target = target


    def __repr__(self):
        return f"{self.aircraft.type} - {self.pilot.name} - {self.target.city}"