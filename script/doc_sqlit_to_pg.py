import psycopg2
import sqlite3


def get_sqlit_data(db_name, cur_pg):
    conn = sqlite3.connect(db_name)
    cur_sqlit = conn.cursor()
    cur_sqlit.execute("select * from results_handoutlist")
    while True:
        data = cur_sqlit.fetchone()
        if data:
            title = data[1]  # 分发单标题
            signer = data[2]  # 签发
            name = data[3]  # 分发单名称
            uniquenum = data[4]  # 分发单唯一编号
            listnum = data[5]  # 编号
            auditnum = data[6]  # 审核编号
            secrecyagreementnum = data[7]  # 保密责任书编号
            purpose = data[8]  # 用途
            sendunit = data[9]  # 发出单位
            sendunitaddr = data[10]  # 发出单位通讯地址
            sendunitpostcode = data[11]  # 发出单位邮政编码
            receiveunit = data[12]  # 接收单位
            receiveunitaddr = data[13]  # 接收单位通讯地址
            receiveunitpostcode = data[14]  # 接收单位邮政编码
            handler = data[15]  # 经办人
            handlerphonenum = data[16]  # 经办人联系电话(座机)
            handlermobilephonenum = data[17]  # 经办人联系电话(手机)
            receiver = data[18]  # 接收人
            receiverphonenum = data[19]  # 接收人联系电话(座机)
            receivermobilephonenum = data[20]  # 接收人联系电话(手机)
            sendouttime = data[21]  # 发出日期
            recievetime = data[22]  # 接收日期
            selfgetway = True if data[23] == 1 else False  # 递送方式为自取
            postway = True if data[24] == 1 else False  # 递送方式为邮寄
            networkway = True if data[25] == 1 else False  # 递送方式为网络
            sendtoway = True if data[26] == 1 else False  # 递送方式为送往
            signature = data[27]  # 递送方式后面的签名
            papermedia = True if data[28] == 1 else False  # 纸质介质
            cdmedia = True if data[29] == 1 else False  # 光盘介质
            diskmedia = True if data[30] == 1 else False  # 硬盘介质
            networkmedia = True if data[31] == 1 else False  # 网络介质
            othermedia = True if data[32] == 1 else False  # 其他介质
            medianums = data[33]  # 介质编号
            mapnums = data[34]  # 分发单包含的成果的图幅号
            filename = data[35]  # 分发单文件名字
            file = data[36]  # 分发单文件路径


            cur_pg.execute(
                "INSERT INTO results_handoutlist (title, signer, name, uniquenum, listnum, auditnum, secrecyagreementnum, purpose, sendunit, sendunitaddr, sendunitpostcode, receiveunit, receiveunitaddr, receiveunitpostcode, handler, handlerphonenum, handlermobilephonenum, receiver, receiverphonenum, receivermobilephonenum, sendouttime, recievetime, selfgetway, postway, networkway, sendtoway, signature, papermedia, cdmedia, diskmedia, networkmedia, othermedia, medianums, mapnums, filename, file) VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', %r, %r, %r, %r, '%s', %r, %r, %r,  %r,  %r, '%s', '%s', '%s', '%s')"% (title, signer, name, uniquenum, listnum, auditnum, secrecyagreementnum, purpose, sendunit, sendunitaddr, sendunitpostcode, receiveunit, receiveunitaddr, receiveunitpostcode, handler, handlerphonenum, handlermobilephonenum, receiver, receiverphonenum, receivermobilephonenum, sendouttime, recievetime, selfgetway, postway, networkway, sendtoway, signature, papermedia, cdmedia, diskmedia, networkmedia, othermedia, medianums, mapnums, filename, file))
        else:
            break

    cur_sqlit.execute("select * from results_fileinfo")
    while True:
        data = cur_sqlit.fetchone()
        if data:
            name = data[1]
            secretlevel = data[2]
            resultnum = data[3]
            datasize = data[4]
            formatormedia = data[5]
            remarks = data[6]
            handoutlist_uniquenum = data[7]

            cur_pg.execute(
                "INSERT INTO results_fileinfo (name, secretlevel, resultnum, datasize, formatormedia, remarks, handoutlist_uniquenum) VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s')"% (name, secretlevel, resultnum, datasize, formatormedia, remarks, handoutlist_uniquenum))
        else:
            break



def pg_conn(db_name):
    conn = psycopg2.connect(dbname=u"resmanagev0.3",
                            user=u"postgres",
                            password=u"Lantucx2018",
                            host=u"localhost",
                            port=u"5432")
    cur_pg = conn.cursor()

    get_sqlit_data(db_name, cur_pg)

    conn.commit()
    conn.close()


def main(db_name):
    pg_conn(db_name)


if __name__ == '__main__':
    db_name = "doc_sqlit.db"
    main(db_name)
