from django.contrib import admin

from .models import City
from .models import User
from .models import Ride
from .models import RidePassenger
from .models import Request

admin.site.register(City)
admin.site.register(User)
admin.site.register(Ride)
admin.site.register(RidePassenger)
admin.site.register(Request)
