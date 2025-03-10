from django.db import models
from alumnos.models import Alumno
from clase.models import Clase

class Asistencia(models.Model):
    id = models.AutoField(primary_key=True)
    alumno_id = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    clase_id = models.ForeignKey(Clase, on_delete=models.CASCADE)
    fecha = models.DateField()
    estado_id = models.IntegerField()
    estado_asistencia = models.CharField(max_length=1, null=True, blank=True)

    def __str__(self):
        return f"Asistencia {self.id} - {self.alumno} - {self.clase}"
