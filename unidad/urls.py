from rest_framework import routers
from unidad.views import UnidadViewSet
from django.urls import path, include

router = routers.DefaultRouter()
router.register(r'api', UnidadViewSet)

urlpatterns = [
    path('', include(router.urls)),
]