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
    zurich = City('Zurich', 'Switzerland', 109, 47.3723941, 8.5423328)
    algiers = City('Algiers', 'Algeria', 1, 28.0000272,	2.9999825)
    canberra = City('Canberra','Australia', 54, -35.2975906, 149.1012676)
    oxford = City('Oxford', 'United Kingdom', 55, 51.7520131, -1.2578499)
    city_collection = CityCollection([zurich, san_francisco, algiers, canberra, london, paris, toronto, beijing, los_angeles, oxford])
    return london, paris, toronto, los_angeles, beijing, san_francisco, zurich, algiers, canberra, oxford, city_collection 

@pytest.fixture
def testFile():
    filepath = Path('test_attendee_locations.csv')
    return filepath
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
    assert london.distance_to(paris) == pytest.approx(343.51651914890107)

def test_City_distance_to_shortHaul(testClasses):
    toronto = testClasses[2]
    los_angeles = testClasses[3]
    assert toronto.distance_to(los_angeles) == pytest.approx(3493.908413422292)

def test_City_distance_to_longHaul(testClasses):
    beijing = testClasses[4]
    san_francisco = testClasses[5]
    assert beijing.distance_to(san_francisco) == pytest.approx(9503.485826688868)

def test_City_co2_to_publicTransport(testClasses):
    london = testClasses[0]
    paris =  testClasses[1]
    assert london.co2_to(paris) == pytest.approx(8038286.548084285)

def test_City_co2_to_shortHaul(testClasses):
    toronto = testClasses[2]
    los_angeles = testClasses[3]
    assert toronto.co2_to(los_angeles) == pytest.approx(77739462.198646)

def test_City_co2_to_longHaul(testClasses):
    beijing = testClasses[4]
    san_francisco = testClasses[5]
    assert beijing.co2_to(san_francisco) == pytest.approx(2708493460.6063275)

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
    elif not len(city_collection.countries()) == len(set(city_collection.countries())):
        raise ValueError('CityCollection.countries() method produces list with duplicate countries.')

def test_CityCollection_total_attendees(testClasses):
    city_collection = testClasses[10]
    attendees = city_collection.total_attendees()
    assert attendees == 1910
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
    assert test == pytest.approx(574273.4912686805)

def test_CityCollection_travel_by_country(testClasses):
    london = testClasses[0]
    paris = testClasses[1]
    toronto = testClasses[2]
    collection = CityCollection([london,paris,toronto])
    test = collection.travel_by_country(paris)
    if not isinstance(test, dict):
        raise TypeError('Output of method should be a dictionary.')
    elif not isinstance(list(test.items())[0][0], str):
        raise TypeError('Output dictionary should have keys of tyoe: string.')
    elif not isinstance(list(test.items())[0][1], float):
        raise TypeError('Output dictionary should have keys of tyoe: float.')
    assert test['United Kingdom'] == pytest.approx(40191.43274042143)
    assert test['France'] == pytest.approx(0.)
    assert test['Canada'] == pytest.approx(534082.0585282592)

def test_CityCollection_co2_by_country(testClasses):
    london = testClasses[0]
    paris = testClasses[1]
    toronto = testClasses[2]
    collection = CityCollection([london,paris,toronto])
    test = collection.co2_by_country(paris)
    if not isinstance(test, dict):
        raise TypeError('Output of method should be a dictionary.')
    elif not isinstance(list(test.items())[0][0], str):
        raise TypeError('Output dictionary should have keys of type: string.')
    elif not isinstance(list(test.items())[0][1], float):
        raise TypeError('Output dictionary should have keys of type: float.')
    assert test['United Kingdom'] == pytest.approx(8038286.548084285)
    assert test['France'] == pytest.approx(0.0)
    assert test['Canada'] == pytest.approx(133520514.6320648)

def test_CityCollection_total_co2(testClasses):
    london = testClasses[0]
    paris = testClasses[1]
    toronto = testClasses[2]
    collection = CityCollection([london,paris,toronto])
    test = collection.total_co2(paris)
    if not isinstance(test, float):
        raise TypeError('Output of method should be a float.')
    assert test == pytest.approx(141558801.18014908)

def test_CityCollection_sorted_by_emissions(testClasses):
    collection = testClasses[10]
    test = collection.sorted_by_emissions()
    if not isinstance(test, list):
        raise TypeError('Output of method should be a list.')
    elif not isinstance(test[0], tuple):
        raise TypeError('Output of method should be a list with tuple elements')
    for i in range(1, len(test)):
        assert test[i-1][1] < test[i][1]
    assert len(test) == len(collection.city_list), 'city_list in CityCollection object are missing from the sorted list of emissions.'

def test_CityCollection_summary(testClasses):
    test = testClasses[10]
    with pytest.raises(TypeError) as exception:
        test.summary('London')

def test_read_attendees_file(testFile):
    filepath = testFile
    test = read_attendees_file(filepath)
    if not isinstance(test, CityCollection):
        raise TypeError('Output from read_attendees_file should be a dictionary and a list.')