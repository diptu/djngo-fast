# Generated by Django 4.2.15 on 2024-08-18 07:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle_usages', '0002_vehicleusages_vehicle_emissions_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vehicleusages',
            old_name='vehicle_emissions',
            new_name='vehicle_footprint',
        ),
        migrations.RenameField(
            model_name='vehicleusages',
            old_name='vehicle_emissions_unit',
            new_name='vehicle_footprint_unit',
        ),
    ]
