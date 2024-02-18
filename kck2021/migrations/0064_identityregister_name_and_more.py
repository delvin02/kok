# Generated by Django 4.2 on 2024-02-17 13:51

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('kck2021', '0063_identityregister_alter_article_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='identityregister',
            name='name',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='identityregister',
            name='reference_code',
            field=models.UUIDField(default=uuid.uuid1, editable=False),
        ),
        migrations.AddField(
            model_name='identityregister',
            name='verified',
            field=models.BooleanField(default=False),
        ),
    ]
