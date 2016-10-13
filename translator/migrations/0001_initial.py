# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-12 23:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Translation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entered_text', models.TextField()),
                ('language', models.TextField()),
                ('translated_text', models.TextField()),
                ('session', models.CharField(max_length=40)),
            ],
        ),
    ]