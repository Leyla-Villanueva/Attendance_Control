from django.apps import AppConfig


class GrupoConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "grupo"

    def ready(self):
        import grupo.signals  # Importa las señales al iniciar la aplicación
