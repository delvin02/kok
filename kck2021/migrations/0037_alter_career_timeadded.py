# Generated by Django 3.2.4 on 2021-08-25 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kck2021', '0036_alter_career_timeadded'),
    ]

    operations = [
        migrations.AlterField(
            model_name='career',
            name='timeAdded',
            field=models.DateTimeField(default=1629901839.952181),
        ),
    ]
