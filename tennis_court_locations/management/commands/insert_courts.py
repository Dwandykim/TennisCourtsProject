from django.core.management.base import BaseCommand
from tennis_court_locations.tennis_courts import *
from tennis_court_locations.public_courts import *
from tennis_court_locations.models import Locations, PublicCourts
from django.contrib.gis.geos import Point

class Command(BaseCommand):
    
    def handle(self, *args, **kwargs):
        
        tennis_courts = la_tennis_courts()
        for court in tennis_courts:
            Locations.objects.create(
                park_name = court["park_name"],
                address = court["address"],
                type = court["type"], 
                fees = court["fees"], 
                lights = court["lights"], 
                indoor = court["indoor"], 
                courts = court["courts"], 
                
            )

        public_courts = get_public_courts()
        for court in public_courts:
            PublicCourts.objects.create(
                park_name = court["park_name"],
                address = court["address"],
                type = court["type"], 
                fees = court["fees"], 
                lights = court["lights"], 
                indoor = court["indoor"], 
                courts = court["courts"], 
                coordinates = Point(x=court["location_long"],y=court["location_lat"],srid=4326),
                latitude = court["location_lat"],
                longitude = court["location_long"],

            )