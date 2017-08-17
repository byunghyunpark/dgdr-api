# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-08-17 02:17
from __future__ import unicode_literals

from django.db import migrations
import sortedm2m.fields
from sortedm2m.operations import AlterSortedManyToManyField


class Migration(migrations.Migration):

    dependencies = [
        ('house', '0016_auto_20170816_2248'),
    ]

    operations = [
        AlterSortedManyToManyField(
            model_name='house',
            name='search_tag',
            field=sortedm2m.fields.SortedManyToManyField(blank=True, help_text=None, to='house.SearchTag', verbose_name='tag'),
        ),
    ]
