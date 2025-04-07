from django.db import models
from alumnos.models import Alumno
from clase.models import Clase
from unidad.models import Unidad

""" class EstadoAsistencia(models.Model):
    nombre = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre """

class Asistencia(models.Model):
    id = models.AutoField(primary_key=True)
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    clase = models.ForeignKey(Clase, on_delete=models.CASCADE)
    unidad = models.ForeignKey(Unidad, on_delete=models.CASCADE, null=True, blank=True)  
    fecha = models.DateField()
    estado = models.BooleanField(default=False)
    #estado = models.ForeignKey(EstadoAsistencia, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"Asistencia {self.id} - {self.alumno} - {self.clase} - {self.unidad}"
