# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-15 20:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20180315_2358'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rating',
            name='total',
        ),
        migrations.AddField(
            model_name='rating',
            name='budget',
            field=models.IntegerField(default=300),
        ),
    ]
