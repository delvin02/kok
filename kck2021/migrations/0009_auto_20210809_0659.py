# Generated by Django 3.2.4 on 2021-08-09 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kck2021', '0008_auto_20210808_1441'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField()),
                ('thumbnail', models.ImageField(upload_to='static/img/blog/')),
                ('month', models.CharField(max_length=10)),
                ('day', models.PositiveIntegerField()),
                ('author', models.CharField(default='False', max_length=255)),
                ('intro', models.TextField()),
                ('body', models.TextField()),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-date_added'],
            },
        ),
        migrations.CreateModel(
            name='ArticleCategories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=60)),
            ],
            options={
                'ordering': ['category'],
            },
        ),
        migrations.DeleteModel(
            name='Post',
        ),
        migrations.AddField(
            model_name='article',
            name='categories',
            field=models.ManyToManyField(related_name='articleCategories', to='kck2021.ArticleCategories'),
        ),
    ]
