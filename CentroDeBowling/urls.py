from django.contrib import admin
from .views import BaseView, LoginView
from . import views
from django.urls import path


urlpatterns = [
    path('', views.BaseView.as_view(), name='index'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('reservas/', views.ReservasView.as_view(), name = 'reservas'),
    path('reservas/reservar/', views.ReservarView.as_view(), name = 'reservar'),
    path('reservas/editar/', views.EditView.as_view(), name = 'editar'),
    path('reservas/read/', views.ReadView.as_view(), name = 'read'),
    path('reservas/borrar/', views.DeleteView.as_view(), name = 'borrar'),
    path('registro/', views.ClienteView.as_view(), name='registro'),
    path('cafeteria/', views.CafeteriaView.as_view(), name='cafeteria'),
    ]