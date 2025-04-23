from django.db import models
from carrera.models import Carrera


class Grupo(models.Model):
    id = models.AutoField(primary_key=True, null=False)
    nombre = models.CharField(max_length=50, null=False)
    grado = models.CharField(max_length=50, null=False)
    carrera = models.ForeignKey(
        Carrera, on_delete=models.SET_NULL, null=True, blank=True, related_name="grupos"
    )  # Relación con el modelo Carrera

    def __str__(self):
        return self.nombre
