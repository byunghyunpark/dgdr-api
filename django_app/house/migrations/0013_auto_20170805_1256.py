# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-08-05 03:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('house', '0012_auto_20170804_0946'),
    ]

    operations = [
        migrations.AlterField(
            model_name='house',
            name='status',
            field=models.CharField(choices=[('open', 'open'), ('close', 'close'), ('ready', 'ready')], default='ready', max_length=30, verbose_name='status'),
        ),
    ]
