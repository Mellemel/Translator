# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-13 10:57
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('translator', '0002_auto_20161012_2223'),
    ]

    operations = [
        migrations.RenameField(
            model_name='translations',
            old_name='entered_text',
            new_name='original_text',
        ),
    ]