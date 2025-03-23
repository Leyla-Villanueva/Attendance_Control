from rest_framework import serializers
from .models import Alumno

class AlumnoSerializer(serializers.ModelSerializer):
    asistencia = serializers.CharField()  # Por ejemplo, podrías hacerlo estático o de alguna otra manera
    color = serializers.CharField()  # Usamos un color aleatorio o de alguna lógica específica

    class Meta:
        model = Alumno
        fields = '__all__'

        