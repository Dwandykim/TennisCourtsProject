# from django.contrib import admin
from django.contrib.gis import admin
from django.contrib.gis.admin import OSMGeoAdmin
# "Relatively Import" - they are in the same directory/module
from .models import Locations, PublicCourts

# Register your models here.

# def register(self, model_or_iterable, admin_class=None, **options):
#     myModels = [models.Locations, models.PublicCourts]  # iterable list
#     admin.site.register(myModels)

# admin.site.register(Locations)
# admin.site.register(PublicCourts)

@admin.register(PublicCourts)
class TennisAdmin(OSMGeoAdmin):
    list_display = ("park_name", "coordinates")