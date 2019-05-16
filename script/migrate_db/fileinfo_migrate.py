# -*- coding: utf-8 -*-
import os
import sys
import psycopg2


def get_fileinfo_data(tablename):
    #
    conn = psycopg2.connect(dbname="resmanageV0.1",
                            user="postgres",
                            password="Lantucx2018",
                            host="localhost",
                            port="5432")
    cur = conn.cursor()
    sql = u"select * from %s order by id" % tablename
    cur.execute(sql)
    while True:
        data = cur.fetchone()
        if data:
            print(data)
            fileinfo_insert(data)
        else:
            conn.close()
            return


def fileinfo_insert(data):
    # file_fileinfo表数据的迁移
    conn = psycopg2.connect(dbname="resmanageV0.2",
                            user="postgres",
                            password="Lantucx2018",
                            host="localhost",
                            port="5432")
    cur = conn.cursor()

    sql = u"insert into file_fileinfo (name,resulttype,num,datasize,resultyear,secretlevel,handoutlist_name,createtime,updatetime,cdmedia,cdmedianum,diskmedia,diskmedianum,networkmedia,othermedia,othermedianum,papermedia) values ('%s','%s','%s','%s','%s','%s','%s',%r,%r,%r,'%s',%r,'%s',%r,%r,'%s',%r)" % (
        data[1], data[2], str(data[3]), data[4], data[5], data[6], data[7], str(data[8]), str(data[9]), data[10],
        data[11], data[12], data[13], data[14], data[15], data[16], data[17])
    print(sql)
    cur.execute(sql)
    conn.commit()
    conn.close()


if __name__ == '__main__':
    # 迁移成果资料表
    get_fileinfo_data("file_fileinfo")

    pass
