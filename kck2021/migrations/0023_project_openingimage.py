# Generated by Django 3.2.4 on 2021-08-16 15:09

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('kck2021', '0022_auto_20210816_2301'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='openingImage',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='media'),
            preserve_default=False,
        ),
    ]
