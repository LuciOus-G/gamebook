# -*- coding: utf-8 -*-
# Generated by Django 1.11.25 on 2020-01-27 19:52
from __future__ import unicode_literals

from django.db import migrations
import tinymce_4.fields


class Migration(migrations.Migration):

    dependencies = [
        ('gamebook_art', '0026_auto_20200127_1938'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gamebook_art',
            name='body',
            field=tinymce_4.fields.TinyMCEModelField(verbose_name='Foo content'),
        ),
    ]
