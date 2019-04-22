# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

"""
class ResultFile(models.Model):
    # 成果文件路径表
    # db_index=True 为该字段创建索引
    filepath = models.TextField(verbose_name=u"成果文件路径")
    serverIP = models.CharField(max_length=500, null=True, verbose_name=u"所属服务器")
    filesize  = models.FloatField(null=True,verbose_name="文件大小,单位: MB")
    filecreatetime = models.DateTimeField(null=True,verbose_name=u"文件创建时间")
    fileupdatetime = models.DateTimeField(null=True,verbose_name=u"文件更新时间")
    dirlength = models.IntegerField(null=True, verbose_name=u"目录深度")
    dirdepth = models.IntegerField(null=True, verbose_name=u"目录深度")

    class Meta:
        verbose_name = u"成果文件路径"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.filepath
"""


class HandOutList(models.Model):
    """成果分发清单表"""
    name = models.CharField(max_length=5000,unique=True, error_messages={"unique": u"名称已存在"},verbose_name=u"成果交付清单名称")
    listnum = models.CharField(max_length=1000, null=True,blank=True, verbose_name=u"清单受理编号")
    auditnum = models.CharField(max_length=1000, null=True,blank=True, verbose_name=u"审核编号")
    # 密级
    secretlevel = models.CharField(max_length=2000, null=True,blank=True, verbose_name=u"清单秘密级别")
    # 格式或者介质,介质类型:纸质,光盘(要填写介质编号),硬盘(填写介质编号),网络,其他______
    # mediumtype = models.CharField(max_length=2000, null=True, verbose_name=u"格式/介质类型"
    purpose = models.CharField(max_length=2000, null=True,blank=True, verbose_name=u"用途")
    receiveunit = models.CharField(max_length=5000, null=True,blank=True, verbose_name=u"接收单位")
    receiver = models.CharField(max_length=5000, null=True,blank=True, verbose_name=u"接收人")
    receiverinfo = models.CharField(max_length=5000, null=True,blank=True, verbose_name=u"接收人联系方式")
    handovertime = models.DateTimeField(null=True,blank=True, verbose_name=u"交接日期")
    recievetime = models.DateTimeField(null=True,blank=True, verbose_name=u"接收日期")
    # 承办参谋 staffofficer
    undertaker = models.CharField(max_length=1000, null=True,blank=True, verbose_name=u"承办参谋")
    # 递送方式 自取、邮寄、网络、送往、其他__
    # deliveryway = models.CharField(max_length=2000, null=True, verbose_name=u"递送方式")
    selfgetway = models.BooleanField(default=False,verbose_name=u"递送方式为自取")
    postway = models.BooleanField(default=False,verbose_name=u"递送方式为邮寄")
    networkway = models.BooleanField(default=False,verbose_name=u"递送方式为网络")
    deliverway = models.BooleanField(default=False,verbose_name=u"递送方式为送往")
    otherway = models.BooleanField(default=False,verbose_name=u"递送方式为其他")
    otherwaydetail = models.CharField(max_length=1000,null=True,blank=True,verbose_name=u"其他递送方式详细信息")
    handler = models.CharField(max_length=1000, null=True,blank=True, verbose_name=u"清单经办人")
    createtime = models.DateTimeField(auto_now_add=True, verbose_name=u"创建时间")
    updatetime = models.DateTimeField(auto_now=True, verbose_name=u"更新时间")

    class Meta:
        verbose_name = u"成果分发清单表"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class FileInfo(models.Model):
    """成果资料信息表"""
    name = models.CharField(max_length=5000, verbose_name=u"成果资料名称")
    resulttype = models.CharField(max_length=5000, null=True,blank=True, verbose_name=u"成果类型")
    num = models.CharField(max_length=2000,null=True,blank=True, verbose_name=u"成果数量")
    datasize = models.CharField(max_length=1000, null=True,blank=True, verbose_name=u"成果数据量GB")
    # 格式或者介质,介质类型:纸质,光盘(要填写介质编号),硬盘(填写介质编号),网络,其他______
    # mediumtype = models.CharField(max_length=1000, null=True, verbose_name=u"格式/介质类型")
    papermedia = models.BooleanField(default=False,verbose_name=u"纸质介质")
    cdmedia = models.BooleanField(default=False,verbose_name=u"光盘介质")
    cdmedianum = models.CharField(max_length=2000,null=True,blank=True,verbose_name=u"光盘介质编号")
    diskmedia = models.BooleanField(default=False,verbose_name=u"硬盘介质")
    diskmedianum = models.CharField(max_length=2000,null=True,blank=True,verbose_name=u"硬盘介质编号")
    networkmedia = models.BooleanField(default=False,verbose_name=u"网络介质")
    othermedia = models.BooleanField(default=False,verbose_name=u"其他介质")
    othermedianum = models.CharField(max_length=5000,null=True,blank=True,verbose_name=u"其他介质编号")
    # mediumnum = models.CharField(max_length=1000, null=True, verbose_name=u"介质编号")
    resultyear = models.CharField(max_length=1000, null=True,blank=True, verbose_name=u"成果年代")
    secretlevel = models.CharField(max_length=1000, null=True,blank=True, verbose_name=u"成果秘密级别")
    handoutlist_name = models.CharField(max_length=5000, verbose_name=u"该成果所属清单")
    createtime = models.DateTimeField(auto_now_add=True, verbose_name=u"创建时间")
    updatetime = models.DateTimeField(auto_now=True, verbose_name=u"更新时间")

    class Meta:
        verbose_name = u"成果资料信息表"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class FilePath(models.Model):
    """成果文件路径表"""
    filepath = models.TextField(null=True,blank=True, verbose_name=u"成果文件路径")
    fileinfo_name = models.CharField(max_length=5000, null=True,blank=True, verbose_name=u"成果资料名称")
    handoutlist_name = models.CharField(max_length=5000, null=True,blank=True, verbose_name=u"该成果所属清单")
    createtime = models.DateTimeField(auto_now_add=True, null=True,blank=True, verbose_name=u"创建时间")
    updatetime = models.DateTimeField(auto_now=True, null=True,blank=True, verbose_name=u"更新时间")

    class Meta:
        verbose_name = u"成果文件路径表"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.filepath
