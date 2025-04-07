from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import Asistencia
from .serializers import AsistenciaSerializer

class AsistenciaViewSet(viewsets.ModelViewSet):
    queryset = Asistencia.objects.all()
    serializer_class = AsistenciaSerializer

    def get_queryset(self):
        queryset = Asistencia.objects.all()
        clase_id = self.request.query_params.get("clase", None)
        if clase_id is not None:
            queryset = queryset.filter(clase_id=clase_id)
        return queryset

    def create(self, request, *args, **kwargs):
        asistencias = request.data.get("registros", [])  # <- Asegúrate que usas "registros" y no "asistencias"

        for asistencia_data in asistencias:
            alumno = asistencia_data.get("alumno")
            fecha = asistencia_data.get("fecha")
            clase = asistencia_data.get("clase") or asistencia_data.get("unidad")  # Dependiendo del nombre que uses
            estado = asistencia_data.get("estado")

            if not alumno or not fecha or not clase:
                continue  # Ignora registros incompletos

            # Buscar si ya existe una asistencia para ese alumno, clase y fecha
            obj, creado = Asistencia.objects.update_or_create(
                alumno_id=alumno,
                clase_id=clase,
                fecha=fecha,
                defaults={"estado": estado},
            )

        return Response({"message": "Asistencias registradas o actualizadas correctamente"}, status=status.HTTP_201_CREATED)


""" from django.shortcuts import render
from rest_framework import viewsets
from .models import Asistencia
from .serializers import AsistenciaSerializer

class AsistenciaViewSet(viewsets.ModelViewSet):
    queryset = Asistencia.objects.all()
    serializer_class = AsistenciaSerializer """
