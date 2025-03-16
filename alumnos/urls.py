from django.urls import path
from .views import *

urlpatterns = [
    path('ver/', ver_asistencia, name='ver'),
]