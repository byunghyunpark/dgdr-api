# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-07-29 15:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import geoposition.fields
import smart_selects.db_fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('region', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='House',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='created date')),
                ('modified_date', models.DateTimeField(auto_now=True, verbose_name='modified_date')),
                ('name', models.CharField(max_length=30, verbose_name='name')),
                ('main_photo', models.ImageField(upload_to='house_main_photo', verbose_name='main photo')),
                ('introduction', models.TextField(verbose_name='introduction')),
                ('trading_area', models.CharField(max_length=50, verbose_name='trading area')),
                ('open_date', models.DateField(verbose_name='open date')),
                ('capacity', models.IntegerField(verbose_name='capacity')),
                ('category', models.CharField(max_length=30, verbose_name='category')),
                ('common_service', models.TextField(verbose_name='common service')),
                ('private_service', models.TextField(verbose_name='private service')),
                ('address', models.CharField(max_length=100, verbose_name='house address')),
                ('position', geoposition.fields.GeopositionField(max_length=42, verbose_name='position')),
                ('transportation', models.TextField(verbose_name='transportation')),
                ('accessibility', models.TextField(verbose_name='accessibility')),
                ('amenity', models.TextField(verbose_name='amenity')),
                ('sort_score', models.IntegerField(verbose_name='sort score')),
                ('city', smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='province', chained_model_field='province', null=True, on_delete=django.db.models.deletion.CASCADE, to='region.City', verbose_name='city')),
                ('province', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='region.Province')),
            ],
            options={
                'verbose_name': 'House',
                'verbose_name_plural': 'Houses',
            },
        ),
        migrations.CreateModel(
            name='SearchTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='name')),
            ],
            options={
                'verbose_name': 'Search tag',
                'verbose_name_plural': 'Search tags',
            },
        ),
        migrations.AddField(
            model_name='house',
            name='search_tag',
            field=models.ManyToManyField(to='house.SearchTag', verbose_name='tag'),
        ),
    ]