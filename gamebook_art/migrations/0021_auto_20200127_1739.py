# -*- coding: utf-8 -*-
# Generated by Django 1.11.25 on 2020-01-27 17:39
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gamebook_art', '0020_auto_20200127_1735'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gamebook_art',
            name='slug',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
