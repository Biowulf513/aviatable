# -*- coding: utf-8 -*-
# encodig: utf-8

"""aviatable URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/

Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import url
from flight.views import one_route, all_route
from flight.search import all_search, filter_search

urlpatterns = [
    url(r'^(?P<route_id>[0-9]+)/$', one_route, name='one_route'),
    url(r'^$', all_route, name='all_route'),
    url(r'^search/$', all_search),
    url(r'^search/filter/$', filter_search),
]

