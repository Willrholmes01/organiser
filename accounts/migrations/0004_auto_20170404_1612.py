# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-04 16:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20170404_1612'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accounts',
            name='friends',
            field=models.ManyToManyField(related_name='_accounts_friends_+', to='accounts.Accounts'),
        ),
    ]
