# Generated by Django 4.2.15 on 2024-08-18 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carbon_footprint', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='emission',
            name='business_emission',
            field=models.FloatField(default=0),
        ),
    ]
