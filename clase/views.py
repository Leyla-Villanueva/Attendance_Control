from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Clase
from .serializers import ClaseSerializer

class ClaseViewSet(viewsets.ModelViewSet):
    queryset = Clase.objects.all()
    serializer_class = ClaseSerializer

    @action(detail=False, methods=["get"], url_path="por_maestro/(?P<maestro_id>[^/.]+)")
    def por_maestro(self, request, maestro_id=None):
        clases = Clase.objects.filter(maestro_id=maestro_id)
        serializer = self.get_serializer(clases, many=True)
        return Response(serializer.data)