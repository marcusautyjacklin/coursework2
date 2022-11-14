from typing import Dict, List, Tuple

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
        return 'City: '+ str(self.city) + '\nCountry: '+ str(self.country) + '\nAttendees: '+ str(self.attendees) + '\nCoordinates: '+ str(self.latitude)+', ' + str(self.longitude)
        raise NotImplementedError

    def distance_to(self, other: 'City') -> float:
        raise NotImplementedError

    def co2_to(self, other: 'City') -> float:
        raise NotImplementedError


class CityCollection:
    
    def __init__(self, list_of_cities: list) -> None:

        if not isinstance(list_of_cities, list):
            raise TypeError('Input for list of cities is not a list')
        elif not list_of_cities:
            raise ValueError('Input list of cities is empty')

        self.cities = list_of_cities

    def countries(self) -> List[str]:
        raise NotImplementedError

    def total_attendees(self) -> int:
        raise NotImplementedError

    def total_distance_travel_to(self, city: City) -> float:
        raise NotImplementedError

    def travel_by_country(self, city: City) -> Dict[str, float]:
        raise NotImplementedError

    def total_co2(self, city: City) -> float:
        raise NotImplementedError

    def co2_by_country(self, city: City) -> Dict[str, float]:
        raise NotImplementedError

    def summary(self, city: City):
        raise NotImplementedError

    def sorted_by_emissions(self) -> List[Tuple[str, float]]:
        raise NotImplementedError

    def plot_top_emitters(self, city: City, n: int, save: bool):
        raise NotImplementedError
