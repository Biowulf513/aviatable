from django.shortcuts import render, redirect
from django.http import Http404

from flight.models import Route


def index(request):
    if request.user.is_authenticated:
        return redirect('all_route')
    else:
        return redirect('login')


def all_route(request):
    routes = Route.objects.all()
    return render(request, 'flight/all_route.html', {'routes':routes})

def one_route(request, route_id):
    args = {}
    try:
        args['route'] = Route.objects.get(id=route_id)
    except Route.DoesNotExist:
        raise Http404('Рейс не найден')
    return render(request, 'flight/one_route.html', args)