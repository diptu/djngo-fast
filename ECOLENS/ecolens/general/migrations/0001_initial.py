# Generated by Django 4.2.15 on 2024-09-05 16:47

from django.db import migrations, models
import ecolens.custom_validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='General',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('num_people', models.IntegerField(default=1, help_text='Amount in USD,e.g.,2', validators=[ecolens.custom_validators.validate_min])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
