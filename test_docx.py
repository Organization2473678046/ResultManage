# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os
import shutil
from datetime import datetime
from doc_to_docx import doc_docx
from doc_2018 import tables_2018
from doc_2017 import tables_2017
from doc_docx_linux import transfer_format
import sqlite3
from docx import Document
import re
from doc_more import doc_more


def data(document, cursor, date_now, doc_file, doc_more_file_path, path_old, doc_year):
    title = ""      # 分发单标题
    signer = ""     # 签发
    name = ""       # 分发单名称
    uniquenum = date_now        # 分发单唯一编号
    listnum = ""    # 编号
    auditnum = ""   # 审核编号
    secrecyagreementnum = ""    # 保密责任书编号
    purpose = ""    # 用途
    sendunit = ""   # 发出单位
    sendunitaddr = ""       # 发出单位通讯地址
    sendunitpostcode = ""   # 发出单位邮政编码
    receiveunit = ""        # 接收单位
    receiveunitaddr = ""    # 接收单位通讯地址
    receiveunitpostcode = ""    # 接收单位邮政编码
    handler = ""            # 经办人
    handlerphonenum = ""    # 经办人联系电话(座机)
    handlermobilephonenum = ""  # 经办人联系电话(手机)
    receiver = ""           # 接收人
    receiverphonenum = ""   # 接收人联系电话(座机)
    receivermobilephonenum = ""     # 接收人联系电话(手机)
    sendouttime = ""        # 发出日期
    recievetime = ""        # 接收日期
    selfgetway = False         # 递送方式为自取
    postway = False            # 递送方式为邮寄
    networkway = False         # 递送方式为网络
    sendtoway = False          # 递送方式为送往
    signature = ""          # 递送方式后面的签名
    papermedia = False         # 纸质介质
    cdmedia = False            # 光盘介质
    diskmedia = False          # 硬盘介质
    networkmedia = False       # 网络介质
    othermedia = False         # 其他介质
    medianums = ""          # 介质编号
    mapnums = ""            # 分发单包含的成果的图幅号
    filename = doc_file           # 分发单文件名字
    file = ""               # 分发单文件路径

    remake_str = ""
    is_remake = False
    is_textbox = True

    x = 0

    # 读取文本框
    xml = document._element.xml
    pattern = "<v:textbox([\s\S]*?)</v:textbox>"
    regex = re.compile(pattern)
    textbox_list = regex.findall(xml)
    if len(textbox_list) <= 2:
        for result in textbox_list:
            # pattern2 = u"[\u4e00-\u9fa5]+"
            pattern2 = "<w:t>(.*?)</w:t>"
            regex2 = re.compile(pattern2)
            textbox_str = regex2.findall(result)
            textbox_str = "".join(textbox_str)
            if x == 0 and is_textbox == True:
                print("名称:" + textbox_str)
                name = textbox_str
            if x == 1 and is_textbox == True:
                print("用途:" + textbox_str)
                purpose = textbox_str
                x = 0
                is_textbox = False
            x += 1


        # 读取文本
        for para in document.paragraphs:
            pattern = "[\u4e00-\u9fa5]+"
            regex = re.compile(pattern)
            results = regex.findall(para.text)
            # print(results)
            if results != [] and is_remake is False:
                if "交付清单" in results[0]:
                    title = para.text
                    print("标题：" + results[0])

                if "审批单号" in results:
                    my_num01 = para.text.split(" ")[0].split("：").pop()
                    auditnum = my_num01
                    print("审批单号:" + my_num01)

                if "签发" in results:
                    my_num001 = para.text.split("：").pop().split("签")[0].strip()
                    listnum = my_num001
                    print("编号:" + my_num001)

                if "保密责任证书" in results:
                    my_num02 = para.text.split("：").pop()
                    secrecyagreementnum = my_num02
                    print("保密责任证书:" + my_num02)

                if "递送方式" in results:
                    my_list01 = para.text.split(" ")
                    for my_way in my_list01:
                        if my_way == "自取":
                            selfgetway = True
                        if my_way == "邮寄":
                            postway = True
                        if my_way == "网络":
                            networkway = True
                        if my_way == "送往":
                            sendtoway = True

                if "介质类型" in results:
                    my_list02 = para.text.split(" ")
                    for my_way in my_list02:
                        if my_way == "纸质":
                            selfgetway = True
                        if my_way == "光盘":
                            postway = True
                        if my_way == "硬盘":
                            networkway = True
                        if my_way == "网络":
                            sendtoway = True
                        if my_way == "其他":
                            sendtoway = True

                if "介质编号" in results:
                    my_num03 = para.text.split("：").pop()
                    medianums = my_num03
                    print("介质编号:" + my_num03)

                if "发出单位" in results:
                    my_str01 = para.text.split(" ")[0].split("：").pop()
                    sendunit = my_str01
                    print("发出单位:" + my_str01)

                if "接收单位" in results:
                    my_str02 = para.text.split(" ").pop().split("：").pop()
                    receiveunit = my_str02
                    print("接收单位：" + my_str02)

                if "通讯地址" in results:
                    my_str03 = para.text.split(" ")[0].split("：").pop()
                    sendunitaddr = my_str03
                    print("发出方通讯地址：" + my_str03)
                    my_str03_ = para.text.split("：").pop()
                    receiveunitaddr = my_str03_
                    print("接收方通讯地址：" + receiveunitaddr)


                if "邮政编码" in results:
                    my_str04 = para.text.split(" ")[0].split("：").pop()
                    sendunitpostcode = my_str04
                    print("发出方邮政编码：" + my_str04)

                    my_str04_ = para.text.split("：").pop()
                    receiveunitpostcode = my_str04_
                    print("接收方邮政编码：" + receiveunitpostcode)

                if "座机" in results:
                    my_str05 = para.text.split(" ")[0].split("）").pop()
                    handlerphonenum = my_str05
                    print("发出方联系电话：（座机）：" + my_str05)

                    my_str05_ = para.text.split("）").pop()
                    receiverphonenum = my_str05_
                    print("接收方联系电话：（座机）：" + receiverphonenum)

                if "手机" in results:
                    my_str06 = para.text.split("）")[1].split(" ")[0]
                    handlermobilephonenum = my_str06
                    print("发出方联系电话：（手机）：" + my_str06)

                    my_str06_ = para.text.split("）").pop()
                    receivermobilephonenum = my_str06_
                    print("接收方联系电话：（手机）：" + receivermobilephonenum)

                if "发出日期" in results:
                    my_str07 = para.text.split("：")[1].split("接")[0]
                    my_str07 = my_str07.strip()
                    my_str07_year = my_str07.split("年")[0].strip() if my_str07.split("年")[0].strip() != '' else "  "
                    my_str07_mon = my_str07.split("年")[1].split("月")[0].strip() if my_str07.split("年")[1].split("月")[0].strip() != '' else "  "
                    my_str07_day = my_str07.split("年")[1].split("月")[1].split("日")[0].strip() if my_str07.split("年")[1].split("月")[1].split("日")[0].strip() != '' else "  "
                    sendouttime = my_str07_year + "年" + my_str07_mon + "月" + my_str07_day + "日"
                    print("发出日期：" + sendouttime)

                    my_str07_ = para.text.split("接收日期：")[1].strip()
                    my_str07_year = my_str07_.split("年")[0].strip() if my_str07_.split("年")[0].strip() != '' else "  "
                    my_str07_mon = my_str07_.split("年")[1].split("月")[0].strip() if my_str07_.split("年")[1].split("月")[0].strip() != '' else "  "
                    my_str07_day = my_str07_.split("年")[1].split("月")[1].split("日")[0].strip() if my_str07_.split("年")[1].split("月")[1].split("日")[0].strip() != '' else "  "

                    recievetime = my_str07_year + "年" + my_str07_mon + "月" + my_str07_day + "日"
                    print("接收日期：" + recievetime)


                if "注" in results:
                    is_remake = True
                    my_str09 = para.text.split("：").pop()
                    remake_str = my_str09
                    continue

            if is_remake:
                remake_str += para.text

        print("备注图幅号：" + remake_str)
        mapnums = remake_str
        row = (title, signer, name, uniquenum, listnum, auditnum, secrecyagreementnum, purpose, sendunit, sendunitaddr, sendunitpostcode, receiveunit, receiveunitaddr, receiveunitpostcode, handler, handlerphonenum, handlermobilephonenum, receiver, receiverphonenum, receivermobilephonenum, sendouttime, recievetime, selfgetway, postway, networkway, sendtoway, signature, papermedia, cdmedia, diskmedia, networkmedia, othermedia, medianums, mapnums, filename, file)
        cursor.execute("INSERT INTO results_handoutlist (title, signer, name, uniquenum, listnum, auditnum, secrecyagreementnum, purpose, sendunit, sendunitaddr, sendunitpostcode, receiveunit, receiveunitaddr, receiveunitpostcode, handler, handlerphonenum, handlermobilephonenum, receiver, receiverphonenum, receivermobilephonenum, sendouttime, recievetime, selfgetway, postway, networkway, sendtoway, signature, papermedia, cdmedia, diskmedia, networkmedia, othermedia, medianums, mapnums, filename, file) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", row)

        # 读取表格
        if doc_year == 2018:
            tables_2018(document, cursor, date_now)
        if doc_year == 2017:
            tables_2017(document, cursor, date_now)


    else:
        print("此文件为多单号文件：" + doc_file)
        doc_more(document, cursor, date_now, doc_file, doc_more_file_path, path_old, doc_year)
        # shutil.move(path_old, doc_more_file_path)
    return date_now, doc_file





