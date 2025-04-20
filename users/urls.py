from django.urls import path, include
from .views import *
from rest_framework.routers import SimpleRouter
from rest_framework_simplejwt.views import TokenRefreshView
from .views import PasswordRecoveryView

router = SimpleRouter()
router.register('api', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('token/', CustomTokenObtainPairView.as_view(), name='token'),
    path('token/refresh/', TokenRefreshView.as_view(), name='refresh'),
    path('password-recovery/', PasswordRecoveryView.as_view(), name='password-recovery'),
    path('password-update/', PasswordUpdateView.as_view(), name='password-update'),
    path('block-user/', BlockUserView.as_view(), name='block_user'),
]
