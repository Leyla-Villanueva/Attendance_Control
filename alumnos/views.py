from django.shortcuts import render
from rest_framework.renderers import JSONRenderer
from rest_framework import viewsets
from .models import Alumno
from .serializers import AlumnoSerializer

# Vista para ver asistencia
def ver_asistencia(request):
    return render(request, 'inicio.html')

class AlumnoViewSet(viewsets.ModelViewSet):
    # Esta variable indica de dónde sacar el modelo y la información de la BD
    queryset = Alumno.objects.all()
    
    # Cómo serializar la información
    serializer_class = AlumnoSerializer
    
    # Cómo renderizar las respuestas
    renderer_classes = [JSONRenderer]
    
    # Permitir filtrar qué métodos HTTP se pueden usar
    http_method_names = ['get', 'post', 'put', 'delete']


    def get_queryset(self):
        queryset = super().get_queryset()
        clase_id = self.request.query_params.get('clase', None)
        if clase_id is not None:
            queryset = queryset.filter(grupo=clase_id)  # Cambia 'grupo' por el campo de relación que tengas
        return queryset