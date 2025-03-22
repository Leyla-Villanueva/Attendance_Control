from django.db import models

from users.models import User

class Maestro(models.Model):
    id = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido_paterno = models.CharField(max_length=100)
    apellido_materno = models.CharField(max_length=100)
    contrasenaTemporal = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.nombre