from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AsistenciaViewSet, calcular_porcentaje_asistencia, calcular_porcentaje_asistencia_general, exportar_asistencia_excel

router = DefaultRouter()
router.register(r'api', AsistenciaViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('calcular-porcentaje/',calcular_porcentaje_asistencia, name='calcular_porcentaje_asistencia'),
    path('porcentaje_general/',calcular_porcentaje_asistencia_general, name='calcular_porcentaje_asistencia_general'),
    path('exportar-excel/', exportar_asistencia_excel, name='exportar_asistencia_excel'),
]
