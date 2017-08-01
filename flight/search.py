# -*- coding: utf-8 -*-
from flight.models import Route
from django.db.models import Q
from django.shortcuts import render
from flight.utils import search_lang


def all_search(request):
    if 'search_q' in request.GET:
        query = request.GET['search_q']
        if search_lang(query) != 'ru':
            search = Route.objects.filter(
              Q(code__icontains=query) | Q(plane__reg_numb__icontains=query)
            )
        else:
            search = Route.objects.filter(
                Q(airpotr_out__name__icontains=query) | Q(airpotr_in__name__icontains=query)
            )
        return render(request, 'search.html', {'search':search})
