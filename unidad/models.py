from django.db import models

from materia.models import Materia

class Unidad(models.Model):
    nombre = models.CharField(max_length=45)
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE, related_name="unidades")

    def __str__(self):
        return self.nombre