def test_doc(path_old, path_new, doc_year, date_now, doc_file, doc_more_file_path, cursor):
    path_new = path_new + "\\" + doc_file + "x"

    doc_docx(path_new, path_old)

    document = Document(path_new)

    # 读取数据
    data(document, cursor, date_now, doc_file, doc_more_file_path, path_old, doc_year)




def main(doc_path, docx_path, doc_year, doc_finish, doc_more_file_path):
    dbname = "doc_sqlit_%s.db" % (datetime.now().strftime("%H-%M-%S-%f"))
    conn = sqlite3.connect(dbname)
    cursor = conn.cursor()

    cursor.execute(
        'CREATE TABLE "results_fileinfo" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(5000) NOT NULL, "secretlevel" varchar(1000) NULL, "resultnum" varchar(2000) NULL, "datasize" varchar(1000) NULL, "formatormedia" varchar(1000) NULL, "remarks" varchar(5000) NULL,"handoutlist_uniquenum" varchar(5000) NULL, "createtime" datetime NULL, "updatetime" datetime NULL)')

    cursor.execute(
        'CREATE TABLE "results_handoutlist" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "title" varchar(5000) NULL, "signer" varchar(1000) NULL, "name" varchar(5000) NULL, "uniquenum" varchar(5000) NOT NULL UNIQUE, "listnum" varchar(1000) NULL, "auditnum" varchar(1000) NULL, "secrecyagreementnum" varchar(2000) NULL, "purpose" varchar(2000) NULL, "sendunit" varchar(5000) NULL, "sendunitaddr" varchar(5000) NULL, "sendunitpostcode" varchar(1000) NULL, "receiveunit" varchar(5000) NULL, "receiveunitaddr" varchar(5000) NULL, "receiveunitpostcode" varchar(1000) NULL, "handler" varchar(1000) NULL, "handlerphonenum" varchar(1000) NULL, "handlermobilephonenum" varchar(1000) NULL, "receiver" varchar(5000) NULL, "receiverphonenum" varchar(1000) NULL, "receivermobilephonenum" varchar(1000) NULL, "sendouttime" varchar(1000) NULL, "recievetime" varchar(1000) NULL, "selfgetway" bool NOT NULL, "postway" bool NOT NULL, "networkway" bool NOT NULL, "sendtoway" bool NOT NULL, "signature" varchar(5000) NULL, "papermedia" bool NOT NULL, "cdmedia" bool NOT NULL, "diskmedia" bool NOT NULL, "networkmedia" bool NOT NULL, "othermedia" bool NOT NULL, "medianums" varchar(5000) NULL, "mapnums" text NULL, "filename" varchar(5000) NULL, "file" varchar(5000) NULL, "createtime" datetime NULL, "updatetime" datetime NULL)')

    doc_files = os.listdir(doc_path)


    for doc_file in doc_files:
        if "~$" in doc_file:
            pass
        else:
            date_now = datetime.now().strftime("%Y%m%d%H%M%S%f")
            doc_file_path = doc_path + "\\" + doc_file
            docx_file_path = docx_path
            test_doc(doc_file_path, docx_file_path, doc_year, date_now, doc_file, doc_more_file_path, cursor)
            try:
                shutil.move(doc_file_path, doc_finish)
            except Exception as e:
                print(e)

    conn.commit()
    conn.close()


# def partition_page():
#     file_path = "/home/ltcx/python_code/doc_more/分发单模板.docx"
#     import win32com.client
#     xls = win32com.client.Dispatch("Word.Application")
#     xls.Documents.Open(file_path)
#     xls.Application.Run("NewMacros.SplitEveryFivePagesAsDocuments")
#     xls.Application.Quit()
#
#
#     pass




if __name__ == '__main__':
    pass
    # windows
    doc_path = "E:\\doc_data"
    doc_finish = "E:\\doc_finish\\"

    # doc_finish = "E:\\doc_data\\"
    # doc_path = "E:\\doc_finish"

    docx_path = "E:\\docx_data"
    doc_more_file_path = "E:\\doc_more\\"

    doc_year = 2018

    main(doc_path, docx_path, doc_year, doc_finish, doc_more_file_path)

    # partition_page()