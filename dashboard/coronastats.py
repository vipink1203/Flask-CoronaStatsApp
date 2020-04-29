import requests
from datetime import datetime as dt, timedelta
from heapq import nlargest


response = requests.get('https://coronacache.home-assistant.io/corona.json')   
# print json content 
res = response.json()
corona_list = []
mc = []

def allCountries():
    for country in res['features']:
        dict = {
            'Country' : str(country['attributes']['Country_Region']),
            'Deaths' : country['attributes']['Deaths'],
            'Confirmed' : country['attributes']['Confirmed'],
            'Recovered' : country['attributes']['Recovered'],
            'Active' : country['attributes']['Active'],
            'Last_updated': str(dt.fromtimestamp(float(country['attributes']['Last_Update'])/1000).strftime('%Y-%m-%d'))
        }
        corona_list.append(dict)
    return corona_list