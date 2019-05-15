# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from datetime import datetime


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'data/{0}/{1}/{2}/{3}/{4}'.format(datetime.now().strftime("%Y"),
                                             datetime.now().strftime("%m"),
                                             datetime.now().strftime("%d"),
                                             datetime.now().strftime("%Y-%m-%d-%H-%M-%S-%f"), filename)


class HandOutList(models.Model):
    """成果分发清单表"""
    title = models.CharField(max_length=5000, blank=True, null=True, verbose_name=u"分发单标题")
    signer = models.CharField(max_length=1000, blank=True, null=True, verbose_name=u"签发")
    name = models.CharField(max_length=5000, blank=True, null=True, verbose_name=u"分发单名称")
    uniquenum = models.CharField(max_length=5000, unique=True, error_messages={"unique": u"分发单已存在"},
                                 verbose_name=u"分发单唯一编号")
    listnum = models.CharField(max_length=1000, null=True, blank=True, verbose_name=u"编号")
    auditnum = models.CharField(max_length=1000, null=True, blank=True, verbose_name=u"审核编号")
    # secretlevel = models.CharField(max_length=2000, null=True, blank=True, verbose_name=u"分发单秘密级别")
    secrecyagreementnum = models.CharField(max_length=2000, null=True, blank=True, verbose_name=u"保密责任书编号")
    purpose = models.CharField(max_length=2000, null=True, blank=True, verbose_name=u"用途")
    sendunit = models.CharField(max_length=5000, null=True, blank=True, verbose_name=u"发出单位")
    sendunitaddr = models.CharField(max_length=5000, null=True, blank=True, verbose_name=u"发出单位通讯地址")
    sendunitpostcode = models.CharField(max_length=1000, null=True, blank=True, verbose_name=u"发出单位邮政编码")
    receiveunit = models.CharField(max_length=5000, null=True, blank=True, verbose_name=u"接收单位")
    receiveunitaddr = models.CharField(max_length=5000, null=True, blank=True, verbose_name=u"接收单位通讯地址")
    receiveunitpostcode = models.CharField(max_length=1000, null=True, blank=True, verbose_name=u"接收单位邮政编码")
    handler = models.CharField(max_length=1000, null=True, blank=True, verbose_name=u"经办人")
    handlerphonenum = models.CharField(max_length=1000, null=True, blank=True, verbose_name=u"经办人联系电话(座机)")
    handlermobilephonenum = models.CharField(max_length=1000, null=True, blank=True, verbose_name=u"经办人联系电话(手机)")
    receiver = models.CharField(max_length=5000, null=True, blank=True, verbose_name=u"接收人")
    receiverphonenum = models.CharField(max_length=1000, null=True, blank=True, verbose_name=u"接收人联系电话(座机)")
    receivermobilephonenum = models.CharField(max_length=1000, null=True, blank=True, verbose_name=u"接收人联系电话(手机)")
    # handovertime = models.DateTimeField(null=True, blank=True, verbose_name=u"交接日期")
    sendouttimec = models.CharField(max_length=1000, null=True, blank=True, verbose_name=u"发出日期")
    recievetimec = models.CharField(max_length=1000, null=True, blank=True, verbose_name=u"接收日期")
    sendouttime = models.DateTimeField(null=True, blank=True, verbose_name=u"发出日期")
    recievetime = models.DateTimeField(null=True, blank=True, verbose_name=u"接收日期")
    # 承办参谋 staffofficer
    # undertaker = models.CharField(max_length=1000, null=True, blank=True, verbose_name=u"承办参谋")
    # 递送方式 自取、邮寄、网络、送往、其他__
    selfgetway = models.BooleanField(default=False, verbose_name=u"递送方式为自取")
    postway = models.BooleanField(default=False, verbose_name=u"递送方式为邮寄")
    networkway = models.BooleanField(default=False, verbose_name=u"递送方式为网络")
    sendtoway = models.BooleanField(default=False, verbose_name=u"递送方式为送往")
    signature = models.CharField(max_length=5000, null=True, blank=True, verbose_name=u"递送方式后面的签名")
    papermedia = models.BooleanField(default=False, verbose_name=u"纸质介质")
    cdmedia = models.BooleanField(default=False, verbose_name=u"光盘介质")
    diskmedia = models.BooleanField(default=False, verbose_name=u"硬盘介质")
    networkmedia = models.BooleanField(default=False, verbose_name=u"网络介质")
    othermedia = models.BooleanField(default=False, verbose_name=u"其他介质")
    # othermediadetail = models.BooleanField(max_length=2000, null=True, blank=True, verbose_name=u"其他介质详情")
    medianums = models.CharField(max_length=5000, null=True, blank=True, verbose_name=u"介质编号")
    mapnums = models.TextField(null=True, blank=True, verbose_name=u"分发单包含的成果的图幅号")
    filename = models.CharField(max_length=5000, null=True, blank=True, verbose_name=u"分发单文件名字")
    file = models.FileField(upload_to=user_directory_path, max_length=5000, null=True, blank=True,
                            verbose_name=u"分发单文件路径")
    createtime = models.DateTimeField(auto_now_add=True, null=True, blank=True, verbose_name=u"创建时间")
    updatetime = models.DateTimeField(auto_now=True, null=True, blank=True, verbose_name=u"更新时间")

    class Meta:
        verbose_name = u"成果分发清单表"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class FileInfo(models.Model):
    """成果资料信息表"""
    name = models.CharField(max_length=5000, verbose_name=u"成果资料名称")
    resultnum = models.CharField(max_length=2000, null=True, blank=True, verbose_name=u"成果数量")
    datasize = models.CharField(max_length=1000, null=True, blank=True, verbose_name=u"成果数据量")
    # 格式或者介质,介质类型:纸质,光盘(要填写介质编号),硬盘(填写介质编号),网络,其他______
    formatormedia = models.CharField(max_length=1000, null=True, blank=True, verbose_name=u"格式/介质")
    # papermedia = models.BooleanField(default=False, verbose_name=u"纸质介质")
    # cdmedia = models.BooleanField(default=False, verbose_name=u"光盘介质")
    # cdmedianum = models.CharField(max_length=2000, null=True, blank=True, verbose_name=u"光盘介质编号")
    # diskmedia = models.BooleanField(default=False, verbose_name=u"硬盘介质")
    # diskmedianum = models.CharField(max_length=2000, null=True, blank=True, verbose_name=u"硬盘介质编号")
    # networkmedia = models.BooleanField(default=False, verbose_name=u"网络介质")
    # othermedia = models.BooleanField(default=False, verbose_name=u"其他介质")
    # othermedianum = models.CharField(max_length=5000, null=True, blank=True, verbose_name=u"其他介质编号")
    # mediumnum = models.CharField(max_length=1000, null=True, verbose_name=u"介质编号")
    # resultyear = models.CharField(max_length=1000, null=True, blank=True, verbose_name=u"成果年代")
    secretlevel = models.CharField(max_length=1000, null=True, blank=True, verbose_name=u"成果秘密级别")
    # handoutlist_name = models.CharField(max_length=5000, verbose_name=u"该成果所属清单")
    remarks = models.CharField(max_length=5000, null=True, blank=True, verbose_name=u"成果资料备注")
    handoutlist_uniquenum = models.CharField(max_length=5000, verbose_name=u"分发单唯一编号")
    createtime = models.DateTimeField(auto_now_add=True, null=True, blank=True, verbose_name=u"创建时间")
    updatetime = models.DateTimeField(auto_now=True, null=True, blank=True, verbose_name=u"更新时间")

    class Meta:
        verbose_name = u"成果资料信息表"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class UploadDoc(models.Model):
    file = models.FileField(upload_to=user_directory_path, max_length=5000, null=True, blank=True,
                            verbose_name=u"分发单文件路径")
    handoutlist_uniquenum = models.CharField(max_length=5000, verbose_name=u"分发单唯一编号")
    createtime = models.DateTimeField(auto_now_add=True, null=True, blank=True, verbose_name=u"创建时间")
    updatetime = models.DateTimeField(auto_now=True, null=True, blank=True, verbose_name=u"更新时间")

    class Meta:
        verbose_name = u"分发单文件"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.handoutlist_uniquenum


