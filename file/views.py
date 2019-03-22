# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db.models import QuerySet
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework import mixins
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response
from django.http import HttpResponse
from file.models import ResultFile, HandOutList, FileInfo, FilePath
from file.serializers import ResultFileSerializer, HandOutListNameSerializer, HandOutListSerializer,FileInfoSerializer,FilePathSerializer


class ResultFileViewSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'limit'
    max_page_size = 50
    page_query_param = 'page'


class HandOutListViewSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'limit'
    max_page_size = 50
    page_query_param = 'page'


class FileInfoViewSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'limit'
    max_page_size = 50
    page_query_param = 'page'

class FilePathViewSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'limit'
    max_page_size = 50
    page_query_param = 'page'



class ResultFileViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, GenericViewSet):
    """
    list: 获取目录
    """
    serializer_class = ResultFileSerializer
    queryset = ResultFile.objects.all()
    pagination_class = ResultFileViewSetPagination
    filter_backends = [SearchFilter, DjangoFilterBackend, OrderingFilter]
    ordering_fields = ("id", "filepath", "serverIP", "dirlength", "dirdepth")
    ordering = ("dirdepth", "dirlength", "id")
    search_fields = ('filepath', 'serverIP')

    # def list(self, request, *args, **kwargs):
    #     queryset = self.filter_queryset(self.get_queryset())
    #
    #     # 如果返回的是查询集,进行序列化返回
    #     if isinstance(queryset, QuerySet):
    #         page = self.paginate_queryset(queryset)
    #         if page is not None:
    #             serializer = self.get_serializer(page, many=True)
    #             return self.get_paginated_response(serializer.data)
    #         serializer = self.get_serializer(queryset, many=True)
    #         return Response(serializer.data)
    #
    #     # 如果返回的是列表
    #     page = self.paginate_queryset(queryset)
    #     if page is not None:
    #         return self.get_paginated_response(page)
    #     return Response(queryset)
    #     # return HttpResponse(queryset)


class HandOutListNameViewSet(mixins.ListModelMixin, GenericViewSet):
    queryset = HandOutList
    serializer_class = HandOutListNameSerializer


class HandOutListViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, GenericViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = HandOutListSerializer
    pagination_class = HandOutListViewSetPagination

    def get_queryset(self):
        if self.request is not None:
            if self.action == "list":
                # 获取清单名称
                name = self.request.query_params.get("name")
                if name:
                    return HandOutList.objects.filter(name=name)
                else:
                    return HandOutList.objects.all()
            else:
                return HandOutList.objects.all()
        else:
            return []


class FileInfoViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, GenericViewSet):
    permission_classes = [IsAuthenticated]
    queryset = FileInfo.objects.all()
    serializer_class = FileInfoSerializer
    pagination_class = FileInfoViewSetPagination

    def get_queryset(self):
        if self.request is not None:
            if self.action == "list":
                handoutlist_name = self.request.query_params.get("handoutlist_name")
                return FileInfo.objects.filter(handoutlist_name=handoutlist_name)
            else:
                return FileInfo.objects.all()
        else:
            return []


class FilePathViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, GenericViewSet):
    permission_classes = [IsAuthenticated]
    pagination_class = FilePathViewSetPagination
    serializer_class = FilePathSerializer
    def get_queryset(self):
        if self.request is not None:
            if self.action == "list":
                fileinfo_name = self.request.query_params.get("fileinfo_name")
                return FilePath.objects.filter(fileinfo_name=fileinfo_name)
            else:
                return FilePath.objects.all()
        else:
            return []


