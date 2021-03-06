# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-19 15:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_rating_best_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='addres',
            field=models.CharField(default='', max_length=1000),
        ),
        migrations.AddField(
            model_name='place',
            name='phone',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AddField(
            model_name='rating',
            name='best_month',
            field=models.CharField(choices=[('jan', 'January'), ('feb', 'February'), ('mar', 'March'), ('apr', 'April'), ('may', 'May'), ('jun', 'June'), ('jul', 'July'), ('aug', 'August'), ('sept', 'September'), ('oct', 'October'), ('nov', 'November'), ('dec', 'Decemeber')], default='jan', max_length=12),
        ),
        migrations.AlterField(
            model_name='rating',
            name='best_time',
            field=models.CharField(choices=[('morning', 'Morning'), ('day', 'Day'), ('evening', 'Evening'), ('night', 'Night')], default='day', max_length=4),
        ),
    ]
