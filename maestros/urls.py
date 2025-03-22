from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import MaestroViewSet

router = SimpleRouter()
router.register("api", MaestroViewSet)

urlpatterns = [path("", include(router.urls))]
