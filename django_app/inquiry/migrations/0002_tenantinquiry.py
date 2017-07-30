# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-07-30 17:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('house', '0010_auto_20170730_2302'),
        ('inquiry', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TenantInquiry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='생성일')),
                ('modified_date', models.DateTimeField(auto_now=True, verbose_name='수정일')),
                ('name', models.CharField(max_length=20, verbose_name='name')),
                ('sex', models.CharField(choices=[('man', 'man'), ('woman', 'woman')], max_length=20, verbose_name='sex')),
                ('phone_number', models.CharField(max_length=20, verbose_name='phone number1')),
                ('email', models.EmailField(blank=True, max_length=100, null=True, verbose_name='email')),
                ('moving_date', models.DateField(verbose_name='moving date')),
                ('memo', models.TextField(blank=True, null=True, verbose_name='memo')),
                ('is_tenant', models.BooleanField(default=False, verbose_name='is tenant')),
                ('house', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='house.House', verbose_name='house')),
                ('room', smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='house', chained_model_field='house', null=True, on_delete=django.db.models.deletion.CASCADE, to='house.Room', verbose_name='room')),
            ],
            options={
                'verbose_name_plural': 'Tenant inquiries',
                'verbose_name': 'Tenant inquiry',
            },
        ),
    ]