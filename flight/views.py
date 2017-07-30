from django.shortcuts import render
from flight.models import Route

def all_route(request):
    routes = Route.objects.all()
    return render(request, 'all_route.html', {'routes':routes})