# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db.models import QuerySet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter,SearchFilter
from file.utils.file_search_filter import FileSearchFilter
from rest_framework import mixins
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response
from django.http import HttpResponse
from file.models import ResultFile
from file.serializers import ResultFileSerializer


class ResultFileViewSetPagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = 'limit'
    max_page_size = 50
    page_query_param = 'page'


class ResultFileViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, GenericViewSet):
    serializer_class = ResultFileSerializer
    queryset = ResultFile.objects.all()
    # pagination_class = ResultFileViewSetPagination
    filter_backends = [FileSearchFilter, DjangoFilterBackend, OrderingFilter]
    # filter_backends = [FileSearchFilter]
    ordering_fields = ("id", "filepath", "serverIP")
    ordering = ("id",)
    search_fields = ('filepath', 'serverIP')

    def filter_queryset(self, queryset):
        """
        Given a queryset, filter it with whichever filter backend is in use.

        You are unlikely to want to override this method, although you may need
        to call it either from a list view, or from a custom `get_object`
        method if you want to apply the configured filtering backend to the
        default queryset.
        """
        flag = self.request.query_params.get("flag")
        if flag:
            self.filter_backends = [SearchFilter, DjangoFilterBackend, OrderingFilter]
        else:
            self.filter_backends = [FileSearchFilter]

        # for backend in list(self.filter_backends):
        #     if backend == OrderingFilter:
        #         if isinstance(queryset, QuerySet):
        #             queryset = backend().filter_queryset(self.request, queryset, self)
        #             self.ordering_fields = ("id", "filepath", "serverIP")
        #             self.ordering = ("id",)
        #         else:
        #             self.ordering_fields = None
        #             self.ordering = None
        #     queryset = backend().filter_queryset(self.request, queryset, self)
        #     return queryset

        for backend in list(self.filter_backends):
            queryset = backend().filter_queryset(self.request, queryset, self)
        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        # 如果返回的是查询集,进行序列化返回
        if isinstance(queryset, QuerySet):
            page = self.paginate_queryset(queryset)
            if page is not None:
                serializer = self.get_serializer(page, many=True)
                return self.get_paginated_response(serializer.data)
            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data)

        # 如果返回的是列表
        page = self.paginate_queryset(queryset)
        if page is not None:
            return self.get_paginated_response(page)
        return Response(queryset)
        # return HttpResponse(queryset)
