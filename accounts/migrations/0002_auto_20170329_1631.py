# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-29 16:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accounts',
            name='events',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='cal.Events'),
        ),
        migrations.AlterField(
            model_name='accounts',
            name='friends',
            field=models.ManyToManyField(null=True, related_name='_accounts_friends_+', to='accounts.Accounts'),
        ),
        migrations.AlterField(
            model_name='accounts',
            name='username',
            field=models.CharField(max_length=254, null=True),
        ),
    ]
