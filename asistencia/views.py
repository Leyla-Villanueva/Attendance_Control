from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import Asistencia
from .serializers import AsistenciaSerializer

class AsistenciaViewSet(viewsets.ModelViewSet):
    queryset = Asistencia.objects.all()
    serializer_class = AsistenciaSerializer

    def create(self, request, *args, **kwargs):
        # Recibir una lista de asistencias
        asistencias = request.data.get("asistencias", [])
        
        for asistencia in asistencias:
            serializer = self.get_serializer(data=asistencia)
            if serializer.is_valid():
                serializer.save()
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        return Response({"message": "Asistencias guardadas correctamente"}, status=status.HTTP_201_CREATED)


""" from django.shortcuts import render
from rest_framework import viewsets
from .models import Asistencia
from .serializers import AsistenciaSerializer

class AsistenciaViewSet(viewsets.ModelViewSet):
    queryset = Asistencia.objects.all()
    serializer_class = AsistenciaSerializer """
