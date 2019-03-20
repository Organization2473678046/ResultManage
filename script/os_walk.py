# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
import os
# li = os.walk("D:\PycharmProjects")
li = os.walk("D:/")
# print li
#
# for maindir, subdir, file_name_list in li:
#     print maindir
#     print subdir
#     print file_name_list
#

if __name__ == '__main__':
    abc =  "\\192.168.3.120\\def/abc/apache/Re_Loader_Activator_XP85/Re_Loader_Activator_XP85/SetupComplete.cmd"
    # li = abc.rsplit('/',2)
    # print li
    temp = '\\192.168.3.120\\新建文件夹/120转180所需安装包/apache/httpd-2.4.6-win32-VC9/Apache24/bin/iconv_tbl_simple.so'

    import re
    temp1 = re.sub(r'\\','/',temp)
    print temp1