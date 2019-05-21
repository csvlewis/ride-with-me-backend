import graphene
from graphene_django import DjangoObjectType
from django.db.models.functions import Concat
from django.db.models import Value

from .models import City


class CityType(DjangoObjectType):
    name = graphene.String()

    class Meta:
        model = City

    def resolve_name(self, info):
        if self is not None:
            return '%s, %s' % (self.city, self.state)
        return ''


class Query(graphene.ObjectType):
    all_cities = graphene.List(CityType)

    def resolve_all_cities(self, info, **kwargs):
        return City.objects.all()
