from django.contrib import admin
from .views import *
from . import views
from django.urls import path


urlpatterns = [
    path('', home, name = 'home'),
    path('login/',login,  name = 'login'),
    path('signup/',signup,  name = 'signup'),
    path('reserva/',reserva,  name = 'reserva')
]