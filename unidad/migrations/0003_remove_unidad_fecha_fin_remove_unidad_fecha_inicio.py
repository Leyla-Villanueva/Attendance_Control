# Generated by Django 5.1.4 on 2025-03-31 04:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('unidad', '0002_unidad_fecha_fin_unidad_fecha_inicio'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='unidad',
            name='fecha_fin',
        ),
        migrations.RemoveField(
            model_name='unidad',
            name='fecha_inicio',
        ),
    ]
