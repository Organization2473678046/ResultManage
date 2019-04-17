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
from file.models import HandOutList, FileInfo, FilePath
from file.serializers import HandOutListNameSerializer, HandOutListSerializer, \
    FileInfoNameSerializer, FileInfoSerializer, FilePathSerializer


# from drf_haystack.viewsets import HaystackViewSet
# from file.serializers import ResultFileIndexSerializer


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


"""
class ResultFileViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, GenericViewSet):

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
    
"""

"""
class ResultFileSearchViewSet(HaystackViewSet):
    # ResultFile搜索
    index_models = [ResultFile]
    pagination_class = ResultFileViewSetPagination

    serializer_class = ResultFileIndexSerializer
"""


class HandOutListNameViewSet(mixins.ListModelMixin, GenericViewSet):
    queryset = HandOutList.objects.all().order_by("id")
    serializer_class = HandOutListNameSerializer


class HandOutListViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, mixins.RetrieveModelMixin,
                         mixins.UpdateModelMixin, GenericViewSet):
    """
    list: 查询分发单
    create :创建分发单
    update: 修改分发单
    """
    permission_classes = [IsAuthenticated]
    queryset = HandOutList.objects.all()
    serializer_class = HandOutListSerializer
    pagination_class = HandOutListViewSetPagination
    filter_backends = [SearchFilter, DjangoFilterBackend, OrderingFilter]
    ordering_fields = (
        'id', 'name', "listnum", "auditnum", "secretlevel", "purpose", "receiveunit", "receiver", "receiverinfo",
        "handovertime", "recievetime", "undertaker", "deliverway", "handler")
    ordering = ("id",)
    search_fields = (
        'id', 'name', "listnum", "auditnum", "secretlevel", "purpose", "receiveunit", "receiver", "receiverinfo",
        "handovertime", "recievetime", "undertaker", "deliverway", "handler")

    # def get_queryset(self):
    #     if self.request is not None:
    #         if self.action == "list":
    #             # 获取清单名称
    #             name = self.request.query_params.get("name")
    #             if name:
    #                 return HandOutList.objects.filter(name=name)
    #             else:
    #                 return HandOutList.objects.all()
    #         else:
    #             return HandOutList.objects.all()
    #     else:
    #         return []

    def retrieve(self, request, *args, **kwargs):
        handoutlist = self.get_object()
        fileinfos = FileInfo.objects.filter(handoutlist_name=handoutlist.name)
        handoutlist_serializer = self.get_serializer(handoutlist)
        fileinfos_serializer = FileInfoSerializer(fileinfos, many=True)
        return Response({"handoutlist": handoutlist_serializer.data, "fileinfos": fileinfos_serializer.data})


class FileInfoNameViewSet(mixins.ListModelMixin, GenericViewSet):
    """
    list: 查询成果资料名字信息

    """
    permission_classes = [IsAuthenticated]
    # queryset = FileInfo.objects.all().order_by("id")
    serializer_class = FileInfoNameSerializer

    def get_queryset(self):
        if self.request is not None:
            # if self.action == "list":
            handoutlist_name = self.request.query_params.get("handoutlist_name")
            return FileInfo.objects.filter(handoutlist_name=handoutlist_name).order_by("id")

        else:
            return []


class FileInfoViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin, GenericViewSet):
    """
    list: 查询成果资料信息
    create: 添加成果资料
    update: 修改成果资料
    """
    permission_classes = [IsAuthenticated]
    queryset = FileInfo.objects.all()
    serializer_class = FileInfoSerializer
    pagination_class = FileInfoViewSetPagination
    filter_backends = [SearchFilter, DjangoFilterBackend, OrderingFilter]
    ordering_fields = (
        'id', 'name', "resulttype", "num", "datasize", "resultyear", "secretlevel", "handoutlist_name", "createtime",
        "updatetime")
    ordering = ("id",)
    search_fields = (
        'id', 'name', "resulttype", "num", "datasize", "papermedia", "cdmedia", "diskmedia", "networkmedia",
        "othermedia", "resultyear", "secretlevel", "handoutlist_name", "createtime", "updatetime")

    def get_queryset(self):
        if self.request is not None:
            if self.action == "list":
                handoutlist_name = self.request.query_params.get("handoutlist_name")
                return FileInfo.objects.filter(handoutlist_name=handoutlist_name)
            else:
                return FileInfo.objects.all()
        else:
            return []


class FilePathViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin,
                      GenericViewSet):
    """
    list: 查询成果资料文件路径
    create: 批量添加成果资料文件路径
    update: 修改成果资料文件路径
    """
    permission_classes = [IsAuthenticated]
    pagination_class = FilePathViewSetPagination
    serializer_class = FilePathSerializer
    filter_backends = [SearchFilter, DjangoFilterBackend, OrderingFilter]
    ordering_fields = ("id", "filepath", "fileinfo_name", "handoutlist_name", "createtime", "updatetime")
    ordering = ("id",)
    search_fields = ("id", "filepath", "fileinfo_name", "handoutlist_name", "createtime", "updatetime")

    def get_queryset(self):
        if self.request is not None:
            if self.action == "list":
                handoutlist_name = self.request.query_params.get("handoutlist_name")
                fileinfo_name = self.request.query_params.get("fileinfo_name")
                return FilePath.objects.filter(handoutlist_name=handoutlist_name, fileinfo_name=fileinfo_name).order_by(
                    "id")
            else:
                return FilePath.objects.all()
        else:
            return []

    def create(self, request, *args, **kwargs):
        filepath_list = request.data.get("filepath_list")
        fileinfo_name = request.data.get("fileinfo_name")
        handoutlist_name = request.data.get("handoutlist_name")
        if handoutlist_name is None:
            return Response({"msg": "请指定成果分发单"})
        if fileinfo_name is None:
            return Response({"msg": "请指定成果"})
        if filepath_list is None:
            return Response({"msg": "请选择成果资料路径"})

        filepaths = []
        for path in filepath_list:
            try:
                filepath = FilePath.objects.get(handoutlist_name=handoutlist_name, fileinfo_name=fileinfo_name,
                                                filepath=path)
            except FilePath.DoesNotExist:
                filepath = FilePath.objects.create(
                    # filepath=path["object"]["filepath"],
                    filepath=path["filepath"],  # TODO 此处需要修改
                    fileinfo_name=fileinfo_name,
                    handoutlist_name=handoutlist_name
                )
                filepaths.append(filepath)
            else:
                filepaths.append(filepath)
        serializer = self.get_serializer(filepaths, many=True)
        return Response(serializer.data)
