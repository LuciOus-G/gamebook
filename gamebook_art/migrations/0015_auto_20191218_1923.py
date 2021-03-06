# -*- coding: utf-8 -*-
# Generated by Django 1.11.25 on 2019-12-18 19:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gamebook_art', '0014_auto_20191103_1754'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gamebook_art',
            name='Gdrive1',
            field=models.URLField(blank=True, default='', max_length=1000),
        ),
        migrations.AlterField(
            model_name='gamebook_art',
            name='Gdrive2',
            field=models.URLField(blank=True, default='', max_length=1000),
        ),
        migrations.AlterField(
            model_name='gamebook_art',
            name='Video_url',
            field=models.URLField(blank=True, default='', max_length=1000),
        ),
        migrations.AlterField(
            model_name='gamebook_art',
            name='slug',
            field=models.SlugField(blank=True, editable=False, max_length=255),
        ),
    ]
