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
            user_insert(data, "users_user")
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
    sql = "insert into %s (username, password,is_superuser, is_staff, is_active,reallyname,isadmin) values ('%s', '%s',%r,%r, %r,'%s',%r)" % (
        tablename, data[4], data[1], data[3], data[8], data[9], data[11], data[12])
    print(sql)
    cur.execute(sql)
    conn.commit()
    conn.close()


if __name__ == '__main__':
    # 迁移users_user表时,需要去掉first_name,last_name, email,date_joined几个字段的非空约束
    get_user_data("users_user")
    pass
