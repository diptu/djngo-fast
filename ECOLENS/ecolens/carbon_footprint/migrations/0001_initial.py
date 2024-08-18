# Generated by Django 4.2.15 on 2024-08-18 08:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('food', '0017_foodconsumption_consumption_unit_and_more'),
        ('household', '0001_initial'),
        ('vehicle_usages', '0003_rename_vehicle_emissions_vehicleusages_vehicle_footprint_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Emission',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('resedential_emission', models.FloatField(default=0)),
                ('unit', models.CharField(choices=[('tCO2', 'Tons of Carbon Dioxide')], default='tCO2', max_length=10)),
                ('food_consumption', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='food.foodconsumption')),
                ('household_usages', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='household.householdusages')),
                ('vehicle_usages', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vehicle_usages.vehicleusages')),
            ],
        ),
    ]
