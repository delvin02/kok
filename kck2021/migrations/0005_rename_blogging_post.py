# Generated by Django 3.2.4 on 2021-08-08 14:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kck2021', '0004_auto_20210808_1405'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Blogging',
            new_name='Post',
        ),
    ]