from django.contrib import admin
from django.urls import path,include

from django.urls import include

from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('alumnos/', include('alumnos.urls')),
    path('materia/', include('materia.urls')),
    path('grupo/', include('grupo.urls')),
    path('users/', include('users.urls')),
    path('maestros/', include('maestros.urls')),
    path('carrera/', include('carrera.urls')),
    path('clase/', include('clase.urls')),
    path('asistencia/', include('asistencia.urls')),
    path('unidad/', include('unidad.urls')),
]
