# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.test import TestCase

# Create your tests here.
import os
import sys
import time
import random

reload(sys)
sys.setdefaultencoding('utf8')

if not os.environ.get("DJANGO_SETTINGS_MODULE"):
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ResultManage.settings")
import django

django.setup()
from file.models import ResultFile, HandOutList,FileInfo,FilePath

if __name__ == '__main__':

    # result = ResultFile.objects.filter(filepath=None)
    # print result
    # 添加分发清单测试数据
    # for i in range(100):
    #     HandOutList.objects.create(
    #         name="苏果超市" + str(i * 2),
    #         listnum=str(i * 6),
    #         auditnum=str((i + 2) * 6),
    #         secretlevel=str(i),
    #         purpose="购物",
    #         receiveunit="苏果",
    #         receiver="张三" + str(i),
    #         receiverinfo="153000" + str(i),
    #         handovertime="2019-03-25 09:50:24.{0}+08".format(str(i)),
    #         recievetime="2019-03-25 09:52:24.{0}+08".format(str(i)),
    #         undertaker="李四" + str(i),
    #         # deliveryway=random.choice(["自取", "邮寄", "网络", "送往", "其他"]),
    #         selfgetway=random.choice([True,False]),
    #         postway=random.choice([True,False]),
    #         networkway=random.choice([True,False]),
    #         deliverway=random.choice([True,False]),
    #         otherway=random.choice([True,False]),
    #         handler="王五" + str(i)
    #
    #     )
    #     time.sleep(1)

    # 添加成果测试数据
    # handoutlists=HandOutList.objects.all()[:20]
    # for handoutlist in handoutlists:
    #     for i in range(1,10):
    #         FileInfo.objects.create(
    #             name="成果"+str(i),
    #             resulttype=str(i),
    #             num = random.randint(2,50),
    #             datasize="{0}GB".format(str(i)),
    #             # mediumtype = random.choice(["纸质","光盘","硬盘","网络","其他"]),
    #             # mediumnum=str(random.randint(1000,9999)),
    #             papermedia=random.choice([True,False]),
    #             cdmedia=random.choice([True,False]),
    #             diskmedia=random.choice([True,False]),
    #             networkmedia=random.choice([True,False]),
    #             othermedia=random.choice([True,False]),
    #             resultyear = random.choice(["2012","2013","2014","2015","2016","2017","2018"]),
    #             secretlevel=str(random.randint(2,7)),
    #             handoutlist_name=handoutlist.name
    #         )
    #         time.sleep(2)

    li = []
    if li:
        print "非空"



    pass
