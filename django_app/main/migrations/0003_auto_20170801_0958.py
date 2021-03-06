# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-08-01 00:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20170801_0041'),
    ]

    operations = [
        migrations.CreateModel(
            name='PartnerFAQ',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=50, verbose_name='question')),
                ('answer', models.CharField(max_length=50, verbose_name='answer')),
                ('my_order', models.PositiveIntegerField(default=0, verbose_name='my_order')),
            ],
            options={
                'verbose_name_plural': 'PartnerFAQs',
                'ordering': ['my_order'],
                'verbose_name': 'PartnerFAQ',
            },
        ),
        migrations.CreateModel(
            name='TenantFAQ',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=50, verbose_name='question')),
                ('answer', models.CharField(max_length=50, verbose_name='answer')),
                ('my_order', models.PositiveIntegerField(default=0, verbose_name='my_order')),
            ],
            options={
                'verbose_name_plural': 'TenantFAQs',
                'ordering': ['my_order'],
                'verbose_name': 'TenantFAQ',
            },
        ),
        migrations.AlterField(
            model_name='news',
            name='my_order',
            field=models.PositiveIntegerField(default=0, verbose_name='my_order'),
        ),
    ]
