# Generated by Django 4.2 on 2023-12-18 12:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('kck2021', '0061_alter_legal_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='legal',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='legal_category', to='kck2021.legalcategory'),
        ),
    ]
