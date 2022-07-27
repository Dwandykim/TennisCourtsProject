from django.db import models
  
# Create your models here.

class Locations(models.Model):
    park_name = models.CharField(max_length=150) #max_length is required
    address = models.CharField(max_length=300)
    type = models.CharField(max_length=25)
    fees = models.CharField(max_length=10)
    lights = models.CharField(max_length=10)
    indoor = models.CharField(max_length=10)
    courts = models.CharField(max_length=10)
    

    

        