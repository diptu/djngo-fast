# Generated by Django 4.2.14 on 2024-08-05 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle_usages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicleusages',
            name='public_transit_distance',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='vehicleusages',
            name='transit_unit',
            field=models.CharField(choices=[('Km', 'Kilometer'), ('Mi', 'Mile')], default='Km', max_length=2),
        ),
        migrations.AlterField(
            model_name='vehicleusages',
            name='flight_unit',
            field=models.CharField(choices=[('Km', 'Kilometer'), ('Mi', 'Mile')], default='Km', max_length=2),
        ),
    ]
