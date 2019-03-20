# -*- coding: utf-8 -*-


# 根据传入的路径进行拼接
def get_filedir_list(path, search_word_list):
    # path_list1 = path.split('/')
    path_list1 = path.split('\\')
    print path_list1
    path_list2 = []
    # while len(path_list1) > 0:
    while len(path_list1) > 2:
        for search_word in search_word_list:
            if search_word in path_list1[-1]:
                temp_path = '/'.join(path_list1)

                # temp_path = '/'.join(path_list1[2:])
                # temp_path = temp_path.replace('/', '\\', 1)
                # temp_path = '\\' + temp_path

                for search_word in search_word_list:
                    if search_word not in temp_path:
                        break
                else:
                    path_list2.append(temp_path)
                    break
        # else:
        path_list1.pop()

    return path_list2


# def get_filedir_list(path, search_word_list):
#     path_list1 = path.split('/')
#     path_list2 = []
#     while len(path_list1) > 0:
#         if search_word_list in path_list1[-1]:
#             temp_path = '/'.join(path_list1)
#             path_list2.append(temp_path)
#         path_list1.pop()
#     return path_list2

# # print path_list1
# path_list2 = []
# for i in range(len(path_list1) - 1):
#     path_list3 = []
#     temp_path = ''
#     for path1 in path_list1[:len(path_list1) - i]:
#         path_list3.append(path1)
#         temp_path = '/'.join(path_list3)
#     path_list2.append(temp_path)

# return path_list2
# return file_dir


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

    # list1 = get_filedir_list2(u'E:/E盘文件/pg自动备份/数据库备份/计划任务设置.txt')
    list1 = get_filedir_list(u'D:/PycharmProjects/RGSManager/celery_app/tasktemplate/Source', 'app')
    print list1
    list = [u'D:', u'PycharmProjects', u'RGSManager', u'celery_app']
