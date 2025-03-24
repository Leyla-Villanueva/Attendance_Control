from rest_framework.renderers import JSONRenderer
from rest_framework import viewsets
from .models import Grupo
from .serializers import GrupoSerializer

class GrupoViewSet(viewsets.ModelViewSet):

    queryset = Grupo.objects.all()

    serializer_class = GrupoSerializer

    renderer_classes = [JSONRenderer]
    
    http_method_names = ['get', 'post', 'put', 'delete']
