# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-11 00:50
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('pkmn_app', '0002_auto_20160310_2318'),
    ]

    operations = [
        migrations.AddField(
            model_name='pokemon',
            name='posted',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2016, 3, 11, 0, 50, 51, 199491, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
