# Generated by Django 3.2.4 on 2021-08-16 07:32

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('kck2021', '0014_auto_20210815_1714'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='introImage',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='static/img/project/'),
            preserve_default=False,
        ),
    ]
