from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import MaestroViewSet, ExportarMaestrosView

router = SimpleRouter()
router.register("api", MaestroViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("export/", ExportarMaestrosView.as_view(), name="exportar_maestros"),
    ]
