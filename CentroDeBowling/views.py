from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse

def home(request):
    return render(request,'home.html')


#comprueba si la contraseña ingresada es correcta, en caso de serlo redirige a la vista de reservas
def signup(request):
    if request.method == 'GET':
        return render(request,'signup.html',{
        'form': UserCreationForm
    })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                user.save()
                return redirect('reserva')
            except:
                return render (request, 'signup.html', {
                    'form': UserCreationForm,
                    "error": 'Usuario ya existente'
                })
        return render (request, 'signup.html', {
            'form': UserCreationForm,
            "error": 'Contra no coinciden'
        })


def reserva(request):
    return render(request, 'rev.html')


def login(request):
    return render(request,'login.html')

