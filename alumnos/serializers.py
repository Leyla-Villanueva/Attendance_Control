from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Alumno
from rol.models import Rol
import random
import string
from users.serializers import CustomUserSerializer

User = get_user_model()


class AlumnoSerializer(serializers.ModelSerializer):

    usuario = CustomUserSerializer(source="id", read_only=True)

    asistencia = serializers.CharField(
        required=False
    )  # Campo adicional para asistencia
    color = serializers.CharField(required=False)  # Campo adicional para color

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
        # Validar el campo 'nombre'
        first_name = (
            validated_data["nombre"].split()[0]
            if validated_data.get("nombre") and " " in validated_data["nombre"]
            else validated_data.get("nombre", "")
        )
        if not first_name:
            raise serializers.ValidationError("El campo 'nombre' es obligatorio.")

        last_name = validated_data["apellido_paterno"]

        # Generar un username único
        while True:
            random_suffix = "".join(random.choices(string.ascii_letters + string.digits, k=3))
            username = f"{first_name}.{last_name}".lower() + random_suffix
            if not User.objects.filter(username=username).exists():
                break

        # Creación de contraseña
        characters = string.ascii_letters + string.digits + string.punctuation
        password = "".join(random.choices(characters, k=8))

        # Asignación del rol
        try:
            rol_alumno = Rol.objects.get(rol="alumno")
        except Rol.DoesNotExist:
            raise serializers.ValidationError("El rol 'alumno' no existe.")

        # Crear el usuario
        user = User.objects.create_user(
            username=username, password=password, rol=rol_alumno
        )

        # Crear el alumno
        alumno = Alumno.objects.create(
            id=user, contrasenaTemporal=password, **validated_data
        )
        return alumno
