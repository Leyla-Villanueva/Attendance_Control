from django.db import models

from users.models import User

class Admin(models.Model):
    id = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre
