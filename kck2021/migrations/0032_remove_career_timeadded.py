# Generated by Django 3.2.4 on 2021-08-25 14:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kck2021', '0031_alter_career_timeadded'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='career',
            name='timeAdded',
        ),
    ]
