from django.shortcuts import render
from .models import *

def base(request):
    return render(request,'index.html')