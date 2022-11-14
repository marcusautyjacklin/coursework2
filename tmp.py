from utils import read_attendees_file
from cities import City, CityCollection
from pathlib import Path
import csv

filepath = Path("attendee_locations.csv")
collection, cities_dict = read_attendees_file(Path("attendee_locations.csv"))

collection.countries()