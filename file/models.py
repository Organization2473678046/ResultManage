# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class ResultFile(models.Model):
    """成果文件路径表"""
    # db_index=True 为该字段创建索引
    filepath = models.TextField(verbose_name=u"成果文件路径")
    serverIP = models.CharField(max_length=500, null=True, verbose_name=u"所属服务器")
    dirlength = models.IntegerField(null=True, verbose_name=u"目录深度")
    dirdepth = models.IntegerField(null=True, verbose_name=u"目录深度")

    class Meta:
        verbose_name = u"成果文件路径"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.filepath


# @python_2_unicode_compatible
# class MediumType(models.Model):
#     """成果交付清单名称"""
#     name = models.CharField(max_length=5000,verbose_name=u"介质类型")
#     mediumnum = models.CharField(max_length=5000,null=True,verbose_name=u"介质编号")
#     #该介质属于哪个清单
#     handoutlist_name = models.CharField(max_length=5000,verbose_name=u"介质所属清单")
#     resultfile_name = models.CharField(max_length=5000,verbose_name=u"介质所属成果")
#
#
#     class Meta:
#         verbose_name = u"介质类型表"
#         verbose_name_plural = verbose_name
#
#     def __str__(self):
#         return self.name


@python_2_unicode_compatible
class HandOutList(models.Model):
    """成果分发清单表"""
    name = models.CharField(max_length=5000, verbose_name=u"成果交付清单名称")
    listnum = models.CharField(max_length=1000, null=True, verbose_name=u"清单受理编号")
    auditnum = models.CharField(max_length=1000, null=True, verbose_name=u"审核编号")
    # 密级
    secretlevel = models.CharField(max_length=2000, null=True, verbose_name=u"清单秘密级别")
    # 格式或者介质,介质类型:纸质,光盘(要填写介质编号),硬盘(填写介质编号),网络,其他______
    # mediumtype = models.CharField(max_length=2000, null=True, verbose_name=u"格式/介质类型")
    purpose = models.CharField(max_length=2000, null=True, verbose_name=u"用途")
    receiveunit = models.CharField(max_length=5000, null=True, verbose_name=u"接收单位")
    receiver = models.CharField(max_length=5000, null=True, verbose_name=u"接收人")
    receiverinfo = models.CharField(max_length=5000, null=True, verbose_name=u"接收人联系方式")
    handovertime = models.DateTimeField(null=True, verbose_name=u"交接日期")
    recievetime = models.DateTimeField(null=True, verbose_name=u"接收日期")
    # 承办参谋 staffofficer
    undertaker = models.CharField(max_length=1000, null=True, verbose_name=u"承办参谋")
    # 递送方式 自取、邮寄、网络、送往、其他__
    deliveryway = models.CharField(max_length=2000, null=True, verbose_name=u"递送方式")
    handler = models.CharField(max_length=1000, null=True, verbose_name=u"清单经办人")
    createtime = models.DateTimeField(auto_now_add=True, verbose_name=u"创建时间")
    updatetime = models.DateTimeField(auto_now=True, verbose_name=u"更新时间")

    class Meta:
        verbose_name = u"成果分发清单表"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class FileInfo(models.Model):
    """成果资料信息表"""
    name = models.CharField(max_length=5000, unique=True, verbose_name=u"成果资料名称")
    type = models.CharField(max_length=5000, null=True, verbose_name=u"成果类型")
    num = models.IntegerField(null=True, verbose_name=u"成果数量")
    datasize = models.CharField(max_length=1000, null=True, verbose_name=u"成果数据量GB")
    # 格式或者介质,介质类型:纸质,光盘(要填写介质编号),硬盘(填写介质编号),网络,其他______
    mediumtype = models.CharField(max_length=1000, null=True, verbose_name=u"格式/介质类型")
    mediumnum = models.CharField(max_length=1000, null=True, verbose_name=u"介质编号")
    year = models.CharField(max_length=1000, null=True, verbose_name=u"成果年代")
    secretlevel = models.CharField(max_length=1000, null=True, verbose_name=u"成果秘密级别")
    handoutlist_name = models.CharField(max_length=5000, verbose_name=u"该成果所属清单")
    createtime = models.DateTimeField(auto_now_add=True, verbose_name=u"创建时间")
    updatetime = models.DateTimeField(auto_now=True, verbose_name=u"更新时间")

    class Meta:
        verbose_name = u"成果资料信息表"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class FilePath(models.Model):
    """成果文件路径表"""
    filepath = models.TextField(null=True, verbose_name=u"成果文件路径")
    fileinfo_name = models.CharField(max_length=5000, null=True, verbose_name=u"成果资料名称")
    handoutlist_name = models.CharField(max_length=5000, null=True, verbose_name=u"该成果所属清单")
    createtime = models.DateTimeField(auto_now_add=True, null=True, verbose_name=u"创建时间")
    updatetime = models.DateTimeField(auto_now=True, null=True, verbose_name=u"更新时间")

    class Meta:
        verbose_name = u"成果文件路径表"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.filepath
