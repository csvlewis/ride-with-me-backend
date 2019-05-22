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
    available_rides = graphene.List(RideType)
    search_by_cities = graphene.List(RideType, start_city_id = graphene.Int(), end_city_id = graphene.Int())

    def resolve_all_cities(self, info, **kwargs):
        return City.objects.all()

    def resolve_available_rides(self, info, **kwargs):
        return Ride.objects.filter(status='available')

    def resolve_search_by_cities(self, info, start_city_id, end_city_id):
        return Ride.objects.filter(status='available', start_city_id = start_city_id, end_city_id = end_city_id)
