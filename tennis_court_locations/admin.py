from django.contrib import admin
# "Relatively Import" - they are in the same directory/module
from .models import Locations

# Register your models here.
admin.site.register(Locations)