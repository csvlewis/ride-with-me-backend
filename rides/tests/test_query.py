import graphene
import pytest
from rides.schema import Query
from rides.schema import Mutation
from graphene.test import Client
schema = graphene.Schema(Query, Mutation)

pytestmark = pytest.mark.django_db

def test_all_cities(snapshot):
    client = Client(schema)
    response = client.execute("query { allCities{name}}")
    snapshot.assert_match(response)

def test_find_ride_by_id(snapshot):
    client = Client(schema)
    response = client.execute("query { searchRideById(id:1){ id } }" )
    snapshot.assert_match(response)

def test_all_available_rides(snapshot):
    client = Client(schema)
    response = client.execute("query { availableRides{ id } }")
    snapshot.assert_match(response)

def test_create_new_ride(snapshot):
    client = Client(schema)
    response = client.execute('mutation { createRide(driverId:1 startCityId:1 endCityId:2 description:"Going for a ride" mileage:100 price:50.00 totalSeats:4 departureTime:"2019-05-23") { id } }')
    snapshot.assert_match(response)

def test_pending_requests(snapshot):
    client = Client(schema)
    response = client.execute("query { pendingRequests(driverId:1){ id message status } }")
    snapshot.assert_match(response)
