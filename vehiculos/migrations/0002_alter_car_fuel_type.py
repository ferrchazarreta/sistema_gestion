# Generated by Django 5.0.4 on 2024-11-06 01:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehiculos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='fuel_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fuels', to='vehiculos.fuel'),
        ),
    ]
