# Generated by Django 3.2.4 on 2022-10-14 09:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kck2021', '0044_auto_20221014_1745'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='ProjectImages',
            new_name='photos',
        ),
    ]