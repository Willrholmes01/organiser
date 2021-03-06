# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-13 19:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Events',
            fields=[
                ('title', models.CharField(max_length=250, primary_key=True, serialize=False)),
                ('start_date', models.DateField()),
                ('start_time', models.TimeField(blank=True)),
                ('end_date', models.DateField(default=models.TimeField(blank=True))),
                ('end_time', models.TimeField(blank=True)),
                ('created', models.DateTimeField(auto_now=True)),
                ('location', models.CharField(blank=True, max_length=250)),
                ('attendees', models.EmailField(blank=True, max_length=254)),
                ('private', models.BooleanField(default=False)),
                ('description', models.TextField(blank=True)),
            ],
        ),
    ]
