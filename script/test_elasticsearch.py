from datetime import datetime
from elasticsearch import Elasticsearch
from faker import Faker


def test():
    es = Elasticsearch()
    f = Faker(locale='zh_CN')
    # es.indices.create(index='my-index', ignore=400)
    # es.index(index="my-index", id=42, body={"any": "data", "timestamp": datetime.now()}, doc_type="index")
    for _ in range(1):
        es.index(index="resmanage", id=1, body={"filepath": f.file_path(8), "createtime": datetime.now()},
                 doc_type="modelresult")

    # text = es.get(index="my-index", id=42, doc_type="index")['_source']
    # text = es.get(index="resmanage", id=1, doc_type="modelresult")['_source']
    # print(text)


if __name__ == '__main__':
    test()
