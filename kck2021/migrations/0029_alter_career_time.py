# Generated by Django 3.2.4 on 2021-08-25 08:55

from django.db import migrations
import unixtimestampfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('kck2021', '0028_auto_20210825_1642'),
    ]

    operations = [
        migrations.AlterField(
            model_name='career',
            name='time',
            field=unixtimestampfield.fields.UnixTimeStampField(auto_now_add=True),
        ),
    ]
