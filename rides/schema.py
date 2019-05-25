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

class RequestType(DjangoObjectType):
    class Meta:
        model = Request

class RidePassengerType(DjangoObjectType):
    class Meta:
        model = RidePassenger

class CreateRide(graphene.Mutation):
    ride = graphene.Field(RideType)

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

        return CreateRide(ride=ride)

class UpdateRide(graphene.Mutation):
    ride = graphene.Field(RideType)

    class Arguments:
        id = graphene.Int()
        status = graphene.String()

    def mutate(self, info, id, status):
        ride = Ride.objects.filter(id = id)[0]
        setattr(ride, 'status', status)
        ride.save()
        return UpdateRide(ride)

class UpdateRequest(graphene.Mutation):
    request = graphene.Field(RequestType)

    class Arguments:
        id = graphene.Int()
        status = graphene.String()

    def mutate(self, info, id, status):
        request = Request.objects.filter(id = id)[0]
        setattr(request, 'status', status)
        request.save()
        return UpdateRequest(request)

class Query(graphene.ObjectType):
    all_cities = graphene.List(CityType)
    available_rides = graphene.List(RideType)
    search_ride_by_id = graphene.List(RideType, id = graphene.Int())
    search_rides_by_cities = graphene.List(RideType, start_city_id = graphene.Int(), end_city_id = graphene.Int(), departure_time = graphene.types.datetime.Date())
    pending_requests = graphene.List(RequestType, driver_id = graphene.Int())

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

    def resolve_pending_requests(self, info, driver_id):
        return Request.objects.filter(driver_id = driver_id, status = 'pending')

class Mutation(graphene.ObjectType):
    create_ride = CreateRide.Field()
    change_ride_status = UpdateRide.Field()
    change_request_status = UpdateRequest.Field()
