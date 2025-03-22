from rest_framework import viewsets
from .models import Maestro
from .serializers import MaestroSerializer

class MaestroViewSet(viewsets.ModelViewSet):
    queryset = Maestro.objects.all()
    serializer_class = MaestroSerializer