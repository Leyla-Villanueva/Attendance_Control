from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Maestro
from rol.models import Rol
import random
import string

User = get_user_model()

class MaestroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Maestro
        fields = '__all__'
        extra_kwargs = {
            'contrasenaTemporal': {'required': False},
            'id': {'required': False}
        }
        
    def create(self, validated_data):
        # Crear el usuario
        first_name = validated_data['nombre']
        last_name = validated_data['apellido_paterno']
        username = f"{first_name}.{last_name}".lower()
        #Creacion de contraseña con letras, numeros y caracteres especiales
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choices(characters, k=8))
        
        #Asignacion del rol
        rol_maestro = Rol.objects.get(rol='maestro')
        
        #User
        user = User.objects.create_user(username=username, password=password, rol=rol_maestro)
        
        #Creacion del maestro pero con contraseña temporal (le vamos a preguntar a Derick como hacer esto xd)
        maestro = Maestro.objects.create(id=user, contrasenaTemporal=password, **validated_data)
        return maestro