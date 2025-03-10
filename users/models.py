from django.db import models

from rol.models import Rol
class User(models.Model):
    id_user = models.AutoField(primary_key=True)
    username = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE)
    token = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.username