# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os
from rest_framework.filters import SearchFilter
import operator
from functools import reduce
from django.db import models
from django.utils import six
from file.utils.get_dir_list import get_filedir_list

from rest_framework.compat import (
    distinct
)


class FileSearchFilter(SearchFilter):

    def get_search_terms(self, request):
        """
        Search terms are set by a ?search=... query parameter,
        and may be comma and/or whitespace delimited.
        """
        params = request.query_params.get(self.search_param, '')
        # return params.replace(',', ' ').split()

        self.params = params.replace(',', ' ').split()
        return self.params
    def filter_queryset(self, request, queryset, view):
        search_fields = getattr(view, 'search_fields', None)
        search_terms = self.get_search_terms(request)

        if not search_fields or not search_terms:
            return queryset

        orm_lookups = [
            self.construct_search(six.text_type(search_field))
            for search_field in search_fields
        ]

        base = queryset
        conditions = []
        for search_term in search_terms:
            queries = [
                models.Q(**{orm_lookup: search_term})
                for orm_lookup in orm_lookups
            ]
            conditions.append(reduce(operator.or_, queries))
        queryset = queryset.filter(reduce(operator.and_, conditions))

        if self.must_call_distinct(queryset, search_fields):
            # Filtering against a many-to-many field requires us to
            # call queryset.distinct() in order to avoid duplicate items
            # in the resulting queryset.
            # We try to avoid this if possible, for performance reasons.
            queryset = distinct(queryset, base)

        # 根据搜索条件过滤之后的查询集
        print queryset
        # 搜索关键字参数 search
        print self.search_param
        # 传过来的搜索关键词
        print self.params[0]
        print self.params
        print len(queryset)

        # 说明查到了结果
        if len(queryset) > 0:
            temp_filedir_list = []
            for resultfile in queryset:
                # 如果只包括名字中包含关键词的目录
                # filedir = os.path.dirname(resultfile.filepath)
                # 如果要包括名字中包含关键词的文件
                filedir = resultfile.filepath
                # # filedir = filedir.encode('utf-8')
                # # filedir = filedir.replace('\\','/')
                # filedir_list = filedir.split('\\')
                # # print filedir_list
                # temp1 = '/'.join(filedir_list[4:])
                # temp2 = '\\'.join(filedir_list[:4])
                # temp = temp2+'/'+temp1
                # # print temp
                # print temp.split('/')

                # filedir = os.path.normpath(filedir)
                print filedir

                resultfile_dirlist = get_filedir_list(filedir, self.params)
                temp_filedir_list += resultfile_dirlist
            # 去重
            temp_filedir_list = list(set(temp_filedir_list))

            filedir_list = []
            for filedir in temp_filedir_list:
                filedir = filedir.replace('/','\\',1)
                filedir = filedir.replace('/','',1)
                # filedir = filedir.replace('/','\\',1)

                filedir_list.append(filedir)
            # 排序
            filedir_list.sort()
            # 然后再将没有搜索关键词的项删除
            # filedir_list = []
            # for filedir in temp_filedir_list:
            #     if self.params[0] in filedir:
            #         filedir_list.append(filedir)
            print filedir_list
            return filedir_list
        # 没有查到结果
        return queryset

