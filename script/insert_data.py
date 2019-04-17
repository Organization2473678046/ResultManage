# -*- coding: utf-8 -*-
import sys
from faker import Faker
from datetime import datetime
from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk


# 批量插入数据
def bulk_insert_data(index_name):
    es = Elasticsearch(timeout=10)

    f = Faker(locale='zh_CN')
    count = 0
    for c in range(1):
        actions = []
        for i in range(1000):
            filepath = f.file_path(3) + f.name() + f.license_plate() + f.name()
            count += 1
            action = {
                "_index": index_name,
                "_type": "doc",
                "_id": str(count),
                "_source": {
                    # "id": str(),
                    "filepath": filepath,
                    "dirlength": len(filepath),
                    "dirdepth": len(filepath.split("/")),
                    "filecreatetime": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    "fileupdatetime": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                }
            }

            actions.append(action)
        res, _ = bulk(es, actions, index=index_name, raise_on_error=True)
        print(count)
        # print(res)
    print("插入数据成功")


if __name__ == '__main__':
    print(u"要插入数据的索引为: %s" % sys.argv[1])
    index_name = sys.argv[1]
    bulk_insert_data(index_name)
