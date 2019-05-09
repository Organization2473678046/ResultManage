#!/opt/rh/rh-python36/root/usr/bin/python3
# -*- coding:utf-8 -*-
from celery import Celery

app = Celery('celery_generate_file')

# 通过Celery 实例来加载配置模块
app.config_from_object('celery_app.celeryconfig')

