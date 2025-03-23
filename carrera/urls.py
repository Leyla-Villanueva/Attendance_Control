from django.urls import path,include
from rest_framework.routers import SimpleRouter
from .views import *

router = SimpleRouter()
router.register(r'api', CarreraViewSet)

urlpatterns = [
    path('', include(router.urls)),
]