from django.shortcuts import render
from .models import Clase
from .serializers import ClaseSerializer
from rest_framework import viewsets

class ClaseViewSet(viewsets.ModelViewSet):
    queryset = Clase.objects.all()
    serializer_class = ClaseSerializer