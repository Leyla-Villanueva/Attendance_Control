from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import User
from rest_framework import serializers
from alumnos.models import Alumno
from maestros.models import Maestro
from django.contrib.auth.hashers import make_password

import random
import string


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)

        # Agregar el rol del usuario
        data["role"] = self.user.rol.rol  # Usar el campo 'rol' del modelo Rol

        # Agregar el nombre de usuario
        data["username"] = self.user.username

        # Agregar el ID del usuario
        data["id"] = self.user.id

        # Verificar si el usuario es un Alumno
        if hasattr(self.user, "alumno"):
            alumno = self.user.alumno
            data["nombre"] = alumno.nombre
            data["apellido_paterno"] = alumno.apellido_paterno
            data["apellido_materno"] = alumno.apellido_materno
            data["grado"] = alumno.grado
            data["grupo"] = alumno.grupo.nombre if alumno.grupo else None
            data["carrera"] = alumno.carrera_id.nombre if alumno.carrera_id else None

        # Verificar si el usuario es un Maestro
        elif hasattr(self.user, "maestro"):
            maestro = self.user.maestro
            data["nombre"] = maestro.nombre
            data["apellido_paterno"] = maestro.apellido_paterno
            data["apellido_materno"] = maestro.apellido_materno

        return data


class PasswordRecoverySerializer(serializers.Serializer):
    username = serializers.CharField()

    def validate_username(self, value):
        if not User.objects.filter(username=value).exists():
            raise serializers.ValidationError("El usuario no existe.")
        return value


class PasswordUpdateSerializer(serializers.Serializer):
    username = serializers.CharField()

    def validate_username(self, value):
        if not User.objects.filter(username=value).exists():
            raise serializers.ValidationError("El usuario no existe.")
        return value

    def generate_password(self):
        # Generar una contraseña aleatoria con letras, números y caracteres especiales
        characters = string.ascii_letters + string.digits + string.punctuation
        return "".join(random.choices(characters, k=8))

    def update_password(self):
        username = self.validated_data["username"]
        new_password = self.generate_password()  # Generar la contraseña automáticamente

        # Actualizar la contraseña del usuario
        user = User.objects.get(username=username)
        user.password = make_password(new_password)  # Encriptar la contraseña
        user.is_active = True  # Reactivar al usuario
        user.save()  # Guardar los cambios en la base de datos

        # Actualizar la contraseña temporal en la tabla Alumno (si aplica)
        if hasattr(user, "alumno"):
            alumno = user.alumno
            alumno.contrasenaTemporal = new_password  # Guardar sin encriptar
            alumno.save()

        # Actualizar la contraseña temporal en la tabla Maestro (si aplica)
        if hasattr(user, "maestro"):
            maestro = user.maestro
            maestro.contrasenaTemporal = new_password  # Guardar sin encriptar
            maestro.save()

        return new_password  # Retornar la nueva contraseña generada


class UserBlockSerializer(serializers.Serializer):
    username = serializers.CharField()

    def validate_username(self, value):
        if not User.objects.filter(username=value).exists():
            raise serializers.ValidationError("El usuario no existe.")
        return value

    def block_user(self):
        username = self.validated_data["username"]

        # Bloquear al usuario
        user = User.objects.get(username=username)
        user.is_active = False  # Desactivar al usuario
        user.save()

        return {"message": f"El usuario '{username}' ha sido bloqueado."}
