# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-16 18:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pkmn_app', '0003_pokemon_posted'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='subcategory',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]