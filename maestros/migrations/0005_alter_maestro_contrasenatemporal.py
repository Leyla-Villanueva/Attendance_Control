# Generated by Django 5.1.5 on 2025-03-23 05:47

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