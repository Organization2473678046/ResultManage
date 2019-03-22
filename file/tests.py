# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

# Create your tests here.
import os
import sys
import psycopg2
import time

reload(sys)
sys.setdefaultencoding('utf8')


if not os.environ.get("DJANGO_SETTINGS_MODULE"):
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ResultManage.settings")
import django

django.setup()
from file.models import ResultFile

if __name__ == '__main__':

    result = ResultFile.objects.filter(filepath=None)
    print result



