# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-07-30 13:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('house', '0008_auto_20170730_2226'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='room',
            options={'ordering': ['position'], 'verbose_name': 'Room', 'verbose_name_plural': 'Rooms'},
        ),
        migrations.RemoveField(
            model_name='room',
            name='sort_score',
        ),
        migrations.AddField(
            model_name='room',
            name='position',
            field=models.PositiveSmallIntegerField(null=True, verbose_name='Position'),
        ),
    ]
