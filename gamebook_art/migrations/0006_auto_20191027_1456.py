# -*- coding: utf-8 -*-
# Generated by Django 1.11.25 on 2019-10-27 06:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gamebook_art', '0005_auto_20191022_2156'),
    ]

    operations = [
        migrations.AddField(
            model_name='gamebook_art',
            name='number',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='carousel',
            name='banners',
            field=models.ImageField(default='', upload_to='image'),
        ),
        migrations.AlterField(
            model_name='carousel',
            name='slug',
            field=models.SlugField(default=''),
        ),
        migrations.AlterField(
            model_name='carousel',
            name='title',
            field=models.CharField(default='', max_length=100),
        ),
    ]
