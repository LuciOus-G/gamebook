# -*- coding: utf-8 -*-
# Generated by Django 1.11.25 on 2019-10-31 15:41
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gamebook_art', '0009_auto_20191031_2340'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gamebook_art',
            name='number',
        ),
    ]
