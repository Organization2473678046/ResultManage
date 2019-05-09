# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-05-07 12:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('results', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EchartReceiveTime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sendouttime', models.CharField(blank=True, max_length=128, null=True, verbose_name='创建时间')),
                ('count', models.IntegerField(blank=True, null=True, verbose_name='数量')),
            ],
            options={
                'verbose_name': '发出日期Echart',
                'verbose_name_plural': '发出日期Echart',
            },
        ),
        migrations.CreateModel(
            name='EchartReceiveunit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('receiveunit', models.CharField(blank=True, max_length=128, null=True, verbose_name='接收单位')),
                ('count', models.IntegerField(blank=True, null=True, verbose_name='数量')),
            ],
            options={
                'verbose_name': '接收单位Echart',
                'verbose_name_plural': '接收单位Echart',
            },
        ),
    ]
