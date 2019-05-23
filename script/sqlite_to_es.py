# -*- coding: utf-8 -*-
import sqlite3
import os
import shutil
# from faker import Faker
from datetime import datetime
from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk


# 批量插入数据
# def bulk_insert_data(es,index_name):
#     #es = Elasticsearch(timeout=10)
#
#     f = Faker(locale='zh_CN')
#     count = 0
#     for c in range(1000):
#         actions = []
#         for i in range(1000):
#             filepath = f.file_path(3) + f.name() + f.license_plate() + f.name()
#             count += 1
#             action = {
#                 "_index": index_name,
#                 "_type": "doc",
#                 # "_id": str(count),
#                 "_source": {
#                     # "id": str(),
#                     "filepath": filepath,
#                     "dirlength": len(filepath),
#                     "dirdepth": len(filepath.split("/")),
#                     "filesize": "5M",
#                     "filecreatetime": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
#                     "fileupdatetime": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#                 }
#             }
#
#             actions.append(action)
#         res, _ = bulk(es, actions, index=index_name, raise_on_error=True)
#         print(count)
#         # print(res)
#         # print(_)
#     print("插入数据成功")


def insert_data(dbname, es, index_name):
    conn = sqlite3.connect(dbname)
    cursor = conn.cursor()
    count = 0
    while True:
        cursor.execute("select * from result where flag='0'")
        data_list = cursor.fetchmany(500)
        if data_list:
            actions = []
            sqlid_list = []
            for data in data_list:
                count += 1
                print(data)
                filepath = data[1]
                sqlid = "id=%d" % data[0]
                sqlid_list.append(sqlid)
                action = {
                    "_index": index_name,
                    "_type": "doc",
                    "_source": {
                        "filepath": filepath,
                        "dirlength": len(filepath),
                        "dirdepth": len(filepath.split("\\")) - 2,
                        "filesize": data[3],
                        "filetype":data[4],
                        "filecreatetime": data[5],
                        "fileupdatetime": data[6]
                    }
                }
                actions.append(action)
            res, _ = bulk(es, actions, index=index_name, raise_on_error=True)
            sqlstr = " or ".join(sqlid_list)
            sql = "update result set flag='1' where {0}".format(sqlstr)
            cursor.execute(sql)
            # 每500次提交一次
            conn.commit()
            del actions
            del sqlid_list
            del sqlstr
        else:
            conn.close()
            break

    print(count)
    conn.close()
    print(dbname, u"数据迁移完毕")
    return True


def main(es, index_name, old_dbdir, new_dbdir):
    dir_list = os.listdir(old_dbdir)
    for dir in dir_list:
        if dir.endswith(u".db"):
            dbname = os.path.join(old_dbdir, dir)
            res = insert_data(dbname, es, index_name)
            if res:
                shutil.move(dbname, new_dbdir)


if __name__ == '__main__':
    # es = Elasticsearch(timeout=120)
    # index_name = "resmanagev0.1"
    # bulk_insert_data(es, index_name)
    # insert_data(dbname, es, "resmanagev0.1")
    # main(es, "resmanagev0.1", u"D:\\PycharmProjects\\ResultManage\\no-elasticsearch-py3\\ResultManage", u"D:\\PycharmProjects\\ResultManage\\no-elasticsearch-py3\\ResultManage\\finish\\")

    es = Elasticsearch("192.168.190.133:9200",timeout=120)
    main(es, "resmanagev0.3", "/opt/rh/httpd24/root/var/www/html/ResultManage/script/", "/opt/rh/httpd24/root/var/www/html/ResultManage/script")

    pass
