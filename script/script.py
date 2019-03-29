# -*- coding: utf-8 -*-
import sqlite3
import os
import shutil
import sys
import psycopg2
import time
from datetime import datetime

reload(sys)
sys.setdefaultencoding('utf8')

if not os.environ.get("DJANGO_SETTINGS_MODULE"):
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ResultManage.settings")
import django

django.setup()


def TimeStampToTime(timestamp):
    timeStruct = time.localtime(timestamp)
    return time.strftime('%Y-%m-%d %H:%M:%S', timeStruct)


def mysqlite(dir, dbname):
    conn = sqlite3.connect(dbname)
    cursor = conn.cursor()
    cursor.execute(
        'create table result (id INTEGER PRIMARY KEY NOT NULL, filepath varchar(5000), flag varchar(10),filesize FLOAT,createtime datetime,updatetime datetime)')
    # li = []
    for root, dirs, files in os.walk(dir, True):
        for name in files:
            path = os.path.join(root, name)
            createtime = TimeStampToTime(os.path.getctime(path))
            updatetime = TimeStampToTime(os.path.getmtime(path))
            filesize = round(os.path.getsize(path) / float(1024 * 1024), 2)
            print path
            row = (path, 0, filesize, createtime, updatetime)
            # cursor.execute("insert into result values (?,?)", row)
            cursor.execute("insert into result (filepath, flag,filesize,createtime,updatetime) values (?,?,?,?,?)", row)
        for name in dirs:
            path = os.path.join(root, name)
            createtime = TimeStampToTime(os.path.getctime(path))
            updatetime = TimeStampToTime(os.path.getmtime(path))
            filesize = 0.0
            row = (path, 0, filesize, createtime, updatetime)
            # cursor.execute("insert into result  values (?,?)", row)
            cursor.execute("insert into result (filepath, flag,filesize,createtime,updatetime) values (?,?,?,?,?)", row)

    cursor.close()
    conn.commit()
    conn.close()
    print dbname, u"扫描完成"
    return True


if __name__ == '__main__':
    mysqlite(u'\\\\192.168.3.120\\新建文件夹\\120转180所需安装包',
             u"D:\\PycharmProjects\\ResultManage\\v0.2\\ResultManage\\中国9.db")
    pass
