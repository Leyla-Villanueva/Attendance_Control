from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ClaseViewSet

router = DefaultRouter()
router.register(r'api', ClaseViewSet)

urlpatterns = [
    path('', include(router.urls)),
]