from rest_framework import viewsets
from .models import Unidad
from .serializers import UnidadSerializer
from rest_framework.decorators import action
from rest_framework.response import Response

class UnidadViewSet(viewsets.ModelViewSet):
    queryset = Unidad.objects.all()
    serializer_class = UnidadSerializer

    def get_queryset(self):
        queryset = Unidad.objects.all()
        materia_id = self.request.query_params.get("materia")
        if materia_id:
            queryset = queryset.filter(materia_id=materia_id)
        return queryset