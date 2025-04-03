from rest_framework import serializers
from .models import Grupo
from alumnos.models import Alumno  # Importa el modelo Alumno
from carrera.models import Carrera  # Importa el modelo Carrera


class GrupoSerializer(serializers.ModelSerializer):
    alumnos = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Alumno.objects.all(), required=False
    )  # Campo para recibir los IDs de los alumnos
    carrera = serializers.PrimaryKeyRelatedField(
        queryset=Carrera.objects.all(), required=False
    )  # Campo para recibir el ID de la carrera

    class Meta:
        model = Grupo
        fields = "__all__"

    def create(self, validated_data):
        # Extraer los IDs de los alumnos y la carrera del JSON
        alumnos_data = validated_data.pop("alumnos", [])
        carrera_data = validated_data.pop("carrera", None)

        # Crear el grupo
        grupo = Grupo.objects.create(**validated_data)

        # Asignar el grupo, grado y carrera a los alumnos especificados
        for alumno in alumnos_data:
            alumno.grupo = grupo
            alumno.grado = grupo.grado
            if carrera_data:  # Si se especifica una carrera, actualizarla
                alumno.carrera_id = carrera_data
            alumno.save()

        return grupo

    def update(self, instance, validated_data):
        # Extraer los IDs de los alumnos y la carrera del JSON
        alumnos_data = validated_data.pop("alumnos", [])
        carrera_data = validated_data.pop("carrera", None)

        # Actualizar el grupo
        instance.nombre = validated_data.get("nombre", instance.nombre)
        instance.grado = validated_data.get("grado", instance.grado)

        # Si se especifica una nueva carrera, actualizarla en el grupo
        if carrera_data:
            instance.carrera_id = carrera_data

        instance.save()

        # Asignar el grupo, grado y carrera a los alumnos especificados
        for alumno in alumnos_data:
            alumno.grupo = instance
            alumno.grado = instance.grado

            # Si no se especifica una carrera explícita, usar la carrera del grupo
            if not alumno.carrera_id:
                alumno.carrera_id = instance.carrera_id

            alumno.save()

        return instance
