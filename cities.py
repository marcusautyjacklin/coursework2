from typing import Dict, List, Tuple
import math

class City:
    
    def __init__(self, city: str , country: str, attendees: int, latitude: float, longitude: float) -> None:

        if not isinstance(city, str):
            raise TypeError('Input {} for city is not a string'.format(city))

        if not isinstance(country, str):
            raise TypeError('Input {} for country is not a string'.format(country))

        if not isinstance(attendees, int):
            raise TypeError('Input {} for attendees is not an integer'.format(attendees))
        elif attendees < 0:
            raise ValueError('Input {} for attendees is negative'.format(attendees))

        if not isinstance(latitude, float):
            raise TypeError('Input {} for latitude is not a float'.format(latitude))
        elif not -90. <= latitude <= 90.:
            raise ValueError('Input {} for longitude is not within range -90 to 90 degrees'.format(latitude))

        if not isinstance(longitude, float):
            raise TypeError('Input {} for longitude is not a float'.format(longitude))
        elif not -180. <= longitude <= 180.:
            raise ValueError('Input {} for longitude is not within range -90 to 90 degrees'.format(longitude))

        self.city = city
        self.country = country
        self.attendees = attendees
        self.latitude = latitude
        self.longitude = longitude

    def __str__(self):
        return f"{self.__class__.__name__}(\n   City = {self.city},\n   Country = {self.country},\n   Attendees = {self.attendees},\n   Latitude = {self.latitude},\n   Longitude = {self.longitude}\n)"

    def distance_to(self, other: 'City') -> float:
        # Approx radius of the Earth in km:
        R = 6371
        # Calculate distance between two cities using the Haversine formula:
        d = 2*R*math.asin(math.sqrt((math.sin((other.latitude-self.latitude)/2)**2) + math.cos(self.latitude)*math.cos(other.latitude)*(math.sin((other.longitude-self.longitude)/2)**2)))
        # Return distance between two cities:
        return d

    def co2_to(self, other: 'City') -> float:
        # Approx radius of the Earth in km:
        R = 6371
        d = 2*R*math.asin(math.sqrt((math.sin((other.latitude-self.latitude)/2)**2) + math.cos(self.latitude)*math.cos(other.latitude)*(math.sin((other.longitude-self.longitude)/2)**2)))
        #          d < 1000km : 200kg CO2 / km / person
        # 1000km < d < 8000km : 250kg CO2 / km / person
        #          d > 8000km : 300kg CO2 / km / person
        if d <= 1000.:
            co2 = self.attendees * 200. * d
        elif d <= 8000.:
            co2 = self.attendees * (200. * 1000. + 250. * (d - 1000.))
        elif d > 8000.:
            co2 = self.attendees * (200. * 1000. + 250. * 7000. + 300. * (d-8000.))
        return co2


class CityCollection:
    
    def __init__(self, list_of_cities: list) -> None:

        if not isinstance(list_of_cities, list):
            raise TypeError('Input for list of cities is not a list')
        elif not list_of_cities:
            raise ValueError('Input list of cities is empty')

        self.cities = list_of_cities

    def countries(self) -> List[str]:
        countries_list = []
        # Iterate through all classes in self.cities:
        for i in range(0, len(self.cities)):
            # Check if the country of the City class is already in the list and if not, add it.
            if not self.cities[i].country in countries_list:
                countries_list.append(self.cities[i].country)
        return countries_list

    def total_attendees(self) -> int:
        total = 0.
        # Iterate through constituent City classes of CityCollection and sum their attendees.
        for i in range(0, len(self.cities)):
            total += self.cities[i].attendees
        return total


    def total_distance_travel_to(self, other: City) -> float:
        total_distance = 0.
        for i in range(0, len(self.cities)):
            total_distance += (self.cities[i].distance_to(other) * self.cities[i].attendees)
        return total_distance

    def travel_by_country(self, other: City) -> Dict[str, float]:
        travel_dist_dict = {}
        countries_list = self.countries()
        for i in range(0, len(countries_list)):
            travel_dist_dict[countries_list[i]] = 0.
            for j in range(0, len(self.cities)):
                if self.cities[j].country == countries_list[i]:
                    travel_dist_dict[countries_list[i]] += self.cities[j].distance_to(other) * self.cities[j].attendees
        return travel_dist_dict

    def total_co2(self, other: City) -> float:
        total_co2 = 0.
        for i in range(0, len(self.cities)):
            total_co2 += (self.cities[i].co2_to(other) * self.cities[i].attendees)
        return total_co2

    def co2_by_country(self, other: City) -> Dict[str, float]:
        travel_co2_dict = {}
        list_countries = self.countries()
        for i in range(0, len(list_countries)):
            travel_co2_dict[list_countries[i]] = 0.
            for j in range(0, len(self.cities)):
                if self.cities[j].country == list_countries[i]:
                    travel_co2_dict[list_countries[i]] += self.cities[j].co2_to(other) * self.cities[j].attendees
        return travel_co2_dict


    def summary(self, city: City):
        raise NotImplementedError

    def sorted_by_emissions(self) -> List[Tuple[str, float]]:
        raise NotImplementedError

    def plot_top_emitters(self, city: City, n: int, save: bool):
        raise NotImplementedError
