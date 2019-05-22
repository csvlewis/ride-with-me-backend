# import graphene
# from rides.schema import Query
# from graphene.test import Client
# schema = graphene.Schema(Query)
#
# def test_all_cities(snapshot):
#     client = Client(schema)
#     response = client.execute("query { allCities{id}}")
#     snapshot.assert_match(response)
