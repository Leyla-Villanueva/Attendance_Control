<<<<<<< HEAD
from django.urls import path
from .views import *
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('api', AlumnoViewSet)

urlpatterns = [
    path("ver/", ver_asistencia, name="ver"),
    path('', include(router.urls))
]
=======
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AlumnoViewSet

router = DefaultRouter()
router.register(r'alumnos', AlumnoViewSet, basename='alumno')

urlpatterns = [
    path('api/', include(router.urls)),
]
>>>>>>> Ana-Jatz
