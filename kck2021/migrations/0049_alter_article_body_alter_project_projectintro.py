# Generated by Django 4.2 on 2023-05-23 13:49

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kck2021', '0048_remove_project_photos_alter_projectimage_images_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='body',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
        migrations.AlterField(
            model_name='project',
            name='projectIntro',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]