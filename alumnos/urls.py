from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AlumnoViewSet, ver_asistencia, CargaMasivaAlumnosView

router = DefaultRouter()
router.register(r"api", AlumnoViewSet, basename="alumno")

urlpatterns = [
    path('import/', CargaMasivaAlumnosView.as_view(), name='carga_masiva_alumnos'),
    path("", ver_asistencia, name="ver"),
    path("", include(router.urls)),
]
