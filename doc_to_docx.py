from win32com import client as wc




def doc_docx(path_new, path_old):
    # doc转换docx
    word = wc.Dispatch('Word.Application')
    doc = word.Documents.Open(path_old)  # 目标路径下的文件
    doc.SaveAs(path_new, 12, False, "", True, "", False, False, False, False)  # 转化后路径下的文件
    doc.Close()
    word.Quit()
#
#
#
#
# if __name__ == '__main__':
#     path_old = "E:\\分发单模板.doc"
#     path_new = "E:\\分发单模板.docx"
#     doc_docx(path_new, path_old)

