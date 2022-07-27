from django.core.management.base import BaseCommand
from tennis_court_locations.tennis_courts import *
from tennis_court_locations.models import Locations

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
            