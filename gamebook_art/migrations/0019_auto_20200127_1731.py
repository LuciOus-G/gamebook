# -*- coding: utf-8 -*-
# Generated by Django 1.11.25 on 2020-01-27 17:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gamebook_art', '0018_auto_20200127_1729'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gamebook_art',
            name='title',
            field=models.TextField(default=''),
        ),
    ]