import csv
from typing import List
from toolz import  pipe, partial

CSV_PATH = "../repos/missions.csv"


def write_missions_to_csv(missions):
    try:
        with open(CSV_PATH, 'w', newline='') as csvfile:
            csv_writer = csv.DictWriter(csvfile, fieldnames=['id','city' ,'aircraft', 'pilot', 'priority', 'score'])
            csv_writer.writeheader()

            for mission in missions:
                csv_writer.writerow({
                    'id': 1,
                    'aircraft': mission[0].aircraft.type,
                    'pilot': mission[0].pilot.name,
                    'score': mission[1],
                    'city': mission[0].target.city,
                    'priority': mission[0].target.priority
                })
    except Exception as e:
        print(e)