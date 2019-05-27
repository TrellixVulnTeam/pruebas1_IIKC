from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'jvc/inicioSesion.html')


def dashboard(request):
    return render(request, 'jvc/dashboard.html')
