#!C:/Python27/ArcGIS10.2/python.exe
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import sys
import os
import psycopg2
import time

reload(sys)
sys.setdefaultencoding('utf8')


def conn_database(file_midir):
    conn = psycopg2.connect(dbname=u"resmanageV0.1",
                            user=u"postgres",
                            password=u"Lantucx2018",
                            host=u"localhost",
                            port=u"5432")
    cur = conn.cursor()
    ergodic(file_midir, cur)
    conn.commit()
    conn.close()

#
# def ergodic(file_midir, cur):
#     file_list_01 = os.listdir(file_midir)
#     for file in file_list_01:
#         path = file_midir + "/" + file
#         if os.path.isdir(path):
#             ergodic(path, cur)
#         elif os.path.isfile(path):
#             SQL = "INSERT INTO file_resultfile (filepath, serverIP) VALUES ('%s', 'C:/')" % (path)
#             print "文件：%s" % path
#         else:
#             SQL = "INSERT INTO file_resultfile (filepath, serverIP) VALUES ('%s', 'C:/')" % (path)
#             print SQL
#             cur.execute(SQL)
#             print "这是个神秘的文件：%s" % path

def ergodic(file_midir, cur):
    file_list_01 = os.listdir(file_midir)
    for file in file_list_01:
        path = file_midir + "/" + file
        if os.path.isdir(path):
            ergodic(path, cur)
        elif os.path.isfile(path):
            SQL = "INSERT INTO file_resultfile (filepath) VALUES ('%s')" % (path)
            # cur.execute(SQL)
            print "文件：%s" % path
        else:
            SQL = "INSERT INTO file_resultfile (filepath) VALUES ('%s')" % (path)
            # print SQL
            # cur.execute(SQL)
            print "这是个神秘的文件：%s" % path


def main():
    # file_midir = "E:/RGSManager"
    # file_midir = "C:"
    # conn_database(file_midir)
    pass


if __name__ == '__main__':
    # file_midir = "E:/RGSManager"
    # file_midir = "D:/PycharmProjects"
    # start_time = time.time()
    # print start_time
    file_midir = "E:/E盘文件"
    conn_database(file_midir)
    # end_time = time.time()
    # total_time = end_time-start_time
    # print total_time

