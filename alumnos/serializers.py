from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Alumno
from rol.models import Rol
import random
import string

User = get_user_model()


class AlumnoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alumno
        fields = "__all__"
        extra_kwargs = {
            "contrasenaTemporal": {"required": False},
            "id": {"required": False},
            "carrera_id": {"required": False},
            "grado": {"required": False},
            "grupo": {"required": False},
        }

    def create(self, validated_data):
        # Crear el usuario
        first_name = validated_data["nombre"]
        last_name = validated_data["apellido_paterno"]
        username = f"{first_name}.{last_name}".lower()

        # Creación de contraseña con letras, números y caracteres especiales
        characters = string.ascii_letters + string.digits + string.punctuation
        password = "".join(random.choices(characters, k=8))

        # Asignación del rol
        rol_alumno = Rol.objects.get(rol="alumno")

        # Crear el usuario
        user = User.objects.create_user(
            username=username, password=password, rol=rol_alumno
        )

        # Crear el alumno y guardar la contraseña sin encriptar en contrasenaTemporal
        alumno = Alumno.objects.create(
            id=user, contrasenaTemporal=password, **validated_data
        )
        return alumno
