# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.test import TestCase

# Create your tests here.
import os
import sys
import time
import random
from datetime import datetime

if not os.environ.get("DJANGO_SETTINGS_MODULE"):
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ResultManage.settings")
import django

django.setup()
from results.models import HandOutList

if __name__ == '__main__':

    # results = ResultFile.objects.filter(filepath=None)
    # print results
    # 添加分发清单测试数据
    for i in range(100):
        HandOutList.objects.create(
            name="苏果超市" + str(i * 2),
            uniquenum=datetime.now().strftime("%Y%m%d%H%M%S%f") + "%06d" % i,
            listnum=str(i * 6),
            auditnum=str((i + 2) * 6),
            secrecyagreementnum="",
            purpose="购物",
            sendunit="苏宁",
            sendunitpostcode="00021",
            receiveunit="苏果超市",
            handler="王五" + str(i),
            # handlerphonenum="",
            handlermobilephonenum="153000" + "%07d" % i,
            receiver="张三" + str(i),
            # receiverphonenum="",
            receivermobilephonenum="139000" + "%07d" % i,
            sendouttime="2019-04-25 09:50:24.{0}+08".format(str(i)),
            recievetime="2019-04-26 09:52:24.{0}+08".format(str(i)),
            selfgetway=random.choice([True, False]),
            postway=random.choice([True, False]),
            networkway=random.choice([True, False]),
            sendtoway=random.choice([True, False]),
            # signature="",
            papermedia=random.choice([True, False]),
            cdmedia=random.choice([True, False]),
            diskmedia=random.choice([True, False]),
            networkmedia=random.choice([True, False]),
            othermedia=random.choice([True, False]),
            medianums="%08d" % random.randint(1000, 9999),
            # mapnums="",
            # filename="",
        )
        time.sleep(1)

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

    # li = []
    # if li:
    #     print("非空")
    # filepath = FilePath.objects.get(handoutlist_name="苏果超市4", fileinfo_name="成果1",
    #                                             filepath= "\\\\192.168.3.120\\新建文件夹\\120转180所需安装包\\apache\\Microsoft.NET.exe")

    # print(filepath)

    # print(datetime.strptime("2019-04-23", "%Y-%m-%d"))
    # for i in range(1,20):
    #     try:
    #         FileInfo.objects.get(handoutlist_name="苏果超市4",name="成果"+str(i))
    #     except:
    #         print("成果"+str(i),"不存在")
    #     else:
    #         print("成果"+str(i),"存在")
    #
    #
    #     print(i)

    # dict1 = {"name="123","key="key"}
    # print(dict1.keys())
    # if "name" in dict1.keys():
    #     print("有")
    # from datetime import datetime

    # datetime.now().strftime("%Y%m%d%H%M%S%f") + "%06d" % 2
    # print(datetime.now().strftime("%Y%m%d%H%M%S%f") + "%06d" % 55557777)
    # print(type(datetime.now().strftime("%Y%m%d%H%M%S%f")))

    pass
