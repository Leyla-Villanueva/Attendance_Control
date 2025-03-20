from django.db import models

class Rol(models.Model):
    id = models.AutoField(primary_key=True)
    rol = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nombre
