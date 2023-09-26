from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [path("info", views.get_metar_data, name="metar_data")]
