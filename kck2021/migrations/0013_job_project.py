# Generated by Django 3.2.4 on 2021-08-15 09:00

from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('kck2021', '0012_auto_20210812_1606'),
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('specialization', models.CharField(max_length=255)),
            ],
            options={
                'ordering': ['specialization'],
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('thumbnail', models.ImageField(upload_to='static/img/project/')),
                ('intro', tinymce.models.HTMLField()),
                ('slug', models.SlugField()),
                ('title', models.CharField(max_length=60)),
                ('mission', models.CharField(max_length=200)),
                ('location', models.CharField(max_length=100)),
                ('value', models.DecimalField(decimal_places=2, max_digits=3)),
                ('firstImage8x7', models.ImageField(upload_to='static/img/project/')),
                ('secondImage8x7', models.ImageField(upload_to='static/img/project/')),
                ('thirImage8x7', models.ImageField(upload_to='static/img/project/')),
                ('fourImage8x7', models.ImageField(upload_to='static/img/project/')),
                ('fifthImage8x7', models.ImageField(upload_to='static/img/project/')),
                ('sixthImage8x7', models.ImageField(upload_to='static/img/project/')),
                ('dateTime', models.DateTimeField(auto_now_add=True)),
                ('jobType', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kck2021.job')),
            ],
            options={
                'ordering': ['dateTime'],
            },
        ),
    ]