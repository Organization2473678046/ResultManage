
def tables_2018(document, cursor, date_now):
    p = 1
    name = ""       # 成果资料名称
    secretlevel = ""    # 成果秘密级别
    resultnum = ""      # 成果数量
    datasize = ""       # 成果数据量
    formatormedia = ""  # 格式/介质
    remarks = ""        # 成果资料备注
    handoutlist_uniquenum = ""  # 分发单唯一编号


    # 读取表格

    tables = document.tables
    table = tables[0]
    for i in table.rows:
        table_list = []
        for x in i.cells:
            table_list.append(x.text)
        name = table_list[1]
        secretlevel = table_list[2]
        resultnum = table_list[3]
        datasize = table_list[4]
        formatormedia = table_list[5]
        remarks = table_list[6]
        handoutlist_uniquenum = date_now

        if p == 1:
            p = 2
        else:
            print(table_list)
            row2 = (name, secretlevel, resultnum, datasize, formatormedia, remarks, handoutlist_uniquenum)
            cursor.execute("INSERT INTO book_fileinfo (name, secretlevel, resultnum, datasize, formatormedia, remarks, handoutlist_uniquenum) VALUES (?, ?, ?, ?, ?, ?, ?)", row2)

