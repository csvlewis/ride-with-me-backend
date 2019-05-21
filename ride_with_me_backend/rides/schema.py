import graphene
from graphene_django import DjangoObjectType

from .models import City


class CityType(DjangoObjectType):
    class Meta:
        model = City


class Query(graphene.ObjectType):
    cities = graphene.List(CityType)

    def resolve_cities(self, info, **kwargs):
        return City.objects.all()
