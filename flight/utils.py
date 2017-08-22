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

