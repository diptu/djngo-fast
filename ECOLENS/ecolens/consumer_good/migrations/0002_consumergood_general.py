# Generated by Django 4.2.15 on 2024-08-20 15:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0001_initial'),
        ('consumer_good', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='consumergood',
            name='general',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='general.general'),
            preserve_default=False,
        ),
    ]
