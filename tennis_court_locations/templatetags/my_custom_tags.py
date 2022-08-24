from django import template
import json
from urllib.request import urlopen


register = template.Library()

@register.simple_tag
def get_user_location():
    url = 'http://ipinfo.io/json'
    response = urlopen(url)
    data = json.load(response)
    data = data['loc'].split(",")
    print(type(data))
    user_lat = float(data[0])
    user_lon = float(data[1])
    return user_lat, user_lon
