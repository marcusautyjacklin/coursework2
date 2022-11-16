from typing import Dict, List, Tuple
import math
import matplotlib.pyplot as plt
import pytest

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
        if not isinstance(other, City):
            raise TypeError('Input is not a City object. City object is required for this method.')
        # Approx radius of the Earth in km:
        R = 6371
        # Calculate distance between two cities using the Haversine formula:
        phi1 = (self.latitude*(math.pi/180))
        lambda1 = (self.longitude*(math.pi/180))
        phi2 = (other.latitude*(math.pi/180))
        lambda2 = (other.longitude*(math.pi/180))

        d = 2*R*math.asin(math.sqrt(((math.sin((phi2-phi1)/2))**2) + (math.cos(phi1))*(math.cos(phi2))*((math.sin(((lambda2)-(lambda1))/2))**2)))
        # Return distance between two cities:
        return d

    def co2_to(self, other: 'City') -> float:
        if not isinstance(other, City):
            raise TypeError('Input is not a City object. City object is required for this method.')
        d = self.distance_to(other)
        ## Old interpretation of how this function should operate: ##

        #          d < 1000km : 200kg CO2 / km / person
        # 1000km < d < 8000km : 250kg CO2 / km / person
        #          d > 8000km : 300kg CO2 / km / persom
        # if d <= 1000.:
        #     co2 = self.attendees * 200. * d
        # elif d <= 8000.:
        #     co2 = self.attendees * ((200. * 1000.) + (250. * (d - 1000.)))
        # elif d > 8000.:
        #     co2 = self.attendees * ((200. * 1000.) + (250. * 7000.) + (300. * (d-8000.)))

        ## New interpretation of how this function should operate as per Submitty errors: ##
        
        if d <= 1000.:
            co2 = self.attendees * 200. * d
        elif 1000. < d <= 8000.:
            co2 = self.attendees * 250. * d
        elif d > 8000.:
            co2 = self.attendees * 300. * d
        return co2


class CityCollection:
    
    def __init__(self, list_of_cities: list) -> None:
        
        if not isinstance(list_of_cities, list):
            raise TypeError('Input for list of cities is not a list')
        elif not list_of_cities:
            raise ValueError('Input list of cities is empty')
        else:
            for i in range(0,len(list_of_cities)):
                        if not isinstance(list_of_cities[i], City):
                            raise TypeError('Input list contains elements which are not City objects. All elements in list must be City objects.')
        self.city_list = list_of_cities

    def countries(self) -> List[str]:
        countries_list = []
        # Iterate through all classes in self.city_list:
        for i in range(0, len(self.city_list)):
            # Check if city has any attendees, only add to list if there is more than zero.
            if self.city_list[i].attendees > 0:
            # Check if the country of the City class is already in the list and if not, add it.
                if not self.city_list[i].country in countries_list:
                    countries_list.append(self.city_list[i].country)
        return countries_list

    def total_attendees(self) -> int:
        total = 0.
        # Iterate through constituent City classes of CityCollection and sum their attendees.
        for i in range(0, len(self.city_list)):
            total += self.city_list[i].attendees
        total = int(total)
        return total


    def total_distance_travel_to(self, other: City) -> float:
        if not isinstance(other, City):
            raise TypeError('Input is not a City object. City object is required for this method.')
        total_distance = 0.
        for i in range(0, len(self.city_list)):
            total_distance += (self.city_list[i].distance_to(other) * self.city_list[i].attendees)
        return total_distance

    def travel_by_country(self, other: City) -> Dict[str, float]:
        if not isinstance(other, City):
            raise TypeError('Input is not a City object. City object is required for this method.')
        travel_dist_dict = {}
        countries_list = self.countries()
        for i in range(0, len(countries_list)):
            travel_dist_dict[countries_list[i]] = 0.
            for j in range(0, len(self.city_list)):
                if self.city_list[j].country == countries_list[i]:
                    travel_dist_dict[countries_list[i]] += self.city_list[j].distance_to(other) * self.city_list[j].attendees
        return travel_dist_dict

    def total_co2(self, other: City) -> float:
        if not isinstance(other, City):
            raise TypeError('Input is not a City object. City object is required for this method.')
        total_co2 = 0.
        for i in range(0, len(self.city_list)):
            total_co2 += (self.city_list[i].co2_to(other))
        return total_co2

    def co2_by_country(self, other: City) -> Dict[str, float]:
        if not isinstance(other, City):
            raise TypeError('Input is not a City object. City object is required for this method.')
        travel_co2_dict = {}
        list_countries = self.countries()
        for i in range(0, len(list_countries)):
            travel_co2_dict[list_countries[i]] = 0.
            for j in range(0, len(self.city_list)):
                if self.city_list[j].country == list_countries[i]:
                    travel_co2_dict[list_countries[i]] += self.city_list[j].co2_to(other)
        return travel_co2_dict


    def summary(self, other: City):
        if not isinstance(other, City):
            raise TypeError('Input is not a City object. City object is required for this method.')
        co2_tonnes = round(self.total_co2(other)/1000)
        return print("Host city: ",other.city," (",other.country,")\nTotal CO2: ",co2_tonnes," tonnes\nTotal attendees travelling to ",other.city," from ",len(self.city_list)," different cities: ",self.total_attendees(),sep="")    
    
    def sorted_by_emissions(self) -> List[Tuple[str, float]]:
        emissions = []
        for i in range(0, len(self.city_list)):
            emissions.append((self.city_list[i].city, self.total_co2(self.city_list[i])))
        emissions = sorted(emissions,key=lambda x: (x[1]))
        return emissions

    def plot_top_emitters(self, other: City, n=10, save=False):
        if not isinstance(other, City):
            raise TypeError('Input is not a City object. City object is required for this method.')
        emissions = list(self.co2_by_country(other).items())
        emissions = sorted(emissions, key=lambda x : x[1], reverse=True)
        emissions_other = emissions[n:]
        emissions = emissions[0:n]
        temp = ['Other', 0]
        for i in range(0, len(emissions_other)):
            temp[1] += emissions_other[i][1]
        emissions.append(temp)
        emissions_labels = []
        emissions_values = []
        for i in range(0, len(emissions)):
            emissions_labels.append(emissions[i][0])
            emissions_values.append(emissions[i][1])
        fig = plt.figure(figsize=(6,4), dpi = 200)
        fig.set_tight_layout(True)
        plt.tight_layout()
        plt.bar(emissions_labels, emissions_values)
        plt.xlabel("City")
        plt.xticks(fontsize=6, rotation = 90)
        plt.yticks(fontsize=6)
        plt.ylabel("CO2 emissions (tonnes)")
        plt.yscale("log")
        plt.show(block=False)
        if save == True:
            filename = other.city
            filename = filename.replace(" ","_")
            filename = filename.lower()
            plt.savefig(filename)

        

