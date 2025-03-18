from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import GrupoViewSet

router = DefaultRouter()
router.register(r'grupo', GrupoViewSet, basename='grupo')

urlpatterns = [
    path('api/', include(router.urls)),
]