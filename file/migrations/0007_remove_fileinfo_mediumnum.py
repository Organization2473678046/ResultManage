# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-03-25 14:55
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('file', '0006_auto_20190325_1437'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fileinfo',
            name='mediumnum',
        ),
    ]
