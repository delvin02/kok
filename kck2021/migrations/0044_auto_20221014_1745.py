# Generated by Django 3.2.4 on 2022-10-14 09:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('kck2021', '0043_alter_career_timeadded'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(null=True, upload_to='project/')),
            ],
        ),
        migrations.AddField(
            model_name='project',
            name='ProjectImages',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='projectImages', to='kck2021.projectimages'),
        ),
    ]