from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AlumnoViewSet, ver_asistencia

# Usamos DefaultRouter para registrar las rutas
router = DefaultRouter()
router.register(r"api", AlumnoViewSet, basename="alumno")

urlpatterns = [
    path("", ver_asistencia, name="ver"),  # Incluimos la ruta para ver asistencia
    path("", include(router.urls)),  # Incluimos las rutas del router
]
