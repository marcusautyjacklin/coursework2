from cities import City, CityCollection
from pathlib import Path
import csv

def read_attendees_file(filepath: Path) -> CityCollection:

    file = open(filepath)
    csv_file = csv.reader(file)
    header = next(csv_file)
    for i in range(0, len(header)):
        header[i] = header[i].replace(" ","")
    if not 'N' in header:
        raise TypeError('Specified input file does not have a "N" column. Required columns are: "N", "country", "city", "lat", "lon" in any order.')
    elif not 'country' in header:
        raise TypeError('Specified input file does not have a "country" column. Required columns are: "N", "country", "city", "lat", "lon" in any order.')
    elif not 'city' in header:
        raise TypeError('Specified input file does not have a "city" column. Required columns are: "N", "country", "city", "lat", "lon" in any order.')
    elif not 'lat' in header:
        raise TypeError('Specified input file does not have a "lat" column. Required columns are: "N", "country", "city", "lat", "lon" in any order.')
    elif not 'lon' in header:
        raise TypeError('Specified input file does not have a "lon" column. Required columns are: "N", "country", "city", "lat", "lon" in any order.')
    for i in range(0, len(header)):
        if header[i] == 'N':
            N = i
        elif header[i] == 'country':
            country = i
        elif header[i] == 'city':
            city = i
        elif header[i] == 'lat':
            lat = i
        elif header[i] == 'lon':
            lon = i

    cities_dict = {}
    city_list = []

    for row in csv_file:
        name = row[3]
        name = name.replace(" ","_")
        name = name.lower()

        # Create dictionary with city name as the key and value which corresponds to the index of city_list holding the City class for this city.
        cities_dict[name] = csv_file.line_num-2

        # Append class to list with for corresponding row in input csv. Dictionary has associated index for each city.
        # Usage: print(city_list[cities_dict["algiers"]])
        city_list.append(City(str(row[city]), str(row[country]), int(row[N]), float(row[lat]), float(row[lon])))

    # Create city collection class from list of city classes
    collection = CityCollection(city_list)

    return collection, cities_dict


