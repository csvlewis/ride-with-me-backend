import graphene
import pytest
from rides.schema import Query
from rides.schema import Mutation
from graphene.test import Client
schema = graphene.Schema(Query, Mutation)

pytestmark = pytest.mark.django_db

def test_all_cities(snapshot):
    client = Client(schema)
    response = client.execute("{ allCities { name } }")
    snapshot.assert_match(response)

def test_searchable_cities(snapshot):
    client = Client(schema)
    response = client.execute("{ searchableCities { id name } }")
    snapshot.assert_match(response)

def test_user_by_id(snapshot):
    client = Client(schema)
    response = client.execute("{ searchUserById(id: 1) { id firstName lastName email uuid createdAt updatedAt } }")
    snapshot.assert_match(response)

def test_ride_by_id(snapshot):
    client = Client(schema)
    response = client.execute('{ searchRideById(id: 1) { id } }')
    snapshot.assert_match(response)

def test_all_available_rides(snapshot):
    client = Client(schema)
    response = client.execute("{ availableRides { id } }")
    snapshot.assert_match(response)

def test_available_ride_search(snapshot):
    client = Client(schema)
    response = client.execute('{ searchRidesByCities(startCityId: 1, endCityId: 2, departureDate: "2019-05-22") { id } }')
    snapshot.assert_match(response)

def test_create_new_ride(snapshot):
    client = Client(schema)
    response = client.execute('mutation { createRide(driverUuid: "c96808f0-8195-11e9-93f6-88e9fe6e9b8e", startCityId: 3, endCityId: 4, description: "Test ride", price: 10.00, totalSeats: 1, departureDate: "2019-06-22") { ride { id travelTime description mileage} } }')
    snapshot.assert_match(response)

def test_change_ride_status(snapshot):
    client = Client(schema)
    response = client.execute('mutation { changeRideStatus(id: 1, status: "new_status") { ride { id status } } }')
    snapshot.assert_match(response)

def test_driver_pending_requests(snapshot):
    client = Client(schema)
    response = client.execute('{ pendingRequests(driverUuid: "c96808f0-8195-11e9-93f6-88e9fe6e9b8e") { id } }')
    snapshot.assert_match(response)

def test_create_request(snapshot):
    client = Client(schema)
    response = client.execute('mutation { createRequest(message: "Test message", passengerUuid: "c96808f0-8195-11e9-93f6-88e9fe6e9b8e", rideId: 5) { request { id message passenger { id } ride { id } } } }')
    snapshot.assert_match(response)

def test_change_request_status(snapshot):
    client = Client(schema)
    response = client.execute('mutation { changeRequestStatus(id: 1 status: "new_status"){ request { id status } } }')
    snapshot.assert_match(response)

def test_delete_ridepassenger(snapshot):
    client = Client(schema)
    response = client.execute('mutation { deleteRidePassenger(passengerUuid: "cbe2753e-8195-11e9-93f6-88e9fe6e9b8e", rideId:8){ ok message } }')
    snapshot.assert_match(response)

def test_add_ridepassenger(snapshot):
    client = Client(schema)
    response = client.execute('mutation { createRidePassenger(passengerId: 1, rideId: 6){ ok message } }')
    snapshot.assert_match(response)

def test_get_my_rides(snapshot):
    client = Client(schema)
    response = client.execute('{ myRides(userUuid: "c96808f0-8195-11e9-93f6-88e9fe6e9b8e") { id description } }')
    snapshot.assert_match(response)

def test_login_user(snapshot):
    client = Client(schema)
    response = client.execute('mutation { loginUser(email: "johnnydepp@gmail.com", firstName: "Johnny", lastName: "Depp", image_url:"https://d1nhio0ox7pgb.cloudfront.net/_img/o_collection_png/green_dark_grey/512x512/plain/user.png") { user { id firstName lastName email uuid } } }')
    snapshot.assert_match(response)

def test_register_user(snapshot):
    client = Client(schema)
    response = client.execute('mutation { loginUser(email: "newuser@gmail.com", firstName: "New", lastName: "User", image_url:"https://d1nhio0ox7pgb.cloudfront.net/_img/o_collection_png/green_dark_grey/512x512/plain/user.png") { user { id firstName lastName email uuid } } }')
    snapshot.assert_match(response)
