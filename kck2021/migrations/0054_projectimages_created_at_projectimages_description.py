# Generated by Django 4.2 on 2023-07-02 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kck2021', '0053_rename_projectimage_projectimages_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectimages',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='projectimages',
            name='description',
            field=models.CharField(default='ddd', max_length=100),
            preserve_default=False,
        ),
    ]
