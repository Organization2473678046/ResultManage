# -*- coding: utf-8 -*-
import os
import sys
import psycopg2


def get_user_data(tablename):
    # 获取用户表数据
    conn = psycopg2.connect(dbname="resmanageV0.1",
                            user="postgres",
                            password="Lantucx2018",
                            host="localhost",
                            port="5432")
    cur = conn.cursor()
    SELECTSQL = "select * from %s order by id" % tablename
    cur.execute(SELECTSQL)
    while True:
        data = cur.fetchone()
        if data:
            print(data)
            # user_insert(data, "users_user")
        else:
            conn.close()
            return


def user_insert(data, tablename):
    # users_user表数据的迁移
    conn = psycopg2.connect(dbname="resmanageV0.2",
                            user="postgres",
                            password="Lantucx2018",
                            host="localhost",
                            port="5432")
    cur = conn.cursor()

    sql = "insert into %s (username, password,is_superuser, is_staff, is_active,reallyname,isadmin) values ('%s', '%s',%r,%r, %r, %r, '%s')" % (
        tablename, data[4], data[1], data[3], data[8], data[9], data[11], data[12])
    print(sql)
    cur.execute(sql)
    conn.commit()
    conn.close()


def get_handoutlist_data(tablename):
    # 获取主任务包表数据
    conn = psycopg2.connect(dbname="resmanageV0.1",
                            user="postgres",
                            password="Lantucx2018",
                            host="localhost",
                            port="5432")
    cur = conn.cursor()
    sql = u"select * from %s order by id" % tablename
    cur.execute(sql)
    data_list = cur.fetchall()
    # print data_list
    for data in data_list:
        # data = cur.fetchone()
        # data = list(data)
        print(data)
        # username = data[2]
        # print type(username)
        # cur.execute(u"-- select reallyname from users_user where username = '%s'" % username)
        # reallyname = cur.fetchone()[0]
        # print reallyname
        # data.append(reallyname)
        handoutlist_insert(data)

    conn.close()


def handoutlist_insert(data):
    """file_handoutlist表数据的迁移"""
    conn = psycopg2.connect(dbname="resmanageV0.2",
                            user="postgres",
                            password="Lantucx2018",
                            host="localhost",
                            port="5432")
    cur = conn.cursor()
    sql = u"insert into file_hanoutlist (name,listnum,auditnum,secretlevel,purpose,receiveunit,receiver,receiverinfo,handovertime,recievetime,undertaker,selfgetway,postway,networkway,deliverway,otherway,otherwaydetail,handler,createtime,updatetime) values ('%s','%s','%s','%s','%s','%s','%s','%s',  %r, %r,'%s','%s',%r,%r,%r,%r,'%s','%s',%r,%r)" % (
        data[1], data[2], data[3], data[4], data[5], data[6], data[7],
        data[8], str(data[9]), str(data[10]), data[11], data[12], data[13], data[14], data[15], data[16], data[17],
        data[18], str(data[19]), str(data[20]))
    # else:
    #     # sql = u"insert into taskpackages_taskpackage (name,owner,exowner,mapnums,file,status,describe,createtime,updatetime,isdelete,mapnumcounts, schedule,reallyname) values ('%s','%s','%s','%s','%s',%r, '%s',%r, %r,%r,%d,'%s','%s')" % (
    #     #     data[1], data[10], data[2], data[3], data[4], data[5], data[9], str(data[7]), str(data[8]), data[6])
    #     sql = u"insert into taskpackages_taskpackage (name,owner,exowner,mapnums,file,status,createtime,updatetime,describe,isdelete,mapnumcounts,newtaskpackagesonfornotice,reallyname,schedule,regiontask_name) values ('%s','%s','%s','%s','%s',%r, %r, %r,'%s',%r,%d,%d,'%s','%s','%s')" % (
    #         data[1], data[2], data[3], data[4], data[5], data[6], str(data[7]), str(data[8]), data[9],
    #         data[10], data[11], data[12], data[13], data[14], data[15])
    cur.execute(sql)

    conn.commit()
    conn.close()


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

    sql = u"insert into file_fileinfo (name,resulttype,num,datasize,papermedia,cdmedia,cdmedianum,diskmedia,diskmedianum,networkmedia,othermedia,othermedianum,resultyear,secretlevel,,handoutlist_name,createtime,updatetime) values ('%s','%s','%s','%s',%r,%r,'%s',%r,'%s',%r,%r,'%s','%s','%s','%s',%r,%r)" % (
        data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8], data[9], data[10], data[11], data[12],
        data[13], data[14], data[15], str(data[16]), str(data[17]))
    print(sql)
    cur.execute(sql)
    conn.commit()
    conn.close()


def get_filepath_data(tablename):
    # file_filepath表的迁移
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
            filepath_insert(data)
        else:
            conn.close()
            return


def filepath_insert(data):
    # file_filepath表的迁移
    conn = psycopg2.connect(dbname="resmanageV0.2",
                            user="postgres",
                            password="Lantucx2018",
                            host="localhost",
                            port="5432")
    cur = conn.cursor()
    # if data[3] is None or data[3] == "None":
    sql = u"insert into file_filepath (filepath,fileinfo_name,handoutlist_name,createtime,updatetime) values ('%s','%s','%s',%r,%r)" % (
        data[1], data[2], data[3], str(data[4]), str(data[5]))

    # else:
    #     sql = u"insert into taskpackages_taskpackageowner (taskpackage_name,owner,exowner,createtime,describe,isdelete,regiontask_name) values ('%s','%s','%s',%r,'%s',%r,'%s')" % (
    #         data[1], data[2], data[3], str(data[4]), data[5], data[6], data[7])
    # print(sql)
    cur.execute(sql)
    conn.commit()
    conn.close()


if __name__ == '__main__':
    # 迁移users_user表时,需要去掉first_name,last_name, email,date_joined几个字段的非空约束
    # get_user_data("users_user")

    # 迁移分发单表
    # get_handoutlist_data("file_handoutlist")

    # 迁移成果资料表
    # get_fileinfo_data("file_fileinfo")

    # 迁移成果文件路径表
    # get_filepath_data("file_filepath'")

    pass
