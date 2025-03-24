from rest_framework import serializers
from .models import Materia
from unidad.models import Unidad
from unidad.serializers import UnidadSerializer

class MateriaSerializer(serializers.ModelSerializer):
    unidades = UnidadSerializer(many=True)

    class Meta:
        model = Materia
        fields = '__all__'

    def create(self, validated_data):
        unidades_data = validated_data.pop('unidades')
        materia = Materia.objects.create(**validated_data)
        for unidad_data in unidades_data:
            Unidad.objects.create(materia=materia, **unidad_data)
        return materia

    def update(self, instance, validated_data):
        unidades_data = validated_data.pop('unidades')
        instance.nombre = validated_data.get('nombre', instance.nombre)
        instance.save()

        # Actualizar las unidades
        for unidad_data in unidades_data:
            unidad_id = unidad_data.get('id')
            if unidad_id:
                unidad = Unidad.objects.get(id=unidad_id, materia=instance)
                unidad.nombre = unidad_data.get('nombre', unidad.nombre)
                unidad.fecha_inicio = unidad_data.get('fecha_inicio', unidad.fecha_inicio)
                unidad.fecha_fin = unidad_data.get('fecha_fin', unidad.fecha_fin)
                unidad.save()
            else:
                Unidad.objects.create(materia=instance, **unidad_data)

        return instance