# Generated by Django 4.2 on 2024-02-18 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kck2021', '0070_alter_identityregister_back_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='identityregister',
            name='reference_code',
            field=models.CharField(editable=False, max_length=20, unique=True),
        ),
    ]