# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-05-14 03:05
from __future__ import unicode_literals

from django.db import migrations, models
import results.models


class Migration(migrations.Migration):

    dependencies = [
        ('results', '0006_auto_20190513_1003'),
    ]

    operations = [
        migrations.CreateModel(
            name='UploadDoc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(blank=True, max_length=5000, null=True, upload_to=results.models.user_directory_path, verbose_name='分发单文件路径')),
                ('handoutlist_uniquenum', models.CharField(max_length=5000, verbose_name='分发单唯一编号')),
                ('createtime', models.DateTimeField(auto_now_add=True, null=True, verbose_name='创建时间')),
                ('updatetime', models.DateTimeField(auto_now=True, null=True, verbose_name='更新时间')),
            ],
            options={
                'verbose_name': '分发单文件',
                'verbose_name_plural': '分发单文件',
            },
        ),
    ]
