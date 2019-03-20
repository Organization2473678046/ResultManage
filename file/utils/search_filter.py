# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import operator
from functools import reduce
from django.db import models
from django.db.models.constants import LOOKUP_SEP
from django.template import loader
from django.utils import six
from django.utils.encoding import force_text
from django.utils.translation import ugettext_lazy as _
from file.utils.get_dir_list import get_filedir_list

from rest_framework.compat import (
    coreapi, coreschema, distinct
)
from rest_framework.settings import api_settings
from rest_framework.filters import BaseFilterBackend


class FileSearchFilter(BaseFilterBackend):
    # The URL query parameter used for the search.
    search_param = api_settings.SEARCH_PARAM
    template = 'rest_framework/filters/search.html'
    lookup_prefixes = {
        '^': 'istartswith',
        '=': 'iexact',
        '@': 'search',
        '$': 'iregex',
    }
    search_title = _('Search')
    search_description = _('A search term.')

    def get_search_terms(self, request):
        """
        Search terms are set by a ?search=... query parameter,
        and may be comma and/or whitespace delimited.
        """
        params = request.query_params.get(self.search_param, '')
        # return params.replace(',', ' ').split()

        self.params = params.replace(',', ' ').split()
        return self.params

    def construct_search(self, field_name):
        lookup = self.lookup_prefixes.get(field_name[0])
        if lookup:
            field_name = field_name[1:]
        else:
            lookup = 'icontains'
        return LOOKUP_SEP.join([field_name, lookup])

    def must_call_distinct(self, queryset, search_fields):
        """
        Return True if 'distinct()' should be used to query the given lookups.
        """
        for search_field in search_fields:
            opts = queryset.model._meta
            if search_field[0] in self.lookup_prefixes:
                search_field = search_field[1:]
            parts = search_field.split(LOOKUP_SEP)
            for part in parts:
                field = opts.get_field(part)
                if hasattr(field, 'get_path_info'):
                    # This field is a relation, update opts to follow the relation
                    path_info = field.get_path_info()
                    opts = path_info[-1].to_opts
                    if any(path.m2m for path in path_info):
                        # This field is a m2m relation so we know we need to call distinct
                        return True
        return False

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
        if len(queryset) != 0:
            temp_filedir_list = []
            for resultfile in queryset:
                # 如果只包括名字中包含关键词的目录
                # filedir = os.path.dirname(resultfile.filepath)
                # 如果要包括名字中包含关键词的文件
                filedir = resultfile.filepath

                # resultfile_dirlist = get_filedir_list2(filedir, self.params)
                resultfile_dirlist = get_filedir_list(filedir, self.params)
                temp_filedir_list += resultfile_dirlist

            # 去重
            temp_filedir_list = list(set(temp_filedir_list))
            # 排序
            temp_filedir_list.sort()
            # 然后在没有搜索关键词的项删除
            # filedir_list = []
            # for filedir in temp_filedir_list:
            #     if self.params[0] in filedir:
            #         filedir_list.append(filedir)
            return temp_filedir_list
        # 没有查到结果
        return queryset


    def to_html(self, request, queryset, view):
        if not getattr(view, 'search_fields', None):
            return ''

        term = self.get_search_terms(request)
        term = term[0] if term else ''
        context = {
            'param': self.search_param,
            'term': term
        }
        template = loader.get_template(self.template)
        return template.render(context)


    def get_schema_fields(self, view):
        assert coreapi is not None, 'coreapi must be installed to use `get_schema_fields()`'
        assert coreschema is not None, 'coreschema must be installed to use `get_schema_fields()`'
        return [
            coreapi.Field(
                name=self.search_param,
                required=False,
                location='query',
                schema=coreschema.String(
                    title=force_text(self.search_title),
                    description=force_text(self.search_description)
                )
            )
        ]


if __name__ == '__main__':
    pass
