from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import MateriaViewSet

router = SimpleRouter()
router.register("api", MateriaViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
