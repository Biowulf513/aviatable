# -*- coding: utf-8 -*-
from flight.models import Route
from django.db.models import Q
from django.shortcuts import render
from flight.utils import search_lang


def all_search(request, query=''):
    if request.GET:
        context = {}
        query=request.GET['search_q']
        if search_lang(query) != 'ru':
            context['routes'] = Route.objects.filter(
              Q(code__icontains=query) | Q(plane__reg_numb__icontains=query)
            )
        else:
            query = query.capitalize()
            context['routes'] = Route.objects.filter(
                Q(airport_out__name__icontains=query) | Q(airport_in__name__icontains=query)
            )

        if context['routes']:
            return render(request, 'flight/search_route.html', context)

        else:
            context.clear()
            context['message'] = 'Рейса с данными параметрами не найдено!'
        return render(request, 'flight/search_route.html', context)

def filter_search(request, ):
    if request.GET:
        query = []
        context ={}
        query.append(Q(airport_out__name__icontains=request.GET['out']))
        query.append(Q(airport_in__name__icontains=request.GET['in']))

        context['routes'] = Route.objects.filter(query[0]).filter(query[1])
        if context['routes']:
            return render(request, 'flight/search_route.html', context)

        else:
            context.clear()
            context['message'] = 'Такого рейса не существует'

        return render(request, 'flight/search_route.html', context)
