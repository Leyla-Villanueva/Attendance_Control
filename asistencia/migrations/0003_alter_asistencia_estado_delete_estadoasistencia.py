# Generated by Django 5.1.5 on 2025-04-03 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asistencia', '0002_estadoasistencia_rename_alumno_id_asistencia_alumno_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asistencia',
            name='estado',
            field=models.BooleanField(default=False),
        ),
        migrations.DeleteModel(
            name='EstadoAsistencia',
        ),
    ]
