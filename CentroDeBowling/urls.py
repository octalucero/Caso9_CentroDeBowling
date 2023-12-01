from django.contrib import admin
from .views import BaseView, LoginView
from . import views
from django.urls import path


urlpatterns = [
    path('', BaseView.as_view(), name='index'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('reserva/', views.ReservaView.as_view(), name = 'reserva'),
    path('registro/', views.ClienteView.as_view(), name='registro'),
    path('cafeteria/', views.CafeteriaView.as_view(), name='cafeteria')
    ]