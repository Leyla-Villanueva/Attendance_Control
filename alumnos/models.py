from django.db import models

from carrera.models import Carrera
from grupo.models import Grupo
from users.models import User

class Alumno(models.Model):
    id = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    grupo = models.ForeignKey(Grupo, null=True, blank=True, on_delete=models.SET_NULL)
    grado = models.CharField(max_length=2)
    carrera_id = models.ForeignKey(Carrera, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f"{self.id_alumno.username} - {self.grado}"
