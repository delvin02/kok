# Generated by Django 3.2.4 on 2021-08-25 14:07

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('kck2021', '0032_remove_career_timeadded'),
    ]

    operations = [
        migrations.AddField(
            model_name='career',
            name='timeAdded',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]