# Generated by Django 3.2.4 on 2021-08-25 22:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kck2021', '0038_auto_20210825_2233'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='career',
            name='last_updated_on',
        ),
        migrations.AlterField(
            model_name='career',
            name='timeAdded',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 25, 22, 36, 13, 14185)),
        ),
    ]
