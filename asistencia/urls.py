from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AsistenciaViewSet, calcular_porcentaje_asistencia, calcular_porcentaje_asistencia_general

router = DefaultRouter()
router.register(r'api', AsistenciaViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('calcular-porcentaje/',calcular_porcentaje_asistencia, name='calcular_porcentaje_asistencia'),
    path('porcentaje_general/',calcular_porcentaje_asistencia_general, name='calcular_porcentaje_asistencia_general')
]
