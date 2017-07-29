from django.contrib import admin
from flight.models import PlaneType, Plane, Country, City

admin.site.register(PlaneType)
admin.site.register(Plane)
admin.site.register(Country)
admin.site.register(City)
