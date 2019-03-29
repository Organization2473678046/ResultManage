# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from haystack import indexes

from file.models import ResultFile

class ResultFileIndex(indexes.SearchIndex, indexes.Indexable):
    """
    ResultFile索引数据模型类
    """
    text = indexes.CharField(document=True, use_template=True)

    def get_model(self):
        """返回建立索引的模型类"""
        return ResultFile

    def index_queryset(self, using=None):
        """返回要建立索引的数据查询集"""
        return self.get_model().objects.all()
