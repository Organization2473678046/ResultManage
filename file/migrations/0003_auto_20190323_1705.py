# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-03-23 17:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('file', '0002_auto_20190323_1554'),
    ]

    operations = [
        migrations.AddField(
            model_name='filepath',
            name='createtime',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='\u521b\u5efa\u65f6\u95f4'),
        ),
        migrations.AddField(
            model_name='filepath',
            name='updatetime',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='\u66f4\u65b0\u65f6\u95f4'),
        ),
    ]
