# Generated by Django 5.0.6 on 2024-07-05 03:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_category_blog'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]
