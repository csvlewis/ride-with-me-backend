import graphene
from graphene_django import DjangoObjectType
from django.db.models.functions import Concat
from django.db.models import Value

from .models import City
from .models import Ride
from .models import User
from .models import Request
from .models import RidePassenger

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

class UserType(DjangoObjectType):
    class Meta:
        model = User

class RideType(DjangoObjectType):
    class Meta:
        model = Ride

class RidePassengerType(DjangoObjectType):
    class Meta:
        model = RidePassenger

class CreateRide(graphene.Mutation):
    id = graphene.Int()
    driver_id = graphene.Int()
    start_city_id = graphene.Int()
    end_city_id = graphene.Int()
    description = graphene.String()
    mileage = graphene.Int()
    price = graphene.Float()
    total_seats = graphene.Int()
    departure_time = graphene.types.datetime.Date()
    status = graphene.String()
    created_at = graphene.types.datetime.DateTime()
    updated_at = graphene.types.datetime.DateTime()

    class Arguments:
        driver_id = graphene.Int()
        start_city_id = graphene.Int()
        end_city_id = graphene.Int()
        description = graphene.String()
        mileage = graphene.Int()
        price = graphene.Float()
        total_seats = graphene.Int()
        departure_time = graphene.types.datetime.Date()

    def mutate(self, info, driver_id, start_city_id, end_city_id, description, mileage, price, total_seats, departure_time):
        ride = Ride(driver_id=driver_id, start_city_id=start_city_id, end_city_id=end_city_id, description=description, mileage=mileage, price=price, total_seats=total_seats, departure_time=departure_time, status='available')
        ride.save()

        return CreateRide(
            id=ride.id,
            driver_id=ride.driver_id,
            start_city_id=ride.start_city_id,
            end_city_id=ride.end_city_id,
            description=ride.description,
            mileage=ride.mileage,
            price=ride.price,
            total_seats=ride.total_seats,
            departure_time=ride.departure_time,
            status=ride.status,
            created_at=ride.created_at,
            updated_at=ride.updated_at
        )
class Query(graphene.ObjectType):
    all_cities = graphene.List(CityType)
    available_rides = graphene.List(RideType)
    search_ride_by_id = graphene.List(RideType, id = graphene.Int())

    search_rides_by_cities = graphene.List(RideType, start_city_id = graphene.Int(), end_city_id = graphene.Int(), departure_time = graphene.types.datetime.Date())

    def resolve_all_cities(self, info, **kwargs):
        return City.objects.all()

    def resolve_available_rides(self, info, **kwargs):
        return Ride.objects.filter(status='available')


    def resolve_search_ride_by_id(self, info, id):
        return Ride.objects.filter(id = id)

    def resolve_search_rides_by_cities(self, info, start_city_id, end_city_id, departure_time = None):

        if departure_time and Ride.objects.filter(status='available', start_city_id = start_city_id, end_city_id = end_city_id, departure_time__gte = departure_time):
            return Ride.objects.filter(status = 'available', start_city_id = start_city_id, end_city_id = end_city_id, departure_time__gte = departure_time).order_by('departure_time')

        else:
            return Ride.objects.filter(status = 'available', start_city_id = start_city_id, end_city_id = end_city_id).order_by('departure_time')

class Mutation(graphene.ObjectType):
    create_ride = CreateRide.Field()
