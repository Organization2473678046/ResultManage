# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-03-23 15:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('file', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FileInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=5000, unique=True, verbose_name='\u6210\u679c\u8d44\u6599\u540d\u79f0')),
                ('type', models.CharField(max_length=5000, null=True, verbose_name='\u6210\u679c\u7c7b\u578b')),
                ('num', models.IntegerField(null=True, verbose_name='\u6210\u679c\u6570\u91cf')),
                ('datasize', models.CharField(max_length=1000, null=True, verbose_name='\u6210\u679c\u6570\u636e\u91cfGB')),
                ('mediumtype', models.CharField(max_length=1000, null=True, verbose_name='\u683c\u5f0f/\u4ecb\u8d28\u7c7b\u578b')),
                ('mediumnum', models.CharField(max_length=1000, null=True, verbose_name='\u4ecb\u8d28\u7f16\u53f7')),
                ('year', models.CharField(max_length=1000, null=True, verbose_name='\u6210\u679c\u5e74\u4ee3')),
                ('secretlevel', models.CharField(max_length=1000, null=True, verbose_name='\u6210\u679c\u79d8\u5bc6\u7ea7\u522b')),
                ('handoutlist_name', models.CharField(max_length=5000, verbose_name='\u6210\u679c\u6240\u5c5e\u6e05\u5355')),
                ('createtime', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('updatetime', models.DateTimeField(auto_now=True, verbose_name='\u66f4\u65b0\u65f6\u95f4')),
            ],
            options={
                'verbose_name': '\u6210\u679c\u8d44\u6599\u4fe1\u606f\u8868',
                'verbose_name_plural': '\u6210\u679c\u8d44\u6599\u4fe1\u606f\u8868',
            },
        ),
        migrations.CreateModel(
            name='FilePath',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filepath', models.TextField(null=True, verbose_name='\u6210\u679c\u6587\u4ef6\u8def\u5f84')),
                ('fileinfo_name', models.CharField(max_length=5000, null=True, verbose_name='\u6210\u679c\u8d44\u6599\u540d\u79f0')),
                ('handoutlist_name', models.CharField(max_length=5000, null=True, verbose_name='\u6210\u679c\u6240\u5c5e\u6e05\u5355')),
            ],
            options={
                'verbose_name': '\u6210\u679c\u6587\u4ef6\u8def\u5f84\u8868',
                'verbose_name_plural': '\u6210\u679c\u6587\u4ef6\u8def\u5f84\u8868',
            },
        ),
        migrations.CreateModel(
            name='HandOutList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=5000, verbose_name='\u6210\u679c\u4ea4\u4ed8\u6e05\u5355\u540d\u79f0')),
                ('listnum', models.CharField(max_length=1000, null=True, verbose_name='\u6e05\u5355\u53d7\u7406\u7f16\u53f7')),
                ('auditnum', models.CharField(max_length=1000, null=True, verbose_name='\u5ba1\u6838\u7f16\u53f7')),
                ('secretlevel', models.CharField(max_length=2000, null=True, verbose_name='\u6e05\u5355\u79d8\u5bc6\u7ea7\u522b')),
                ('purpose', models.CharField(max_length=2000, null=True, verbose_name='\u7528\u9014')),
                ('receiveunit', models.CharField(max_length=5000, null=True, verbose_name='\u63a5\u6536\u5355\u4f4d')),
                ('receiver', models.CharField(max_length=5000, null=True, verbose_name='\u63a5\u6536\u4eba')),
                ('receiverinfo', models.CharField(max_length=5000, null=True, verbose_name='\u63a5\u6536\u4eba\u8054\u7cfb\u65b9\u5f0f')),
                ('handovertime', models.DateTimeField(null=True, verbose_name='\u4ea4\u63a5\u65e5\u671f')),
                ('recievetime', models.DateTimeField(null=True, verbose_name='\u63a5\u6536\u65e5\u671f')),
                ('undertaker', models.CharField(max_length=1000, null=True, verbose_name='\u627f\u529e\u53c2\u8c0b')),
                ('deliveryway', models.CharField(max_length=2000, null=True, verbose_name='\u9012\u9001\u65b9\u5f0f')),
                ('handler', models.CharField(max_length=1000, null=True, verbose_name='\u6e05\u5355\u7ecf\u529e\u4eba')),
                ('createtime', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('updatetime', models.DateTimeField(auto_now=True, verbose_name='\u66f4\u65b0\u65f6\u95f4')),
            ],
            options={
                'verbose_name': '\u6210\u679c\u5206\u53d1\u6e05\u5355\u8868',
                'verbose_name_plural': '\u6210\u679c\u5206\u53d1\u6e05\u5355\u8868',
            },
        ),
        migrations.AlterModelOptions(
            name='resultfile',
            options={'verbose_name': '\u6210\u679c\u6587\u4ef6\u8def\u5f84', 'verbose_name_plural': '\u6210\u679c\u6587\u4ef6\u8def\u5f84'},
        ),
    ]
