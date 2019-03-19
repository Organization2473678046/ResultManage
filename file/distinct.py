# -*- coding: utf-8 -*-
import os

# 根据传入的路径进行拼接
# def join_filedir(path):
#     path_list1 = path.split('/')
#     # print path_list1
#     path_list2 = []
#     for i in range(len(path_list1)-1):
#         path_list3 = []
#         temp_path = ''
#         for path1 in path_list1[:len(path_list1) - i]:
#             path_list3.append(path1)
#             temp_path = '/'.join(path_list3)
#         path_list2.append(temp_path)
#     return path_list2
#     # return file_dir





def join_filedir(path,searchword):
    path_list1 = path.split('/')
    # print path_list1
    path_list2 = []
    for i in range(len(path_list1)-1):
        path_list3 = []
        temp_path = ''
        for path1 in path_list1[:len(path_list1) - i]:
            path_list3.append(path1)
        path_list4 = path_list3[::-1]
        # print path_list4
        # [u'Source', u'tasktemplate', u'celery_app', u'RGSManager', u'PycharmProjects', u'D:']
        # [u'tasktemplate', u'celery_app', u'RGSManager', u'PycharmProjects', u'D:']
        # [u'celery_app', u'RGSManager', u'PycharmProjects', u'D:']
        # [u'RGSManager', u'PycharmProjects', u'D:']
        # [u'PycharmProjects', u'D:']
        path_list6 = []
        for path3 in path_list4:
            if searchword in path3:
                path3_index = path_list4.index(path3)
                path_list5 = path_list4[path3_index:]
                # print path_list5
                path_list6 = path_list5[::-1]
                break

        if path_list6 == []:
            break
        print path_list6
        temp_path = '/'.join(path_list6)
        path_list2.append(temp_path)
    return path_list2


if __name__ == '__main__':
    filepath_li = [u'E:/E盘文件/pg自动备份/数据库备份', u'E:/E盘文件/pg自动备份',
                   u'E:/E盘文件/下载的任务包/110000BJ/110000BJ_L5_TM_1990',
                   u'E:/E盘文件/下载的任务包/110000BJ/110000BJ_L5_TM_1990',
                   u'E:/E盘文件/下载的任务包/110000BJ/110000BJ_L5_TM_1990',
                   u'E:/E盘文件/下载的任务包/110000BJ/110000BJ_L5_TM_1990', u'E:/E盘文件/下载的任务包/110000BJ/110000BJ_L5_TM_1990',
                   u'E:/E盘文件/下载的任务包/110000BJ/110000BJ_L5_TM_1990', u'E:/E盘文件/下载的任务包/110000BJ/110000BJ_L5_TM_1990',
                   u'E:/E盘文件/下载的任务包/', u'E:/E盘文件/下载的任务包', u'E:/E盘文件/下载的任务包', u'E:/E盘文件/下载的任务包', u'E:/E盘文件/下载的任务包',
                   u'E:/E盘文件/下载的任务包', u'E:/E盘文件/下载的任务包', u'E:/E盘文件/下载的任务包', u'E:/E盘文件/下载的任务包', u'E:/E盘文件/下载的任务包',
                   u'E:/E盘文件/下载的任务包', u'E:/E盘文件/下载的任务包', u'E:/E盘文件/下载的任务包', u'E:/E盘文件/下载的任务包']


    # list1 = join_filedir(u'E:/E盘文件/pg自动备份/数据库备份/计划任务设置.txt')
    list1 = join_filedir(u'D:/PycharmProjects/RGSManager/celery_app/tasktemplate/Source','app')
    print list1
    list = [u'D:', u'PycharmProjects', u'RGSManager', u'celery_app']
    # print '/'.join(list)
    pass
