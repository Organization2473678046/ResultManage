#!C:/Python27/ArcGIS10.2/python.exe
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import sqlite3
import sys
import time
import psycopg2
from faker import Faker


def main():
    # conn = psycopg2.connect(dbname=u"resmanageV0.1",
    #                         user=u"postgres",
    #                         password=u"Lantucx2018",
    #                         host=u"192.168.3.111",
    #                         port=u"5432")


    conn = sqlite3.connect("faker_data.db")
    cur = conn.cursor()
    cur.execute('CREATE TABLE "result" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "filepath" varchar(5000) NOT NULL, "flag" varchar(32))')

    f = Faker(locale='zh_CN')
    for i in range(20000):
        x =f.file_path(8)
        SQL = "INSERT INTO result (filepath, flag) VALUES ('%s', '%s')" % (x, "0")
        cur.execute(SQL)
    conn.commit()
    conn.close()



if __name__ == '__main__':
    start_time = time.time()

    main()
    end_time = time.time()
    print(end_time - start_time)
