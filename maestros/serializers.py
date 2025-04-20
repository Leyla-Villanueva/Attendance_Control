from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Maestro
from rol.models import Rol
import random
import string
from users.serializers import CustomUserSerializer

User = get_user_model()


class MaestroSerializer(serializers.ModelSerializer):

    usuario = CustomUserSerializer(source="id", read_only=True)

    class Meta:
        model = Maestro
        fields = "__all__"
        extra_kwargs = {
            "contrasenaTemporal": {"required": False},
            "id": {"required": False},
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
            random_suffix = "".join(
                random.choices(string.ascii_letters + string.digits, k=3)
            )
            username = f"{first_name}.{last_name}".lower() + random_suffix
            if not User.objects.filter(username=username).exists():
                break

        # Creación de contraseña con letras, números y caracteres especiales
        characters = string.ascii_letters + string.digits + string.punctuation
        password = "".join(random.choices(characters, k=8))

        # Asignación del rol
        try:
            rol_maestro = Rol.objects.get(rol="maestro")
        except Rol.DoesNotExist:
            raise serializers.ValidationError("El rol 'maestro' no existe.")

        # Crear el usuario
        user = User.objects.create_user(
            username=username, password=password, rol=rol_maestro
        )

        # Crear el maestro
        maestro = Maestro.objects.create(
            id=user, contrasenaTemporal=password, **validated_data
        )
        return maestro