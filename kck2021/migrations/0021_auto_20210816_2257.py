# Generated by Django 3.2.4 on 2021-08-16 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kck2021', '0020_auto_20210816_2255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='fifthImage',
            field=models.ImageField(blank=True, upload_to='media/project/'),
        ),
        migrations.AlterField(
            model_name='project',
            name='firstImage',
            field=models.ImageField(blank=True, upload_to='media/project/'),
        ),
        migrations.AlterField(
            model_name='project',
            name='fourthImage',
            field=models.ImageField(blank=True, upload_to='media/project/'),
        ),
        migrations.AlterField(
            model_name='project',
            name='secondImage',
            field=models.ImageField(blank=True, upload_to='media/project/'),
        ),
        migrations.AlterField(
            model_name='project',
            name='sixthImage',
            field=models.ImageField(blank=True, upload_to='media/project/'),
        ),
        migrations.AlterField(
            model_name='project',
            name='thirdImage',
            field=models.ImageField(blank=True, upload_to='media/project/'),
        ),
    ]