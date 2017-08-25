# -*- coding: utf-8 -*-
from string import digits, ascii_uppercase
from transliterate import translit
import random

#Weather api
import requests


def code_generation(bad_text=None, text=''):
    if bad_text:
        text = ''
    while len(text) < 6:
        text += random.choice(list(digits + ascii_uppercase))

    return text

def route_name_generation(airport_out, airport_in, code_name=''):
    code_name += airport_out.name[0:1]
    code_name += airport_in.name[0:1]
    code_name = (translit(code_name, reversed=True))
    while len(code_name) < 6:
        code_name += random.choice(list(digits))
    return code_name.upper()

def search_lang(search_text):
    import re
    if re.search(r'[^а-яА-Я]',search_text):
        return 'eng'
    else:
        return 'ru'

def weather_info(city_id=''):
    days = 7
    api_key = '21b44faf29243a93f1e83d29526352cc'
    url = 'http://api.openweathermap.org/data/2.5/forecast/daily?q=%s&cnt=%s&appid=%s' % (city_id, days, api_key)

    req = requests.get(url)

    return req.json()

def airport_geoconing(airport=''):
    api_key = 'AIzaSyBEyU7CLrolAMH0Ou8oi_FXxbQ1TVLpKPI'
    url = 'https://maps.googleapis.com/maps/api/geocode/json?&address=%s+терминал&key=%s&language=ru' %(airport, api_key)

    json_data = requests.get(url)
    print_data = json_data.json()
    coords = print_data['results'][0]['geometry']['viewport']['northeast']
    lat = coords['lat']
    lng = coords['lng']
    geocoding={'lat':lat, 'lng':lng}
    return geocoding

def counrty_ISO_3166_1(country=''):
    api_key = 'AIzaSyBEyU7CLrolAMH0Ou8oi_FXxbQ1TVLpKPI'
    url = 'https://maps.googleapis.com/maps/api/geocode/json?&address=%s&key=%s&language=ru' %(country, api_key)

    json_data = requests.get(url)
    print_data = json_data.json()

    i=0
    short_name = print_data ['results'][0]['address_components'][i]

    while ('country' not in short_name['types'][0]):
        i = i+1
        short_name = print_data['results'][0]['address_components'][i]

    ISO_3166_1 = {'short_name':short_name['short_name']}
    return ISO_3166_1

def center_flyway(route):
    lat_center = ((route.airport_out.lat + route.airport_in.lat) / 2)
    lng_center = ((route.airport_out.lng + route.airport_in.lng) / 2)
    center = [lat_center,lng_center]

    return center