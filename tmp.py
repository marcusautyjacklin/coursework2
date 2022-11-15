from utils import read_attendees_file
from cities import City, CityCollection
from pathlib import Path
import csv

filepath = Path("attendee_locations.csv")
city_collection, cities_dict = read_attendees_file(Path("attendee_locations.csv"))


# zurich = City('Zurich', 'Switzerland', 52, 47.22, 8.33)
# san_francisco = City('San Francisco', 'United States', 71, 37.77, -122.41)
# greenwich = City('London', 'United Kingdom', 15, 51.48, 0.)
# algiers = City('Algiers', 'Algeria', 1, 28.0000272,	2.9999825)
# canberra = City('Canberra','Australia', 54, -35.2975906, 149.1012676)

# city_collection = CityCollection([zurich, san_francisco, greenwich, algiers, canberra])

# Usage: city_collection.cities[cities_dict["algiers"]] for City class relating to algiers

# print(city_collection.co2_by_country(city_collection.cities[cities_dict["london"]]))
# print(city_collection.travel_by_country(city_collection.cities[cities_dict["london"]]))
# print(city_collection.cities[cities_dict["london"]].co2_to(city_collection.cities[cities_dict["zurich"]]))

# london = City('London', 'UK', 10, -10., 10.)
# paris = City('Paris', 'France', 10, -80., 10.)

# print(london)
# print(paris)
# print(london.distance_to(paris))
# print(london.co2_to(paris))

# print(city_collection.summary(city_collection.cities[cities_dict["london"]]))

# city_collection.sorted_by_emissions()

city_collection.plot_top_emitters(city_collection.cities[cities_dict["beijing"]],10,True)
# city_collection.plot_top_emitters(zurich, 3, False)

# print(city_collection.cities[cities_dict["london"]].distance_to(city_collection.cities[cities_dict["paris"]]))
# c = list(a.items())

# d = []
# e = []
# for i in range(0,len(a)):
#     d.append(c[i][0])
#     e.append(c[i][1])