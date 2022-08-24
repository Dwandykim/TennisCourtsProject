from django.views import generic
from django.contrib.gis.db.models.functions import Distance
from .models import PublicCourts
from django.contrib.gis.geos import Point

from django.shortcuts import render, redirect

import json
from json import dumps
from django.http import HttpResponse


user_latitude_member = 34.0621149
user_longitude_member = -118.3088618

class Home(generic.ListView):
    # Wilshire / Western
    user_latitude = user_latitude_member
    user_longitude = user_longitude_member
    print("USER LAT:", user_latitude)
    print("USER LONG:", user_longitude)
    user_location = Point(user_longitude, user_latitude, srid=4326)
    model = PublicCourts
    context_object_name = "courts"
    print(type(context_object_name))
    queryset = PublicCourts.objects.annotate(distance=Distance('coordinates', user_location)
    ).order_by("distance")[0:10]
    print(type(queryset))
    template_name = 'courts/index.html'























# def user_location(request):
#     request_body = json.loads(request.body.decode('utf-8'))
#     if request_body:
#         print(request_body['latitude'])
#         print(type(request_body['latitude']))
#         user_latitude_member = request_body['latitude']
#         user_longitude_member = request_body['longitude']
#         location = {
#             "user_latitude_member" : user_latitude_member,
#             "user_longitude_member" : user_longitude_member
#         }
#         return redirect('/locate/')
#     # location = dumps(location)
#     return render(request, 'courts/locate.html', location)   
    # return render(request, 'courts/index.html', {"user_latitude_member" : request_body['latitude'],"user_longitude_member" : request_body['longitude']})

def user_location(request):
    request_body = json.loads(request.body.decode('utf-8'))
    print(request_body['latitude'])
    print(type(request_body['latitude']))
    user_latitude_member = request_body['latitude']
    user_longitude_member = request_body['longitude']
    context = {
        "user_latitude_member" : user_latitude_member,
        "user_longitude_member" : user_longitude_member
    }
    # location = dumps(location)
    return render(request, 'courts/index.html', {"context": context}) 




    