# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
import os
# li = os.walk("D:\PycharmProjects")
li = os.walk("D:/")
print li

for maindir, subdir, file_name_list in li:
    print maindir
    print subdir
    print file_name_list


