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

## Read file test ##

def test_Read_attendees_file():
    raise NotImplementedError


## City class tests ##

def test_City_constructor_invalid_input_city(testClasses):
    with pytest.raises(TypeError) as exception:
        test = City(1, 'test', 0, 0., 0.)

def test_City_constructor_invalid_input_country(testClasses):
    with pytest.raises(TypeError) as exception:
        test = City('test', 1 , 0, 0., 0.)

def test_City_constructor_invalid_input_attendees(testClasses):
    with pytest.raises(TypeError) as exception:
        test = City('test', 'test', 0., 0., 0.)

def test_City_constructor_invalid_input_lat(testClasses):
    with pytest.raises(TypeError) as exception:
        test = City('test', 'test', 0, 'test', 0.)
    with pytest.raises(ValueError) as exception:
        test = City('test', 'test', 0, 300., 0.)

def test_City_constructor_invalid_input_lon(testClasses):
    with pytest.raises(TypeError) as exception:
        test = City('test', 'test', 0, 0., 'test')
    with pytest.raises(ValueError) as exception:
        test = City('test', 'test', 0, 0., 300.)

def test_City_distance_to_publicTransport_invalid_input(testClasses):
    with pytest.raises(TypeError) as exception:
        london = testClasses[0]
        london.distance_to('test')

def test_City_distance_to_shortHaul_invalid_input(testClasses):
    with pytest.raises(TypeError) as exception:
        london = testClasses[0]
        london.distance_to('test')

def test_City_distance_to_longHaul_invalid_input(testClasses):
    with pytest.raises(TypeError) as exception:
        london = testClasses[0]
        london.distance_to('test')

def test_City_co2_to_publicTransport_invalid_input(testClasses):
    with pytest.raises(TypeError) as exception:
        london = testClasses[0]
        london.co2_to('test')

def test_City_co2_to_shortHaul_invalid_input(testClasses):
    with pytest.raises(TypeError) as exception:
        london = testClasses[0]
        london.co2_to('test')

def test_City_co2_to_longHaul_invalid_input(testClasses):
    with pytest.raises(TypeError) as exception:
        london = testClasses[0]
        london.co2_to('test')

def test_City_distance_to_publicTransport(testClasses):
    london = testClasses[0]
    paris = testClasses[1]
    assert london.distance_to(paris) == 343.51651914890107

def test_City_distance_to_shortHaul(testClasses):
    toronto = testClasses[2]
    los_angeles = testClasses[3]
    assert toronto.distance_to(los_angeles) == 3493.908413422292

def test_City_distance_to_longHaul(testClasses):
    beijing = testClasses[4]
    san_francisco = testClasses[5]
    assert beijing.distance_to(san_francisco) == 9503.485826688868

def test_City_co2_to_publicTransport(testClasses):
    london = testClasses[0]
    paris =  testClasses[1]
    assert london.co2_to(paris) == 8038.286548084285

def test_City_co2_to_shortHaul(testClasses):
    toronto = testClasses[2]
    los_angeles = testClasses[3]
    assert toronto.co2_to(los_angeles) == 73289.462198646

def test_City_co2_to_longHaul(testClasses):
    beijing = testClasses[4]
    san_francisco = testClasses[5]
    assert beijing.co2_to(san_francisco) == 2280993.4606063277

## CityCollection class tests ##

def test_CityCollection_constructor_invalid_input(testClasses):
    london = testClasses[0]
    with pytest.raises(TypeError) as exception:
        test = CityCollection([london, 'test'])
    with pytest.raises(ValueError) as exception:
        test = CityCollection([])
    with pytest.raises(TypeError) as exception:
        test = CityCollection('test')

# Info about collection #  

def test_CityCollection_countries(testClasses):
    city_collection = testClasses[10]
    countries = city_collection.countries()
    assert len(countries) == 8
    if not isinstance(countries, list):
        raise TypeError('CityCollection.countries() method output is not a list.')
    if not len(city_collection.countries()) == len(set(city_collection.countries())):
        raise ValueError('CityCollection.countries() method produces list with duplicate countries.')

def test_CityCollection_total_attendees(testClasses):
    city_collection = testClasses[10]
    attendees = city_collection.total_attendees()
    assert attendees == 1853
    if not isinstance(attendees, int):
        raise TypeError('CityCollection.total_attendees() method output is not an integer')

# Info specifc to host-city # 
def test_CityCollection_total_distance_invalid_input(testClasses):
    with pytest.raises(TypeError) as exception:
        city_collection = testClasses[10]
        city_collection.total_distance_travel_to('test')

def test_CityCollection_travel_by_country_invalid_input(testClasses):
    with pytest.raises(TypeError) as exception:
        city_collection = testClasses[10]
        city_collection.travel_by_country('test')

def tets_CityCollection_co2_by_country_invalid_input(testClasses):
    with pytest.raises(TypeError) as exception:
        city_collection = testClasses[10]
        city_collection.co2_by_country('test')

def test_CityCollection_total_co2_invalid_input(testClasses):
    with pytest.raises(TypeError) as exception:
        city_collection = testClasses[10]
        city_collection.total_co2('test')

def test_CityCollection_total_distance(testClasses):
    london = testClasses[0]
    paris = testClasses[1]
    toronto = testClasses[2]
    collection = CityCollection([london,paris,toronto])
    test = collection.total_distance_travel_to(paris)
    if not isinstance(test, float):
        raise TypeError('Output of method should be a float.')
    assert test == 574273.4912686805

def test_CityCollection_travel_by_country(testClasses):
    london = testClasses[0]
    paris = testClasses[1]
    toronto = testClasses[2]
    collection = CityCollection([london,paris,toronto])
    test = collection.travel_by_country(paris)
    if not isinstance(test, dict):
        raise TypeError('Output of method should be a dictionary.')
    if not isinstance(list(test.items())[0][0], str):
        raise TypeError('Output dictionary should have keys of tyoe: string.')
    if not isinstance(list(test.items())[0][1], float):
        raise TypeError('Output dictionary should have keys of tyoe: float.')
    assert test == {'United Kingdom': 40191.43274042143, 'France': 0., 'Canada': 534082.0585282592}

def test_CityCollection_co2_by_country(testClasses):
    london = testClasses[0]
    paris = testClasses[1]
    toronto = testClasses[2]
    collection = CityCollection([london,paris,toronto])
    test = collection.co2_by_country(paris)
    if not isinstance(test, dict):
        raise TypeError('Output of method should be a dictionary.')
    if not isinstance(list(test.items())[0][0], str):
        raise TypeError('Output dictionary should have keys of tyoe: string.')
    if not isinstance(list(test.items())[0][1], float):
        raise TypeError('Output dictionary should have keys of tyoe: float.')
    assert test == {'United Kingdom': 8038.286548084285, 'France': 0., 'Canada': 129070.5146320648}

def test_CityCollection_total_co2(testClasses):
    london = testClasses[0]
    paris = testClasses[1]
    toronto = testClasses[2]
    collection = CityCollection([london,paris,toronto])
    test = collection.total_co2(paris)
    if not isinstance(test, float):
        raise TypeError('Output of method should be a float.')
    assert test == 137108.80118014908

def test_CityCollection_sorted_by_emissions(testClasses):
    collection = testClasses[10]
    test = collection.sorted_by_emissions()
    if not isinstance(test, list):
        raise TypeError('Output of method should be a list.')
    for i in range(1, len(test)):
        assert test[i-1][1] < test[i][1]
    assert len(test) == len(collection.cities), 'Cities in CityCollection object are missing from the sorted list of emissions.'
