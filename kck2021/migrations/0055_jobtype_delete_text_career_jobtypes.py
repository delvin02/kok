# Generated by Django 4.2 on 2023-12-17 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kck2021', '0054_projectimages_created_at_projectimages_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name='Text',
        ),
        migrations.AddField(
            model_name='career',
            name='jobTypes',
            field=models.ManyToManyField(blank=True, related_name='careers', to='kck2021.jobtype'),
        ),
    ]
