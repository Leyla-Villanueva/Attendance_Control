from rest_framework import serializers
from .models import Unidad

class UnidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unidad
        fields = '__all__'
        extra_kwargs = {
            'materia': {'required': False}
        }

    def validate(self, data):
            #Validación para asegurarse de que la fecha de fin sea posterior a la de inicio
            if data['fecha_fin'] < data['fecha_inicio']:
                raise serializers.ValidationError("La fecha de fin no puede ser anterior a la fecha de inicio.")
            return data