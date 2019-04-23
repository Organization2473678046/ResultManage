# -*- coding: utf-8 -*-
from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk
from datetime import datetime
import sys
import time
import psycopg2
from faker import Faker

reload(sys)
sys.setdefaultencoding('utf8')
from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk


def create_index(index_name):
    es = Elasticsearch("192.168.3.120:9200")
    mappings = {
        "settings": {
            "analysis": {
                "analyzer": {
                    "my_analyzer": {
                        "tokenizer": "my_analyzer"
                    }
                },
                "tokenizer": {
                    "my_analyzer": {
                        "type": "ngram",
                        "min_gram": 1,
                        "max_gram": 20,
                        "token_chars": [
                            "letter",
                            "digit"
                        ]
                    }
                }
            }

        },

        "mappings": {
            "doc": {  # doc_type,"文档类型"
                "properties": {
                    # "id": {  # "索引名"
                    #     "type": "long",
                    #     "index": True
                    # },
                    "filepath": {
                        "type": "text",  # keyword不会进行分词,text会分词
                        # "index": True,  # 不建索引为False,建索引为True
                        "analyzer": "my_analyzer",
                        "index_options": "offsets"
                    },
                    "dirlength": {
                        "type": "keyword",
                    },
                    "dirdepth": {
                        "type": "keyword",
                    },
                    "filecreatetime": {
                        "type": "date",
                        "format": "yyyy-MM-dd HH:mm:ss"
                    },
                    "fileupdatetime": {
                        "type": "date",
                        "format": "yyyy-MM-dd HH:mm:ss"
                    }
                }
            }
        }
    }
    res = es.indices.create(index=index_name, body=mappings, ignore=400)
    print u"索引创建完毕"
    return res


# 批量插入数据
def bulk_insert_data(index_name):
    es = Elasticsearch("192.168.3.120:9200")

    f = Faker(locale='zh_CN')
    count = 18821000
    for c in range(10000):
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
        print count
        # print(res)
    print u"插入数据成功"



if __name__ == '__main__':
    # print es.cat.indices()
    # print es.indices
    # 创建索引,index_test,批量插入
    # create_index("index_test")
    # create_index("index_test1")
    # bulk_insert_data("index_test")
    bulk_insert_data("index_test1")
    pass
