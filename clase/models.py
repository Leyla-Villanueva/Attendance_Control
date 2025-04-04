from django.db import models
from materia.models import Materia
from grupo.models import Grupo
from maestros.models import Maestro

class Clase(models.Model):
    id = models.AutoField(primary_key=True)
    maestro_id = models.ForeignKey(Maestro, on_delete=models.CASCADE)
    materia_id = models.ForeignKey(Materia, on_delete=models.CASCADE)
    periodo = models.CharField(max_length=50)
    grupo_id = models.ForeignKey(Grupo, on_delete=models.CASCADE)
    dia_clase = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f"{self.materia_id.nombre} - {self.periodo}"
