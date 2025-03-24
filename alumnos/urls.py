from django.urls import path
from .views import *
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('api', AlumnoViewSet)

urlpatterns = [
    path("ver/", ver_asistencia, name="ver"),
    path('', include(router.urls))
]
