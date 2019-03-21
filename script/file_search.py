#!C:/Python27/ArcGIS10.2/python.exe
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import sys
import os
import psycopg2
import time

reload(sys)
sys.setdefaultencoding('utf8')

import os
import sys

if not os.environ.get("DJANGO_SETTINGS_MODULE"):
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ResultManage.settings")
import django

django.setup()

from file.models import ResultFile


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


def ergodic(file_midir, cur):
    file_list_01 = os.listdir(file_midir)
    for file in file_list_01:
        path = file_midir + "/" + file
        if os.path.isdir(path):
            ergodic(path, cur)
        elif os.path.isfile(path):
            # SQL = "INSERT INTO file_resultfile (filepath) VALUES ('%s')" % (path)
            ResultFile.objects.create(filepath=path)
            # cur.execute(SQL)
            print "文件：%s" % path
        else:
            # SQL = "INSERT INTO file_resultfile (filepath) VALUES ('%s')" % (path)
            ResultFile.objects.create(filepath=path)
            # print SQL
            # cur.execute(SQL)
            print "这是个神秘的文件：%s" % path


def os_walk():
    for maindir, subdir_list, file_name_list in os.walk('\\\\192.168.3.120\\新建文件夹'):
        print "maiddir: %s" % maindir
        print "subdir_list: %s" % subdir_list
        ResultFile.objects.create(filepath=maindir)

        for subdir in subdir_list:
            print "subdir: %s" % subdir
            totalpath = os.path.join(maindir,subdir)
            print "total_subdir: %s" % totalpath
            dirlength = len(totalpath)
            totalpath_list = totalpath.split('\\')
            print "totalpath_list: %s" % totalpath_list
            dirdepth = len(totalpath_list)-3
            ResultFile.objects.create(filepath=totalpath, dirlength=dirlength, dirdepth=dirdepth)
        for file in file_name_list:
            filepath = os.path.join(maindir,file)
            ResultFile.objects.create(filepath=filepath)



if __name__ == '__main__':
    # file_midir = "E:/RGSManager"
    # file_midir = "D:/PycharmProjects"
    # start_time = time.time()
    # print start_time
    # # file_midir = "\\\\192.168.3.120\新建文件夹"
    # file_midir = "\\\\192.168.3.120/新建文件夹"
    # # conn_database(file_midir)
    # end_time = time.time()
    # total_time = end_time - start_time
    # print total_time

    # a = "abcdefa"
    # print a.count('a')
    os_walk()

    temp = r"\\192.168.3.120\新建文件夹\120转180所需安装包\apache\httpd-2.4.6-win32-VC9\Apache24"
    temp =temp.replace("\\",'/')
    # print temp
    # temp_list = temp.split("\\")
    # print temp_list
    # for i in temp_list:
    #     print i
    # print os.sep