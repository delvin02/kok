# Generated by Django 3.2.4 on 2021-08-16 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kck2021', '0018_auto_20210816_2245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='fifthImage',
            field=models.ImageField(upload_to='media/project'),
        ),
        migrations.AlterField(
            model_name='project',
            name='firstImage',
            field=models.ImageField(upload_to='media/project'),
        ),
        migrations.AlterField(
            model_name='project',
            name='fourthImage',
            field=models.ImageField(upload_to='media/project'),
        ),
        migrations.AlterField(
            model_name='project',
            name='secondImage',
            field=models.ImageField(upload_to='media/project'),
        ),
        migrations.AlterField(
            model_name='project',
            name='sixthImage',
            field=models.ImageField(upload_to='media/project'),
        ),
        migrations.AlterField(
            model_name='project',
            name='thirdImage',
            field=models.ImageField(upload_to='media/project'),
        ),
        migrations.AlterField(
            model_name='project',
            name='thumbnail',
            field=models.ImageField(upload_to='media/project'),
        ),
    ]