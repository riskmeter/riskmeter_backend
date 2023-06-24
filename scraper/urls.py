from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("time/formed/", views.time_formed, name="time"),
    path("time/ip/", views.time_ip, name="time"),
    path("crime/<str:country>/<str:city>/", views.crime, name="crime"),
    path("health/covid/<str:country>/<str:city>/", views.corona_data, name="crime"),
]
