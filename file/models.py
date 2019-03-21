# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class ResultFile(models.Model):
    filepath = models.TextField(verbose_name=u"成果文件路径")
    serverIP = models.CharField(max_length=500, null=True, verbose_name=u"所属服务器")
    dirlength = models.IntegerField(null=True,verbose_name=u"目录深度")
    dirdepth = models.IntegerField(null=True,verbose_name=u"目录深度")


    class Meta:
        verbose_name = u"成果文件"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.filepath


