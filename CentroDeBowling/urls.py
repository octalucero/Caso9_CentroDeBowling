from django.contrib import admin
from .views import base, login
from . import views
from django.urls import path


urlpatterns = [
    path('', views.base, name = 'index'),
    path('login/', base, name = 'login')
]