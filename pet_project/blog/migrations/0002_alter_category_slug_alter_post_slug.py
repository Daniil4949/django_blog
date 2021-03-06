# Generated by Django 4.0.5 on 2022-07-14 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(blank=True, max_length=1000, null=True, unique=True, verbose_name='URL'),
        ),
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(blank=True, max_length=1000, null=True, unique=True, verbose_name='URL'),
        ),
    ]
