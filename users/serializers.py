from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import User
from rest_framework import serializers
from alumnos.models import Alumno
from maestros.models import Maestro


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
