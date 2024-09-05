# Generated by Django 4.2.15 on 2024-09-05 16:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('other', '0001_initial'),
        ('consumer_good', '0001_initial'),
        ('vehicle_usages', '0001_initial'),
        ('food', '0001_initial'),
        ('household', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Emission',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('resedential_emission', models.FloatField(default=0)),
                ('business_emission', models.FloatField(default=0)),
                ('total_emission', models.FloatField(default=0)),
                ('unit', models.CharField(choices=[('tCO2', 'Tons of Carbon Dioxide')], default='tCO2', max_length=10)),
                ('consumer_good', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='consumer_good.consumergood')),
                ('food_consumption', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='food.foodconsumption')),
                ('household_usages', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='household.householdusages')),
                ('other_uages', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='other.otherusages')),
                ('vehicle_usages', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vehicle_usages.vehicleusages')),
            ],
        ),
    ]
