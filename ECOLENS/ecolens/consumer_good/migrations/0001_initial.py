# Generated by Django 4.2.15 on 2024-08-20 15:32

import consumer_good.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ConsumerGood',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('clothing', models.FloatField(default=0, help_text='Amount in USD,e.g.,1000', validators=[consumer_good.models.validate_min])),
                ('appliances', models.FloatField(default=0, help_text='Amount in USD,e.g.,1000', validators=[consumer_good.models.validate_min])),
                ('pharmaceuticals', models.FloatField(default=0, help_text='Amount in USD,e.g.,1000', validators=[consumer_good.models.validate_min])),
                ('furniture', models.FloatField(default=0, help_text='Amount in USD,e.g.,1000', validators=[consumer_good.models.validate_min])),
                ('hospitality', models.FloatField(default=0, help_text='Amount in USD,e.g.,1000', validators=[consumer_good.models.validate_min])),
                ('services', models.FloatField(default=0, help_text='Amount in USD,e.g.,1000', validators=[consumer_good.models.validate_min])),
                ('consumption_unit', models.CharField(choices=[('tCO2equ', 'Tons of Carbon Dioxide Equvalant'), ('tCO2equ/USD', 'equivalent carbon units per dollar')], default='tCO2equ/USD', max_length=13)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('clothing_emission', models.FloatField(default=0)),
                ('appliances_emission', models.FloatField(default=0)),
                ('pharmaceuticals_emission', models.FloatField(default=0)),
                ('furniture_emission', models.FloatField(default=0)),
                ('hospitality_emission', models.FloatField(default=0)),
                ('services_emission', models.FloatField(default=0)),
                ('consumer_good_emission', models.FloatField(default=0)),
                ('emission_unit', models.CharField(choices=[('tCO2equ', 'Tons of Carbon Dioxide Equvalant'), ('tCO2equ/USD', 'equivalent carbon units per dollar')], default='tCO2equ', max_length=13)),
            ],
        ),
    ]
