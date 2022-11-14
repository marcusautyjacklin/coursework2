from cities import City, CityCollection
from pathlib import Path
import csv

def read_attendees_file(filepath: Path) -> CityCollection:

    filepath = Path("attendee_locations.csv")

    file = open(filepath)
    csv_file = csv.reader(file)
    next(csv_file)
    variables = vars()
    cities = []

    for row in csv_file:
        name = row[3]
        name.replace(" ","_")
        name = name.lower()
        print(type(name))
        variables[name] = City(str(row[3]), str(row[1]), int(row[0]), float(row[4]), float(row[5]))