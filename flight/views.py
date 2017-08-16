from django.shortcuts import render
from flight.models import Route
from django.contrib import auth


def all_route(request):
    routes = Route.objects.all()
    return render(request, 'flight/all_route.html', {'routes':routes, 'username': auth.get_user(request).username})

def one_route(request, route_id):
    args = {}
    args['route'] = Route.objects.get(id=route_id)
    args['user'] = auth.get_user(request).username
    return render(request, 'flight/one_route.html', args)