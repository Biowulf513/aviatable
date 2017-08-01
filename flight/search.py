# -*- coding: utf-8 -*-
from flight.models import Route
from django.db.models import Q
from django.shortcuts import render

def all_search(request, query):
    search = Route.objects.filter(
        Q(airpotr_out__name__contains=query) | Q(airpotr_in__name__contains=query)
    )
    return render(request, 'search.html', {'search':search})