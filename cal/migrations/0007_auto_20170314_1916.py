# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-14 19:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('cal', '0006_auto_20170314_1915'),
    ]

    operations = [
        migrations.AlterField(
            model_name='events',
            name='start_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
