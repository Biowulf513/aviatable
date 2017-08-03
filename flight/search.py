# -*- coding: utf-8 -*-
from flight.models import Route
from django.db.models import Q
from django.shortcuts import render
from flight.utils import search_lang


def all_search(request, query=''):
    if request.GET:
        if request.GET.get('search_q')!='':
            query=request.GET['search_q']
            if search_lang(query) != 'ru':
                search = Route.objects.filter(
                  Q(code__icontains=query) | Q(plane__reg_numb__icontains=query)
                )
            else:
                query = query.capitalize()
                search = Route.objects.filter(
                    Q(airport_out__name__icontains=query) | Q(airport_in__name__icontains=query)
                )
            return render(request, 'search_route.html', {'routes':search})

        if request.GET.get('out')!='':
            query=request.GET['out']
            search = Route.objects.filter(
                Q(airport_out__name__icontains=query))
            return render(request, 'search_route.html', {'routes': search})

        elif request.GET.get('in')!='':
            query=request.GET['in']
            search = Route.objects.filter(
                Q(airport_in__name__icontains=query))
            return render(request, 'search_route.html', {'routes': search})

