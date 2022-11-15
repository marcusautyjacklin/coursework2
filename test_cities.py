import pytest
from utils import read_attendees_file
from cities import City, CityCollection
from pathlib import Path
import csv

@pytest.fixture
def testClasses():
    london = City('London', 'United Kingdom', 117, 51.5073219, -0.1276474)
    paris = City('Paris', 'France', 173, 48.8566101, 2.3514992)
    toronto = City('Toronto', 'Canada', 89,43.653963, -79.387207)
    los_angeles = City('Los Angeles', 'United States', 298, 34.0536909, -118.2427666)
    beijing = City('Beijing', 'China', 950, 39.906217, 116.3912757)
    san_francisco = City('San Francisco', 'United States', 64, 37.7792808, -122.4192363)
    zurich = City('Zurich', 'Switzerland', 52, 47.22, 8.33)
    algiers = City('Algiers', 'Algeria', 1, 28.0000272,	2.9999825)
    canberra = City('Canberra','Australia', 54, -35.2975906, 149.1012676)
    oxford = City('Oxford', 'United Kingdom', 55, 51.7520131, -1.2578499)

    city_collection = CityCollection([zurich, san_francisco, algiers, canberra, london, paris, toronto, beijing, los_angeles, oxford])

    return london, paris, toronto, los_angeles, beijing, san_francisco, zurich, algiers, canberra, oxford, city_collection 

## City class tests ##

def test_publicTransport_travel(testClasses):
    london = testClasses[0]
    paris = testClasses[1]
    # assert round(london.distance_to(paris),2) == 343.52
    assert london.distance_to(paris) == 343.51651914890107

    # assert round(city_collection.cities[cities_dict["london"]].distance_to(city_collection.cities[cities_dict["paris"]]),2) == 343.52
    # raise NotImplementedError

def test_shortHaul_travel(testClasses):
    toronto = testClasses[2]
    los_angeles = testClasses[3]
    # assert round(toronto.distance_to(los_angeles),2) == 3493.91
    assert toronto.distance_to(los_angeles) == 3493.908413422292

    # assert round(city_collection.cities[cities_dict["toronto"]].distance_to(city_collection.cities[cities_dict["los_angeles"]]),2) == 3493.91
    # raise NotImplementedError

def test_longHaul_travel(testClasses):
    beijing = testClasses[4]
    san_francisco = testClasses[5]
    # assert round(beijing.distance_to(san_francisco),2) == 9503.49
    assert beijing.distance_to(san_francisco) == 9503.485826688868

    # assert round(city_collection.cities[cities_dict["beijing"]].distance_to(city_collection.cities[cities_dict["san_francisco"]]),2) == 9503.49
    # raise NotImplementedError

def test_publicTransport_co2(testClasses):
    london = testClasses[0]
    paris =  testClasses[1]
    # assert round(london.co2_to(paris),2) == 8038.29
    assert london.co2_to(paris) == 8038.286548084285

    # raise NotImplementedError

def test_shortHaul_co2(testClasses):
    toronto = testClasses[2]
    los_angeles = testClasses[3]
    # assert round(toronto.co2_to(los_angeles),2) == 73289.46
    assert toronto.co2_to(los_angeles) == 73289.462198646

    # raise NotImplementedError

def test_longHaul_co2(testClasses):
    beijing = testClasses[4]
    san_francisco = testClasses[5]
    # assert round(beijing.co2_to(san_francisco),2) == 2280993.46
    assert beijing.co2_to(san_francisco) == 2280993.4606063277

    # raise NotImplementedError

## CityCollection class tests ##

# Info about collection #  

def test_countries():
    raise NotImplementedError

def test_attendees():
    raise NotImplementedError

# Info specifc to host-city # 

def test_total_distance():
    raise NotImplementedError

def test_travel_byCountry():
    raise NotImplementedError

def tets_co2_byCountry():
    raise NotImplementedError

def test_total_co2():
    raise NotImplementedError

def test_sortedByEmissions():
    raise NotImplementedError
