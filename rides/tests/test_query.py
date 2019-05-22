import graphene
import pytest
from rides.schema import Query
from graphene.test import Client
schema = graphene.Schema(Query)

pytestmark = pytest.mark.django_db

def test_all_cities(snapshot):
    client = Client(schema)
    response = client.execute("query { allCities{name}}")
    snapshot.assert_match(response)

def test_all_available_rides(snapshot):
    client = Client(schema)
    response = client.execute("query { availableRides{id}}")
    snapshot.assert_match(response)
