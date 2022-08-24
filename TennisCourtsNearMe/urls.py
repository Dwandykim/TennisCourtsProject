"""TennisCourtsNearMe URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from tennis_court_locations import views
# from userLocation import views

# from tennis_court_locations import views

urlpatterns = [
    path('admin/', admin.site.urls),
        path('', views.Home.as_view()),
        # path('locate', views.UserLocation.as_views()),
        # path('locate', views.user_location)
        # path('userLocation/', userLocation, name='userLocation')
        # path('',include('tennis_court_locations.urls')),
]

## Working!!
# urlpatterns = [
#     path('admin/', admin.site.urls),
#         path('', include('tennis_court_locations.urls'), name="TennisCourts")
# ]
