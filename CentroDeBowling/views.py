from django.shortcuts import render
from .models import *

def base(request):
    return render(request,'index.html')

def login(request):
    return render(request,'login.html')