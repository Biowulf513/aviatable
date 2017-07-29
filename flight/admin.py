from django.contrib import admin
from flight.models import PlaneType, Plane, Country, City, Airport, Route

admin.site.register(PlaneType)
admin.site.register(Plane)
admin.site.register(Country)
admin.site.register(City)
admin.site.register(Airport)
admin.site.register(Route)
