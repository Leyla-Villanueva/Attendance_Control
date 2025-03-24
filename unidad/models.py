from django.db import models
from datetime import date


class Unidad(models.Model):
    nombre = models.CharField(max_length=45)
    materia = models.ForeignKey(
        "materia.Materia", on_delete=models.CASCADE, related_name="unidades"
    )
    fecha_inicio = models.DateField(default=date.today)
    fecha_fin = models.DateField(default=date.today)

    def __str__(self):
        return self.nombre
