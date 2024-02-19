# Generated by Django 4.2 on 2024-02-17 15:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('kck2021', '0068_alter_identityregister_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='IdentityRegisterChangeLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('identity_register', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kck2021.identityregister')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-timestamp'],
            },
        ),
    ]