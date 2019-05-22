import graphene
from graphene_django import DjangoObjectType
from django.db.models.functions import Concat
from django.db.models import Value

from .models import City
from .models import Ride


class CityType(DjangoObjectType):
    name = graphene.String()

    class Meta:
        model = City

    def resolve_name(self, info):
        if self is not None:
            return '%s, %s' % (self.city, self.state)
        return ''

class RideType(DjangoObjectType):
    class Meta:
        model = Ride


class Query(graphene.ObjectType):
    all_cities = graphene.List(CityType)

    def resolve_all_cities(self, info, **kwargs):
        return City.objects.all()

    available_rides = graphene.List(RideType)

    def resolve_available_rides(self, info, **kwargs):
        return Ride.objects.filter(status='available')
