from django.shortcuts import render
from .views import *
from django.urls import path,include

# Create your views here.
def ver_asistencia(request):
    return render(request, 'inicio.html')