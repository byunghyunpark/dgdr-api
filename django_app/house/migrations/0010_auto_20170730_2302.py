# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-07-30 14:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('house', '0009_auto_20170730_2235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='name',
            field=models.CharField(max_length=20, verbose_name='name'),
        ),
    ]
