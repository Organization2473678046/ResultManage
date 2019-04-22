# -*- coding: utf-8 -*-
import sys
from elasticsearch import Elasticsearch


def create_index(es, index_name):
    # es = Elasticsearch(timeout=20)
    body = {
        "settings": {
            "index": {
                "number_of_shards": "1",
                "number_of_replicas": "0",
                "max_result_window": 10000000,
                'refresh_interval': -1,
                "analysis": {
                    "analyzer": {  # 这里定义分析器
                        "my_analyzer": {
                            "tokenizer": "my_analyzer"  # 分词器
                        }
                    },
                    "tokenizer": {  # 这里定义分词器
                        "my_analyzer": {
                            "type": "ngram",
                            "min_gram": 1,
                            "max_gram": 20,
                            "token_chars": ["letter", "digit"]
                        }
                    }
                }
            }
        },

        "mappings": {
            "doc": {  # doc_type,"文档类型"
                "properties": {
                    "filepath": {
                        "type": "text",
                        "analyzer": "my_analyzer",
                        "index_options": "offsets"
                    },
                    "dirlength": {
                        "type": "keyword",
                        # "ignore_above": 100
                    },
                    "dirdepth": {
                        "type": "keyword",
                        # "ignore_above": 100
                    },
                    "filesize": {
                        "type": "keyword",
                    },
                    "filecreatetime": {
                        "type": "date",
                        "format": "yyyy-MM-dd HH:mm:ss",
                        # "index_options": "offsets"
                    },
                    "fileupdatetime": {
                        "type": "date",
                        "format": "yyyy-MM-dd HH:mm:ss",
                        # "index_options": "offsets"
                    },

                }
            }
        }
    }
    res = es.indices.create(index=index_name, body=body, ignore=400)
    print(res)
    print("索引创建完毕")


if __name__ == '__main__':
    # es = Elasticsearch("192.168.1.110:9200",timeout=20)
    es = Elasticsearch(timeout=120)
    if len(sys.argv) == 2:
        print("要创建的索引名称为:%s" % sys.argv[1])
        index_name = sys.argv[1]
        create_index(es, index_name)
    else:
        print("脚本运行方式为: python3 %s 要创建的索引名称" % sys.argv[0])
