#!C:/Python27/ArcGIS10.2/python.exe
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import sys
import time
import psycopg2
from faker import Faker


def main():
    conn = psycopg2.connect(dbname=u"resmanageV0.1",
                            user=u"postgres",
                            password=u"Lantucx2018",
                            host=u"192.168.3.111",
                            port=u"5432")
    cur = conn.cursor()
    f = Faker(locale='zh_CN')
    for i in range(2000000):
        x =f.file_path(11)
        SQL = "INSERT INTO file_resultfile (filepath) VALUES ('%s')" % (x)
        cur.execute(SQL)
    conn.commit()
    conn.close()



if __name__ == '__main__':
    start_time = time.time()

    main()
    end_time = time.time()
    print(end_time - start_time)