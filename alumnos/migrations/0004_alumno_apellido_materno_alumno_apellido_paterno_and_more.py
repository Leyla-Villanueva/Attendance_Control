# Generated by Django 5.1.4 on 2025-03-22 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alumnos', '0003_rename_id_alumno_alumno_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='alumno',
            name='apellido_materno',
            field=models.CharField(default='N/A', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='alumno',
            name='apellido_paterno',
            field=models.CharField(default='N/A', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='alumno',
            name='nombre',
            field=models.CharField(default='N/A', max_length=100),
            preserve_default=False,
        ),
    ]
