from django.shortcuts import render
from flight.models import Route

def all_route(request):
    routes = Route.objects.all()
    return render(request, 'all_route.html', {'routes':routes})

def one_route(request, route_id):
    route = Route.objects.get(id=route_id)
    return render(request, 'one_route.html', {'route':route})