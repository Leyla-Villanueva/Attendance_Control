from rest_framework.renderers import JSONRenderer
from rest_framework import viewsets
from .models import Materia
from .serializers import MateriaSerializer


class MateriaViewSet(viewsets.ModelViewSet):

    # Esta variable indica de dónde sacar el modelo y la información de la BD
    queryset = Materia.objects.all()
    
    # Cómo serializar la información
    serializer_class = MateriaSerializer
    
    # Cómo renderizar las respuestas
    renderer_classes = [JSONRenderer]
    
    # Permitir filtrar qué métodos HTTP se pueden usar
    http_method_names = ['get', 'post', 'put', 'delete']