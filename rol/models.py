from django.db import models

class Rol(models.Model):
    id_rol = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nombre
