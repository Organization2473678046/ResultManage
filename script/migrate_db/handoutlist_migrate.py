# -*- coding: utf-8 -*-
import os
import sys
import psycopg2


def get_handoutlist_data(tablename):
    # 获取分发单表数据
    conn = psycopg2.connect(dbname="resmanagev2019.05.10",
                            user="postgres",
                            password="Lantucx2018",
                            host="localhost",
                            port="5432")
    cur = conn.cursor()
    sql = u"select id,title,signer,name,uniquenum,listnum,auditnum,secrecyagreementnum,purpose,sendunit, sendunitaddr,sendunitpostcode,receiveunit,receiveunitaddr,   receiveunitpostcode, handler,handlerphonenum,handlermobilephonenum,receiver,receiverphonenum, receivermobilephonenum, sendouttime,recievetime,selfgetway, postway,networkway,sendtoway,signature,papermedia,cdmedia, diskmedia, networkmedia, othermedia,medianums,mapnums,filename,file,createtime,updatetime from results_handoutlist order_by id"
    cur.execute(sql)
    while True:
        data = cur.fetchone()
        if data:
            print(data)
            handoutlist_insert(data)
        else:
            conn.close()
            return



def handoutlist_insert(data):
    """results_handoutlist表数据的迁移"""
    conn = psycopg2.connect(dbname="resmanagev2019.05.10",
                            user="postgres",
                            password="Lantucx2018",
                            host="localhost",
                            port="5432")

    data_list = list(data)
    for data in data_list[1:-2]:
        if data is None or data == "None":
            data_list[data_list.index(data)] = ""

    title = data_list[1]
    signer = data_list[2]
    name = data_list[3]
    uniquenum = data_list[4]
    listnum = data_list[5]
    auditnum = data_list[6]
    secrecyagreementnum = data_list[7]
    purpose = data_list[8]
    sendunit = data_list[9]
    sendunitaddr = data_list[10]
    sendunitpostcode = data_list[11]
    receiveunit = data_list[12]
    receiveunitaddr = data_list[13]
    receiveunitpostcode = data_list[14]
    handler = data_list[15]
    handlerphonenum = data_list[16]
    handlermobilephonenum = data_list[17]
    receiver = data_list[18]
    receiverphonenum = data_list[19]
    receivermobilephonenum = data_list[20]
    sendouttime_str= data_list[21]
    recievetime_srt = data_list[22]
    sendouttime = sendouttime_str
    recievetime = recievetime_srt
    sendouttimec = sendouttime_str.split("-")[0]+"年"+sendouttime_str.split("-")[1]+"月"+sendouttime_str.split("-")[2]+"日"
    recievetimec =recievetime_srt.split("-")[0]+"年"+recievetime_srt.split("-")[1]+"月"+recievetime_srt.split("-")[2]+"日"
    selfgetway = data_list[23]
    postway = data_list[24]
    networkway = data_list[25]
    sendtoway = data_list[26]
    signature = data_list[27]
    papermedia = data_list[28]
    cdmedia = data_list[29]
    diskmedia = data_list[30]
    networkmedia = data_list[31]
    othermedia = data_list[32]
    medianums = data_list[23]
    mapnums = data_list[33]
    filename = data_list[34]
    file = data_list[35]
    createtime = data_list[36]
    updatetime = data_list[37]

    cur = conn.cursor()
    sql = "insert into results_handoutlist (title,signer,name,uniquenum,listnum,auditnum,secrecyagreementnum,purpose,sendunit, sendunitaddr,sendunitpostcode,receiveunit,receiveunitaddr,receiveunitpostcode, handler,handlerphonenum,handlermobilephonenum,receiver,receiverphonenum, receivermobilephonenum, sendouttime,recievetime, sendouttimec,recievetimec,selfgetway, postway,networkway,sendtoway,signature,papermedia,cdmedia, diskmedia, networkmedia, othermedia,medianums,mapnums,filename,file,createtime,updatetime) values ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s',%r,%r,%r,%r,'%s',%r,%r,%r,%r,%r,'%s','%s','%s','%s','%s','%s')"%(title,signer,name,uniquenum,listnum,auditnum,secrecyagreementnum,purpose,sendunit, sendunitaddr,sendunitpostcode,receiveunit,receiveunitaddr,receiveunitpostcode, handler,handlerphonenum,handlermobilephonenum,receiver,receiverphonenum, receivermobilephonenum, sendouttime,recievetime, sendouttimec,recievetimec,selfgetway, postway,networkway,sendtoway,signature,papermedia,cdmedia, diskmedia, networkmedia, othermedia,medianums,mapnums,filename,file,str(createtime),str(updatetime))
    cur.execute(sql)
    conn.commit()
    conn.close()


if __name__ == '__main__':
    # 迁移分发单表
    get_handoutlist_data("results_handoutlist")

    pass
