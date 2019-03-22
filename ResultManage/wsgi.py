"""
WSGI config for ResultManage project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os
import sys

from django.core.wsgi import get_wsgi_application
sys.path.append('D:/PycharmProjects/ResultManage/v0.1/ResultManage')


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ResultManage.settings")

application = get_wsgi_application()
