from rest_framework import serializers
from .models import Clase

class ClaseSerializer(serializers.ModelSerializer):
    materia_nombre = serializers.CharField(source='materia_id.nombre', read_only=True)
    grupo_nombre = serializers.CharField(source='grupo_id.nombre', read_only=True)
    class Meta:
        model = Clase
        fields = '__all__'
