# -*- coding: utf-8 -*-
# Generated by Django 1.11.25 on 2019-10-21 13:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gamebook_art', '0002_carousel'),
    ]

    operations = [
        migrations.AddField(
            model_name='carousel',
            name='slug',
            field=models.SlugField(default='default'),
        ),
        migrations.AddField(
            model_name='carousel',
            name='title',
            field=models.CharField(default='default', max_length=100),
        ),
    ]
