from django.contrib import admin
from .views import *
from . import views
from django.urls import path


urlpatterns = [
    path('', views.base, name = 'index'),
    path('login/',login,  name = 'login')
]