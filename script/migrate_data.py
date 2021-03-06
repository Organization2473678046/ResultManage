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

from file.models import ResultFile

'''把时间戳转化为时间: 1479264792 to 2016-11-16 10:53:12'''
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


def insert_data(dbname):
    conn = sqlite3.connect(dbname)
    cursor = conn.cursor()
    # 每次只能读取一条
    # count = 0
    # while True:
    #     cursor.execute(u"select * from result where flag='0'")
    #     data = cursor.fetchone()
    #     if data:
    #         count += 1
    #         print data
    #         filepath = data[1]
    #         dirlength = len(filepath)
    #         filepath_list = filepath.split("\\")
    #         dirdepth = len(filepath_list) - 2
    #         ResultFile.objects.create(filepath=filepath, dirlength=dirlength, dirdepth=dirdepth, filesize=data[3],filecreatetime=data[4], fileupdatetime=data[5])
    #         sql = u"update result set flag='1' where id=%d" % data[0]
    #         cursor.execute(sql)
    #         conn.commit()
    #     else:
    #         conn.close()
    #         break

    # 用orm插入
    count = 0
    while True:
        cursor.execute("select * from result where flag='0'")
        data_list = cursor.fetchmany(1000)
        if data_list:
            count += 1
            for data in data_list:
                print data
                filepath = data[1]
                # print filepath
                dirlength = len(filepath)
                filepath_list = filepath.split("\\")
                dirdepth = len(filepath_list) - 2
                ResultFile.objects.create(filepath=filepath, dirlength=dirlength, dirdepth=dirdepth, filesize=data[3],filecreatetime=data[4], fileupdatetime=data[5])
                sql = u"update result set flag='1' where id=%d" % data[0]
                cursor.execute(sql)
            # 每1000次提交一次
            conn.commit()
        else:
            conn.close()
            break

    print count
    # conn.close()
    print dbname, u"数据迁移完毕"
    return True


def main(old_dbdir, new_dbdir):
    dir_list = os.listdir(old_dbdir)
    for dir in dir_list:
        if dir.endswith(u".db"):
            dbname = os.path.join(old_dbdir, dir)
            res = insert_data(dbname)
            if res:
                shutil.move(dbname, new_dbdir)


if __name__ == '__main__':
    # mysqlite(u'\\\\192.168.3.120\\新建文件夹\\120转180所需安装包', u"D:\\PycharmProjects\\ResultManage\\v0.2\\ResultManage\\中国9.db")
    insert_data(u"D:\\PycharmProjects\\ResultManage\\v0.2\\ResultManage\\中国9.db")
    # main(u"D:\\PycharmProjects\\ResultManage\\v0.2\\ResultManage,u"D:\\PycharmProjects")

    pass
