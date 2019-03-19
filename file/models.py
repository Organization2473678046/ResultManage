# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from rest_framework.serializers import ModelSerializer

@python_2_unicode_compatible
class ResultFile(models.Model):
    filepath = models.TextField(verbose_name=u"成果文件路径")
    serverIP = models.CharField(max_length = 128, null=True, verbose_name=u"所属服务器")

    class Meta:
        verbose_name = u"成果文件"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.filepath


class ResultFileSerializer(ModelSerializer):

    class Meta:
        model = ResultFile
        fields = ["id", "filepath", "serverIP"]