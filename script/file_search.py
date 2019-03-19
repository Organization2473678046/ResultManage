#!C:/Python27/ArcGIS10.2/python.exe
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import sys
import os
import psycopg2

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
            print "文件：%s" % path
        else:
            SQL = "INSERT INTO file_resultfile (file_path, server_allow) VALUES ('%s', 'C:/')" % (path)
            print SQL
            cur.execute(SQL)
            print "这是个神秘的文件：%s" % path


def main():
    # file_midir = "E:/RGSManager"
    file_midir = "C:"

    conn_database(file_midir)


if __name__ == '__main__':
    main()
