from rest_framework import serializers
from .models import Asistencia, EstadoAsistencia


class EstadoAsistenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = EstadoAsistencia
        fields = '__all__'

class AsistenciaSerializer(serializers.ModelSerializer):
#    estado = EstadoAsistenciaSerializer()

    class Meta:
        model = Asistencia
        fields = ['id','alumno', 'clase', 'fecha', 'estado']
