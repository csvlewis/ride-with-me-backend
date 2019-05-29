import graphene
import uuid
from graphene_django import DjangoObjectType
from django.db.models.functions import Concat
from django.db.models import Count
from django.db.models import Value
from django.db.models import Q
import requests
from envparse import env
env.read_envfile()

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
    available_seats = graphene.Int()
    class Meta:
        model = Ride

    def resolve_available_seats(self, info):
        if self is not None:
            rides = Ride.objects.filter(id=self.id).annotate(num_passengers=Count('ridepassenger'))
            available_seats = self.total_seats - rides[0].num_passengers
            return available_seats
        return ''

class UserType(DjangoObjectType):
    class Meta:
        model = User

class RequestType(DjangoObjectType):
    class Meta:
        model = Request

class RidePassengerType(DjangoObjectType):
    class Meta:
        model = RidePassenger

class LoginUser(graphene.Mutation):
    user = graphene.Field(UserType)

    class Arguments:
        first_name = graphene.String()
        last_name = graphene.String()
        email = graphene.String()

    def mutate(self, info, first_name, last_name, email):
        user = User.objects.filter(email=email)
        generated_uuid = uuid.uuid1()
        if user.count() == 0:
            user = User.objects.create(
                first_name  = first_name,
                last_name  = last_name,
                email  = email,
                uuid  = generated_uuid
            )
        else:
            user = user[0]
        return LoginUser(user=user)

class CreateRide(graphene.Mutation):
    ride = graphene.Field(RideType)

    class Arguments:
        driver_uuid = graphene.String()
        start_city_id = graphene.Int()
        end_city_id = graphene.Int()
        description = graphene.String()
        mileage = graphene.Int()
        price = graphene.Float()
        total_seats = graphene.Int()
        departure_date = graphene.types.datetime.Date()

    def mutate(self, info, driver_uuid, start_city_id, end_city_id, description, price, total_seats, departure_date):
        start_city = City.objects.get(pk=start_city_id)
        end_city = City.objects.get(pk=end_city_id)
        request = requests.get('https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial&origins=%s+%s&destinations=%s+%s&key=%s' % (str(start_city.city), str(start_city.state), str(end_city.city), str(end_city.state), env.str('GOOGLE_MAPS_API_KEY')))
        response = request.json()
        mileage = int(round(response["rows"][0]["elements"][0]["distance"]["value"] * 0.00062137))
        travel_time = response["rows"][0]["elements"][0]["duration"]["text"]

        driver = User.objects.filter(uuid = driver_uuid)
        if driver[0].uuid == driver_uuid:
            ride = Ride(
                        driver_id=driver[0].id,
                        start_city_id=start_city_id,
                        end_city_id=end_city_id,
                        description=description,
                        mileage=mileage,
                        travel_time=travel_time,
                        price=price,
                        total_seats=total_seats,
                        departure_date=departure_date,
                        status='available')
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

class CreateRequest(graphene.Mutation):
    request = graphene.Field(RequestType)

    class Arguments:
        message = graphene.String()
        passenger_uuid = graphene.String()
        ride_id = graphene.Int()

    def mutate(self, info, message, passenger_uuid, ride_id):
        ride = Ride.objects.get(pk=ride_id)
        passenger = User.objects.filter(uuid = passenger_uuid)
        if passenger[0].uuid == passenger_uuid:
            request = Request(
                driver_id = ride.driver_id,
                message = message,
                passenger_id = passenger[0].id,
                ride_id = ride_id
            )
            request.save()

        return CreateRequest(request=request)

class CreateRidePassenger(graphene.Mutation):
    ok = graphene.Boolean()
    message = graphene.String()

    class Arguments:
        passenger_id = graphene.Int()
        ride_id = graphene.Int()

    def mutate(self, info, passenger_id, ride_id):
        ride_query = Ride.objects.filter(id = ride_id)
        passenger_query = RidePassenger.objects.filter(ride_id = ride_id)
        request_query = Request.objects.filter(ride_id = ride_id, passenger_id = passenger_id)
        ride = ride_query[0]
        available_seats = ride.total_seats - passenger_query.count()
        if available_seats == 0:
            ok = False
            message = "The ride with id %s is already full" % (ride_id)
        else:
            ride_passenger = RidePassenger(
                ride_id = ride_id,
                passenger_id = passenger_id
            )
            ride_passenger.save()
            new_available_seats = available_seats - 1
            if request_query.first() is not None:
                request = request_query[0]
                request.status = "accepted"
                request.save()
            if new_available_seats == 0:
                ride.status = "full"
                ride.save()
            ok = True
            message =  "The passenger with id %s has been added to the ride with id %s. Now the ride has %s available seat(s)." % (passenger_id, ride_id, new_available_seats)

        return CreateRidePassenger(ok = ok, message = message)


