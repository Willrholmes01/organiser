# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-13 19:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cal', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='events',
            name='start_date',
            field=models.DateField(blank=True),
        ),
    ]
