from django.contrib import admin
from django.urls import path
from django.urls import include

from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    
]
