from cities import City, CityCollection
from pathlib import Path
import csv


filepath = Path("attendee_locations.csv")


def read_attendees_file(filepath: Path) -> CityCollection:

    file = open(filepath)
    csv_file = csv.reader(file)
    next(csv_file)
    variables = vars()
    cities_dict = {}
    city_list = []

    for row in csv_file:
        name = row[3]
        name = name.replace(" ","_")
        name = name.lower()
        # Create dictionary with city name as the key and value which corresponds to the index of city_list holding the City class for this city.
        cities_dict[name] = csv_file.line_num-2
        # Append class to list with for corresponding row in input csv. Dictionary has associated index for each city.
        city_list.append(City(str(row[3]), str(row[1]), int(row[0]), float(row[4]), float(row[5])))

    return cities_dict, city_list

cities_dict, city_list = read_attendees_file(Path("attendee_locations.csv"))
print(city_list[cities_dict["algiers"]])


