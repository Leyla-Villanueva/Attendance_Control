from django.db.models.signals import post_migrate
from django.dispatch import receiver
from django.contrib.auth.hashers import make_password
from rol.models import Rol
from users.models import User
from admin_panel.models import Admin


@receiver(post_migrate)
def create_roles_and_admin(sender, **kwargs):
    if sender.name == "users":
        # Crear roles
        roles = ["admin", "maestro", "alumno"]
        for role in roles:
            Rol.objects.get_or_create(rol=role)

        # Crear usuario admin
        admin_role = Rol.objects.get(rol="admin")
        user, created = User.objects.get_or_create(
            username="admin",
            defaults={
                "password": make_password(
                    "contrasenaAdmin"
                ),  # Cambia la contraseña según sea necesario
                "rol": admin_role,
                "token": None,
            },
        )

        # Crear instancia de Admin si el usuario fue creado
        if created:
            Admin.objects.create(id_admin=user, nombre="Admin")
