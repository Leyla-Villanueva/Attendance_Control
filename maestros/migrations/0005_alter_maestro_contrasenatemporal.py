<<<<<<< HEAD
# Generated by Django 5.1.4 on 2025-03-23 22:18
=======
# Generated by Django 5.1.5 on 2025-03-23 05:47
>>>>>>> Ana-Jatz

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maestros', '0004_maestro_contrasenatemporal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maestro',
            name='contrasenaTemporal',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
