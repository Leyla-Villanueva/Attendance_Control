from django.db import models
from carrera.models import Carrera
from grupo.models import Grupo
from users.models import User
from django.db.models.signals import post_delete
from django.dispatch import receiver


class Alumno(models.Model):
    id = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido_paterno = models.CharField(max_length=100)
    apellido_materno = models.CharField(max_length=100)
    grupo = models.ForeignKey(
        Grupo, null=True, blank=True, on_delete=models.SET_NULL, related_name="alumnos"
    )
    grado = models.CharField(max_length=2, blank=True, null=True, default="")
    carrera = models.ForeignKey(
        Carrera, null=True, blank=True, on_delete=models.SET_NULL
    )
    contrasenaTemporal = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.id.username} - {self.grado}"


@receiver(post_delete, sender=Alumno)
def eliminar_usuario_asociado(sender, instance, **kwargs):
    if instance.id:
        instance.id.delete()
