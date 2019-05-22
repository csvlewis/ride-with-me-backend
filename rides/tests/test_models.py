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
    assert rides == 11

def test_ride_object_returns_description(db, django_db_setup):
    ride = Ride.objects.get(pk=1)
    assert str(ride) == 'Looking for two passengers'