class DeleteRidePassenger(graphene.Mutation):
    ok = graphene.Boolean()
    message = graphene.String()

    class Arguments:
        passenger_uuid = graphene.String()
        ride_id = graphene.Int()

    def mutate(self, info, passenger_uuid, ride_id):
        passenger = User.objects.filter(uuid = passenger_uuid)
        if passenger[0].uuid == passenger_uuid:
            result = RidePassenger.objects.filter(ride_id = ride_id).filter(passenger_id = passenger[0].id).delete()

            ride_query = Ride.objects.filter(id=ride_id).annotate(num_passengers=Count('ridepassenger'))

            if result[0] == 0:
                ok = False
                message = "There is no passenger with id %s in ride with id %s" % (passenger[0].id, ride_id)
            else:
                ride = ride_query[0]
                ride.status = "available"
                ride.save()
                seats = ride.total_seats - ride.num_passengers

                message =  "The passenger with id %s has been deleted from the ride with id %s. Now the ride has %s available seat(s)." % (passenger[0].id, ride_id, seats)
                ok = True

        return DeleteRidePassenger(ok = ok, message = message)

class Query(graphene.ObjectType):
    all_cities = graphene.List(CityType)
    available_rides = graphene.List(RideType)
    search_ride_by_id = graphene.List(RideType, id = graphene.Int())
    search_rides_by_cities = graphene.List(RideType, start_city_id = graphene.Int(), end_city_id = graphene.Int(), departure_date = graphene.types.datetime.Date())
    pending_requests = graphene.List(RequestType, driver_uuid = graphene.String())
    search_user_by_id = graphene.Field(UserType, id = graphene.Int())
    request = graphene.Field(RequestType)
    my_rides = graphene.List(RideType, user_uuid = graphene.String())
    searchable_cities = graphene.List(CityType)

    def resolve_searchable_cities(self, info, **kwargs):
        return City.objects.filter(Q(start_city__isnull=False) | Q(end_city__isnull=False)).order_by('city').distinct()

    def resolve_my_rides(self, info, user_uuid):
        user = User.objects.filter(uuid = user_uuid)
        if user[0].uuid == user_uuid:
            return Ride.objects.filter(Q(driver_id=user[0].id) | Q(ridepassenger__passenger_id=user[0].id)).order_by('id').distinct()

    def resolve_all_cities(self, info, **kwargs):
        return City.objects.all().order_by('city')

    def resolve_available_rides(self, info, **kwargs):
        return Ride.objects.filter(status='available')

    def resolve_search_ride_by_id(self, info, id):
        return Ride.objects.filter(id = id)

    def resolve_search_rides_by_cities(self, info, start_city_id, end_city_id, departure_date = None):

        if departure_date and Ride.objects.filter(status='available', start_city_id = start_city_id, end_city_id = end_city_id, departure_date__gte = departure_date):
            return Ride.objects.filter(status = 'available', start_city_id = start_city_id, end_city_id = end_city_id, departure_date__gte = departure_date).order_by('departure_date')

        else:
            return Ride.objects.filter(status = 'available', start_city_id = start_city_id, end_city_id = end_city_id).order_by('departure_date')

    def resolve_pending_requests(self, info, driver_uuid):
        driver = User.objects.filter(uuid = driver_uuid)
        if driver[0].uuid == driver_uuid:
            return Request.objects.filter(driver_id = driver[0].id, status = 'pending')

    def resolve_search_user_by_id(self, info, id):
        return User.objects.filter(id = id)[0]

class Mutation(graphene.ObjectType):
    create_ride = CreateRide.Field()
    change_ride_status = UpdateRide.Field()
    change_request_status = UpdateRequest.Field()
    create_request = CreateRequest.Field()
    create_ride_passenger = CreateRidePassenger.Field()
    delete_ride_passenger = DeleteRidePassenger.Field()
    login_user = LoginUser.Field()
