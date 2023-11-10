from django.shortcuts import render
from .models import *
from django.contrib.auth.decorators import login_required

@login_required
def base(request):
    return render(request,'index.html')


def login(request):
    return render(request,'login.html')