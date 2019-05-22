
import pytest

from django.core.management import call_command

@pytest.fixture(scope='session')
def django_db_setup(django_db_setup, django_db_blocker):
    with django_db_blocker.unblock():
        call_command('loaddata', '../fixtures/city_data.json')
        call_command('loaddata', '../fixtures/user_data.json')
        call_command('loaddata', '../fixtures/ride_data.json')
        call_command('loaddata', '../fixtures/request_data.json')
        call_command('loaddata', '../fixtures/ridepassenger_data.json')
