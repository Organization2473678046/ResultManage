#!/opt/rh/rh-python36/root/usr/bin/python3
# -*- coding:utf-8 -*-

# BORKER_URL='amqp://admin:Lantucx2018@localhost:5672/admin-vhost'
BROKER_URL = 'amqp://guest:guest@localhost:5672//'

CELERY_RESULT_BACKEND = 'amqp://'

CELERY_TIMEZONE = 'Asia/Shanghai'
CELERY_ENABLE_UTC = True


CELERY_QUEUES = {
    'genarate_docx': {
        'exchange': 'genarate_docx',
        'exchange_type': 'direct',
        'binding_key': 'genarate_docx'
    },
    'other_tasks': {
        'exchange': 'other_tasks',
        'exchange_type': 'direct',
        'binding_key': 'other_tasks'
    }
}

CELERY_DEFAULT_QUEUE = 'genarate_docx'

CELERY_IMPORTS = (
    'celery_app.generate_file',
    'celery_app.upload_doc',
)

# 防止死锁
CELERY_FORCE_EXECV = True

# 允许重试
CELERY_ACKS_LATE = True

# 设置并发worker数量
CELERY_CONCURRENCY = 2

# 每个worker最多执行100个任务被销毁
CELERY_MAX_TASKS_PER_CHILD = 100
