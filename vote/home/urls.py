from django.contrib import admin
from django.urls import path,include
from .views import *

urlpatterns = [
    path('',home, name="home"),
    path('votingcontact/',contact,name="contact"),
    path('votingresult/',result, name="result"),
    path('votingwebsite/',web, name="web"),

]