# class FilePath(models.Model):
#     """成果文件路径表"""
#     filepath = models.TextField(null=True, blank=True, verbose_name=u"成果文件路径")
#     fileinfo_name = models.CharField(max_length=5000, null=True, blank=True, verbose_name=u"成果资料名称")
#     handoutlist_name = models.CharField(max_length=5000, null=True, blank=True, verbose_name=u"该成果所属清单")
#     createtime = models.DateTimeField(auto_now_add=True, null=True, blank=True, verbose_name=u"创建时间")
#     updatetime = models.DateTimeField(auto_now=True, null=True, blank=True, verbose_name=u"更新时间")
#
#     class Meta:
#         verbose_name = u"成果文件路径表"
#         verbose_name_plural = verbose_name
#
#     def __str__(self):
#         return self.filepath


"""
class EchartReceiveunit(models.Model):
    receiveunit = models.CharField(max_length = 128, null=True, blank=True, verbose_name="接收单位")
    count = models.IntegerField(null=True, blank=True, verbose_name=u"数量")

    class Meta:
        verbose_name = u"接收单位Echart"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.receiveunit

class EchartReceiveTime(models.Model):
    sendouttime = models.CharField(max_length = 128, null=True, blank=True, verbose_name=u"创建时间")
    count = models.IntegerField(null=True, blank=True, verbose_name=u"数量")

    class Meta:
        verbose_name = u"发出日期Echart"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.sendouttime
"""


class HandoutlistExcel(models.Model):
    excelmark = models.CharField(max_length=2000,unique=True, verbose_name=u"excel标记")
    excelfile = models.FileField(upload_to=user_directory_path,max_length=2000, null=True, blank=True, verbose_name=u"excel文件")
    createtime = models.DateTimeField(auto_now_add=True, null=True, blank=True, verbose_name=u"创建时间")
    updatetime = models.DateTimeField(auto_now=True, null=True, blank=True, verbose_name=u"更新时间")

    def __str__(self):
        return self.excelfile
