#!C:/Python27/ArcGIS10.2/python.exe
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import sys
import os
import psycopg2
import time

if not os.environ.get("DJANGO_SETTINGS_MODULE"):
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ResultManage.settings")
import django

django.setup()
from file.models import ResultFile

reload(sys)
sys.setdefaultencoding('utf8')


def conn_database(file_midir):
    conn = psycopg2.connect(dbname=u"resultmanage",
                            user=u"postgres",
                            password=u"Lantucx2018",
                            host=u"localhost",
                            port=u"5432")
    cur = conn.cursor()
    ergodic(file_midir, cur)
    conn.commit()
    conn.close()


def ergodic(file_midir, cur):
    file_list_01 = os.listdir(file_midir)
    for file in file_list_01:
        path = file_midir + "/" + file
        if os.path.isdir(path):
            ergodic(path, cur)
        elif os.path.isfile(path):
            SQL = "INSERT INTO file_resultfile (file_path, server_allow) VALUES ('%s', 'C:/')" % (path)
            cur.execute(SQL)
            print "文件：%s" % path
        else:
            SQL = "INSERT INTO file_resultfile (file_path, server_allow) VALUES ('%s', 'C:/')" % (path)
            print SQL
            cur.execute(SQL)
            print "这是个神秘的文件：%s" % path



def ergodic02(file_midir):
    file_list_01 = os.listdir(file_midir)
    for file in file_list_01:
        path = file_midir + "/" + file
        if os.path.isdir(path):
            ergodic02(path)
        elif os.path.isfile(path):
            ResultFile.objects.create(filepath=path, serverIP="192.168.3.120")
            print path
        else:
            ResultFile.objects.create(filepath=path, serverIP="192.168.3.120")
            print path


def test_walk(file_midir):
    for root, dirs, files in os.walk(file_midir):
        for file in files:
            ResultFile.objects.create(filepath=root +"/" + file, serverIP="192.168.3.120")
            print root +"\\" + file



def main():
    file_midir = "\\\\192.168.3.120\\新建文件夹"
    # file_midir = "192.168.3.120\新建文件夹\成果管理系统测试文件夹"
    # file_midir = "E:/"

    # ergodic02(file_midir)
    test_walk(file_midir)


if __name__ == '__main__':
    start = time.time()

    main()

    end = time.time()
    print end - start

