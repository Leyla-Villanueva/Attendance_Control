from django.shortcuts import render
from .views import *
from django.urls import path,include
from rest_framework import viewsets
from .models import Alumno
from .serializers import AlumnoSerializer

# Create your views here.
def ver_asistencia(request):
    return render(request, 'inicio.html')

class AlumnoViewSet(viewsets.ModelViewSet):
    queryset = Alumno.objects.all()
    serializer_class = AlumnoSerializer
    
