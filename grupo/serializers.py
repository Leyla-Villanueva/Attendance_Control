from rest_framework import serializers
from .models import Grupo
from alumnos.models import Alumno  # Importa el modelo Alumno
from carrera.models import Carrera  # Importa el modelo Carrera
from carrera.serializers import CarreraSerializer  # Importa el serializer de Carrera


class GrupoSerializer(serializers.ModelSerializer):
    alumnos = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Alumno.objects.all(), required=False
    )
    carrera = CarreraSerializer(read_only=True)
    carrera_id = serializers.PrimaryKeyRelatedField(
        queryset=Carrera.objects.all(),
        write_only=True,
        source="carrera",
        required=False,
    )

    class Meta:
        model = Grupo
        fields = "__all__"

    def create(self, validated_data):
        # Extraer la lista de alumnos de los datos validados
        alumnos_data = validated_data.pop("alumnos", [])

        # Crear el grupo con los datos restantes (incluyendo carrera)
        grupo = Grupo.objects.create(**validated_data)

        # Actualizar cada alumno con el nuevo grupo y datos relacionados
        for alumno in alumnos_data:
            alumno.grupo = grupo
            alumno.grado = grupo.grado
            alumno.carrera = grupo.carrera  # Asignar la misma carrera que el grupo
            alumno.save()

        return grupo

    def update(self, instance, validated_data):
        # Extraer alumnos
        alumnos_data = validated_data.pop("alumnos", [])

        # Actualizar los campos del grupo utilizando los datos validados restantes
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        # Manejar los alumnos actuales
        current_alumnos = list(instance.alumnos.all())

        # Eliminar alumnos que no están en la nueva lista
        for alumno in current_alumnos:
            if alumno not in alumnos_data:
                alumno.grupo = None
                alumno.grado = ""
                # Mantener la carrera como está, o establecerla como None si es necesario
                # alumno.carrera = None
                alumno.save()

        # Asignar valores actualizados a los alumnos en la nueva lista
        for alumno in alumnos_data:
            alumno.grupo = instance
            alumno.grado = instance.grado
            alumno.carrera = instance.carrera  # Asegurar que la carrera esté asignada
            alumno.save()

        return instance
