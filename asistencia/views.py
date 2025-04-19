from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import Asistencia, Unidad
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
        asistencias = request.data.get("registros", [])

        for asistencia_data in asistencias:
            alumno = asistencia_data.get("alumno")
            fecha = asistencia_data.get("fecha")
            clase = asistencia_data.get("clase")
            unidad_id = asistencia_data.get("unidad")
            estado = asistencia_data.get("estado")

            if not alumno or not fecha or not clase:
                continue  # Ignora registros incompletos

            # Obtener la instancia de Unidad si se proporciona
            unidad_instance = None
            if unidad_id:
                try:
                    unidad_instance = Unidad.objects.get(id=unidad_id)
                except Unidad.DoesNotExist:
                    unidad_instance = None  # o podrías loguear un warning si lo prefieres

            # Crear o actualizar la asistencia
            obj, creado = Asistencia.objects.update_or_create(
                alumno_id=alumno,
                clase_id=clase,
                fecha=fecha,
                defaults={
                    "estado": estado,
                    "unidad": unidad_instance,
                },
            )

        return Response({"message": "Asistencias registradas o actualizadas correctamente"}, status=status.HTTP_201_CREATED)
