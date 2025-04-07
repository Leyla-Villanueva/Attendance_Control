from django.db import models
from django.core.exceptions import ValidationError

class Unidad(models.Model):
    nombre = models.CharField(max_length=100)
    fecha_inicio = models.DateField(null=True, blank=True)
    fecha_fin = models.DateField(null=True, blank=True)  
    materia = models.ForeignKey( 
        "materia.Materia", on_delete=models.CASCADE, related_name="unidades"
    )

    def __str__(self):
        return self.nombre

    # Validación: asegurarse de que la fecha de fin sea posterior a la de inicio
    def clean(self):
        if self.fecha_fin < self.fecha_inicio:
            raise ValidationError("La fecha de fin no puede ser anterior a la de inicio.")




""" from django.db import models
from datetime import date


class Unidad(models.Model):
    nombre = models.CharField(max_length=45)
    materia = models.ForeignKey( 
        "materia.Materia", on_delete=models.CASCADE, related_name="unidades"
    )


    def __str__(self):
        return self.nombre """
