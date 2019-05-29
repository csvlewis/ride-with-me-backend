from django.db import models

class City(models.Model):
    city = models.TextField(blank=True, null=True)
    state = models.TextField(blank=True, null=True)
    lat = models.DecimalField(max_digits=8, decimal_places=3)
    long = models.DecimalField(max_digits=8, decimal_places=3)

    class Meta:
        managed = True
        db_table = 'rides_city'

    def __str__(self):
        return '%s, %s' % (self.city, self.state)

class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    uuid = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Ride(models.Model):
    driver = models.ForeignKey(User, on_delete=models.CASCADE)
    start_city = models.ForeignKey(City, related_name='start_city', on_delete=models.CASCADE)
    end_city = models.ForeignKey(City, related_name='end_city', on_delete=models.CASCADE)
    description = models.TextField()
    mileage = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    total_seats = models.IntegerField()
    departure_date = models.DateField()
    status = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "ID: %s, Description: %s" % (self.id, self.description)

class Request(models.Model):
    ride = models.ForeignKey(Ride, on_delete=models.CASCADE)
    driver = models.ForeignKey(User, related_name='driver', on_delete=models.CASCADE)
    passenger = models.ForeignKey(User, related_name='passenger', on_delete=models.CASCADE)
    message = models.TextField()
    status = models.CharField(max_length=100, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class RidePassenger(models.Model):
    ride = models.ForeignKey(Ride, on_delete=models.CASCADE)
    passenger = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
