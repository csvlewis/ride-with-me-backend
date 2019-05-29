import pytest
from rides.models import City, Ride
from mixer.backend.django import mixer

pytestmark = pytest.mark.django_db

def test_returns_as_city_and_state():

    city = mixer.blend('rides.City', city='Denver', state='CO')
    assert str(city) == 'Denver, CO'

def test_can_count_cities(db, django_db_setup):
    cities = City.objects.count()
    assert cities == 50

def test_can_count_rides(db, django_db_setup):
    rides = Ride.objects.count()
    assert rides == 12

def test_ride_object_returns_description(db, django_db_setup):
    ride = Ride.objects.get(pk=1)
    assert str(ride) == "ID: 1, Description: I'm taking a trip to Golden this weekend, room for two passengers!"

def test_gets_rides_within_date_range(db, django_db_setup):
    mock_input_date = '2019-06-05'
    rides = Ride.objects.filter(departure_date__gte=mock_input_date)
    assert len(rides) == 8
