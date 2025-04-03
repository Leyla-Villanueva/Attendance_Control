from django.db.models.signals import pre_delete
from django.dispatch import receiver
from .models import Grupo
from alumnos.models import Alumno


@receiver(pre_delete, sender=Grupo)
def actualizar_alumnos_al_eliminar_grupo(sender, instance, **kwargs):
    """
    Esta señal se ejecuta antes de eliminar un grupo.
    Actualiza los alumnos relacionados con el grupo eliminado,
    estableciendo los campos grado y carrera_id en null.
    """
    print(
        f"Señal activada: Grupo a eliminar - ID: {instance.id}, Nombre: {instance.nombre}"
    )

    # Obtener los alumnos relacionados antes de que el grupo sea eliminado
    alumnos = Alumno.objects.filter(grupo_id=instance.id)
    print(
        f"Alumnos relacionados antes de actualizar: {list(alumnos.values('id_id', 'grado', 'carrera_id_id', 'grupo_id'))}"
    )

    # Actualizar los campos de los alumnos relacionados
    alumnos_actualizados = alumnos.update(grado=None, carrera_id_id=None)
    print(f"Alumnos actualizados: {alumnos_actualizados}")

    # Verificar los valores después de la actualización
    print(
        f"Alumnos después de actualizar: {list(alumnos.values('id_id', 'grado', 'carrera_id_id', 'grupo_id'))}"
    )
