# -*- coding: utf-8 -*-
import sqlite3
import os
import time
from datetime import datetime


def TimeStampToTime(timestamp):
    if timestamp < 0.0:
        timestamp = 0
    timeStruct = time.localtime(timestamp)
    return time.strftime('%Y-%m-%d %H:%M:%S', timeStruct)


def scan_dir(dir, dbdir, count):
    dbname = os.path.join(dbdir, "1.db")
    print(dbname)
    conn = sqlite3.connect(dbname)
    cursor = conn.cursor()
    cursor.execute(
        'create table result (id INTEGER PRIMARY KEY NOT NULL, filepath varchar(5000), flag varchar(10),filesize FLOAT,createtime datetime,updatetime datetime)')
    total_count = 0
    for root, dirs, files in os.walk(dir, True):
        for name in files:
            path = os.path.join(root, name)
            try:
                createtime = TimeStampToTime(os.path.getctime(path))
                updatetime = TimeStampToTime(os.path.getmtime(path))
                filesize = round(os.path.getsize(path) / float(1024 * 1024), 2)
            except:
                print(path)
                createtime = TimeStampToTime(-1)
                updatetime = TimeStampToTime(-1)
                filesize = 0
                row = (path, 0, filesize, createtime, updatetime)
                cursor.execute("insert into result (filepath, flag,filesize,createtime,updatetime) values (?,?,?,?,?)",
                               row)
                total_count += 1
            else:
                row = (path, 0, filesize, createtime, updatetime)
                cursor.execute("insert into result (filepath, flag,filesize,createtime,updatetime) values (?,?,?,?,?)",
                               row)
                total_count += 1

            if total_count % count == 0:
                cursor.close()
                conn.commit()
                conn.close()
                print(str(total_count / count) + ".db", "扫描完成")
                sqlite_name = str(total_count // count + 1) + ".db"
                dbname = os.path.join(dbdir, sqlite_name)
                conn = sqlite3.connect(dbname)
                cursor = conn.cursor()
                cursor.execute(
                    'create table result (id INTEGER PRIMARY KEY NOT NULL, filepath varchar(5000), flag varchar(10),filesize FLOAT,createtime datetime,updatetime datetime)')

        for name in dirs:
            path = os.path.join(root, name)
            try:
                createtime = TimeStampToTime(os.path.getctime(path))
                updatetime = TimeStampToTime(os.path.getmtime(path))
                filesize = 0
            except:
                print(path)
                createtime = TimeStampToTime(-1)
                updatetime = TimeStampToTime(-1)
                filesize = 0
                row = (path, 0, filesize, createtime, updatetime)
                cursor.execute("insert into result (filepath, flag,filesize,createtime,updatetime) values (?,?,?,?,?)",
                               row)
                total_count += 1
            else:
                row = (path, 0, filesize, createtime, updatetime)
                cursor.execute("insert into result (filepath, flag,filesize,createtime,updatetime) values (?,?,?,?,?)",
                               row)
                total_count += 1

            if total_count % count == 0:
                cursor.close()
                conn.commit()
                conn.close()
                print(str(total_count / count) + ".db", "扫描完成")
                sqlite_name = str(total_count // count + 1) + ".db"
                dbname = os.path.join(dbdir, sqlite_name)
                conn = sqlite3.connect(dbname)
                cursor = conn.cursor()
                cursor.execute(
                    'create table result (id INTEGER PRIMARY KEY NOT NULL, filepath varchar(5000), flag varchar(10),filesize FLOAT,createtime datetime,updatetime datetime)')

    cursor.close()
    conn.commit()
    conn.close()
    print(total_count)
    print(dir, u"目录扫描完成")
    return True


if __name__ == '__main__':
    # scan_dir(u'E:\\', u"C:\\Users\\ltcx\\Desktop\\部署4.19\\ResultManage\\sqlites", 20000)
    scan_dir(u'\\\\192.168.3.120\\新建文件夹', u"C:\\Users\\ltcx\\Desktop\\部署4.19\\ResultManage\\sqlites", 20000)

    pass
