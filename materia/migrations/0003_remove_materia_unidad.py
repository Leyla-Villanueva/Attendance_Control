# Generated by Django 5.1.4 on 2025-03-24 03:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('materia', '0002_rename_id_materia_materia_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='materia',
            name='unidad',
        ),
    ]
