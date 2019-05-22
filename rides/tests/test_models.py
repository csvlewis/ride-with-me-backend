import pytest
from rides.models import City
from mixer.backend.django import mixer

pytestmark = pytest.mark.django_db

def test_returns_as_city_and_state():

    city = mixer.blend('rides.City', city='Denver', state='CO')
    assert str(city) == 'Denver, CO'
