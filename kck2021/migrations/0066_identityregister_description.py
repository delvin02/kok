# Generated by Django 4.2 on 2024-02-17 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kck2021', '0065_alter_identityregister_reference_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='identityregister',
            name='description',
            field=models.TextField(default='Belum disemak'),
        ),
    ]
