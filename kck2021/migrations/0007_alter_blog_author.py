# Generated by Django 3.2.4 on 2021-08-08 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kck2021', '0006_auto_20210808_1410'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='author',
            field=models.CharField(default='False', max_length=255),
        ),
    ]