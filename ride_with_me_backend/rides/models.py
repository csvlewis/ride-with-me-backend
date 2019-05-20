from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class City(models.Model):
    city = models.TextField(blank=True, null=True)
    state = models.TextField(blank=True, null=True)
    lat = models.TextField(blank=True, null=True)
    long = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'rides_city' 

    def __str__(self):
        return '%s, %s' % (self.city, self.state)


class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone_number = PhoneNumberField(blank=True)
    api_key = models.UUIDField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Ride(models.Model):
    driver_id = models.ForeignKey(User, on_delete=models.CASCADE)
    start_city_id = models.ForeignKey(City, related_name='start_city_id', on_delete=models.CASCADE)
    end_city_id = models.ForeignKey(City, related_name='end_city_id', on_delete=models.CASCADE)
    description = models.TextField()
    mileage = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    total_seats = models.IntegerField()
    departure_time = models.DateTimeField()
    status = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Request(models.Model):
    ride_id = models.ForeignKey(Ride, on_delete=models.CASCADE)
    driver_id = models.ForeignKey(User, related_name='driver_id', on_delete=models.CASCADE)
    passenger_id = models.ForeignKey(User, related_name='passenger_id', on_delete=models.CASCADE)
    message = models.TextField()
    status = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class RidePassengers(models.Model):
    ride_id = models.ForeignKey(Ride, on_delete=models.CASCADE)
    passenger_id = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
