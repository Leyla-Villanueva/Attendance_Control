# Generated by Django 5.1.4 on 2025-03-20 05:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('maestros', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='maestro',
            old_name='id_maestro',
            new_name='id',
        ),
    ]
