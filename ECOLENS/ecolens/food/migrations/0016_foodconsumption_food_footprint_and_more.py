# Generated by Django 4.2.15 on 2024-08-16 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0015_foodconsumption_level_of_wastage_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='foodconsumption',
            name='food_footprint',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='foodconsumption',
            name='food_footprint_unit',
            field=models.CharField(choices=[('tCO2equ', 'Tons of Carbon Dioxide Equvalant')], default='tCO2equ', max_length=10),
        ),
        migrations.AddField(
            model_name='foodconsumption',
            name='wastage_emission_unit',
            field=models.CharField(choices=[('tCO2equ', 'Tons of Carbon Dioxide Equvalant')], default='tCO2equ', max_length=10),
        ),
    ]
