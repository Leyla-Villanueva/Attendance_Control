from django.db import models

class Materia(models.Model):
    id_materia = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    unidad = models.IntegerField()

    def __str__(self):
        return self.nombre