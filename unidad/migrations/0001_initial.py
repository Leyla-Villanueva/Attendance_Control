# Generated by Django 5.1.4 on 2025-04-23 04:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('materia', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Unidad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('fecha_inicio', models.DateField(blank=True, null=True)),
                ('fecha_fin', models.DateField(blank=True, null=True)),
                ('materia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='unidades', to='materia.materia')),
            ],
        ),
    ]
