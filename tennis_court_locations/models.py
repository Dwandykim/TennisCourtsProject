from django.contrib.gis.db import models
from django.contrib.gis.geos import Point
# Create your models here.

class Locations(models.Model):
    park_name = models.CharField(max_length=150) #max_length is required
    address = models.CharField(max_length=300)
    type = models.CharField(max_length=25)
    fees = models.CharField(max_length=10)
    lights = models.CharField(max_length=10)
    indoor = models.CharField(max_length=10)
    courts = models.CharField(max_length=10)
    
    def __str__(self) -> str:
        return self.park_name

class PublicCourts(models.Model):
    park_name = models.CharField(max_length=150) #max_length is required
    address = models.CharField(max_length=300)
    # coordinates = models.PointField(null=True, srid=4326)
    coordinates = models.PointField(geography=True, default=Point(0.0, 0.0), srid=4326)
    # location_address = models.CharField(max_length=300)
    type = models.CharField(max_length=25)
    fees = models.CharField(max_length=10)
    lights = models.CharField(max_length=10)
    indoor = models.CharField(max_length=10)
    courts = models.CharField(max_length=10)
    latitude = models.DecimalField(max_digits=22, decimal_places=16, blank=True, null=True)
    longitude = models.DecimalField(max_digits=22, decimal_places=16, blank=True, null=True)

    def __str__(self) -> str:
        return self.park_name
        