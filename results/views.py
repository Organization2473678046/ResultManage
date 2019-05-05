# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os
from django.conf import settings
from django.db.models import QuerySet
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework import mixins
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response
from django.http import HttpResponse
from results.models import HandOutList, FileInfo
from results.serializers import HandOutListSerializer
from generate_file import generate_docx


class HandOutListViewSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'limit'
    max_page_size = 50
    page_query_param = 'page'


class HandOutListViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, mixins.RetrieveModelMixin,
                         mixins.UpdateModelMixin, GenericViewSet):
    """
    list: 查询分发单
    create :创建分发单
    update: 修改分发单
    """
    permission_classes = [IsAuthenticated, IsAdminUser]
    queryset = HandOutList.objects.all()
    serializer_class = HandOutListSerializer
    pagination_class = HandOutListViewSetPagination
    filter_backends = [SearchFilter, DjangoFilterBackend, OrderingFilter]
    ordering_fields = (
        "id", "title", "signer", "name", "uniquenum", "listnum", "auditnum", "secrecyagreementnum", "purpose",
        "sendunit",
        "sendunitaddr", "sendunitpostcode", "receiveunit", "receiveunitaddr", "receiveunitpostcode", "handler",
        "handlerphonenum", "handlermobilephonenum", "receiver",
        "receiverphonenum", "receivermobilephonenum", "sendouttime", "recievetime" "selfgetway",
        "postway", "networkway", "sendtoway", "otherway", "signature", "papermedia", "cdmedia", "diskmedia",
        "networkmedia",
        "othermedia", "medianums", "mapnums", "createtime", "filename", "file",
        "updatetime")
    ordering = ("id",)
    search_fields = (
        "id", "title", "signer", "name", "uniquenum", "listnum", "auditnum", "secrecyagreementnum", "purpose",
        "sendunit",
        "sendunitaddr", "sendunitpostcode", "receiveunit", "receiveunitaddr", "receiveunitpostcode", "handler",
        "handlerphonenum", "handlermobilephonenum", "receiver",
        "receiverphonenum", "receivermobilephonenum", "sendouttime", "recievetime" "selfgetway",
        "postway", "networkway", "sendtoway", "otherway", "signature", "papermedia", "cdmedia", "diskmedia",
        "networkmedia",
        "othermedia", "medianums", "mapnums", "createtime", "filename", "file",
        "updatetime")

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

    # def retrieve(self, request, *args, **kwargs):
    #     handoutlist = self.get_object()
    #     fileinfos = FileInfo.objects.filter(handoutlist_name=handoutlist.name)
    #     handoutlist_serializer = self.get_serializer(handoutlist)
    #     fileinfos_serializer = FileInfoSerializer(fileinfos, many=True)
    #     return Response({"handoutlist": handoutlist_serializer.data, "fileinfos": fileinfos_serializer.data})
    #


# class ExportHandoutlistView(mixins.UpdateModelMixin,GenericViewSet):
class ExportHandoutlistView(mixins.ListModelMixin,mixins.RetrieveModelMixin,
                         mixins.UpdateModelMixin,GenericViewSet):
    permission_classes = [IsAuthenticated, IsAdminUser]
    queryset = HandOutList.objects.all()
    serializer_class = HandOutListSerializer

    def update(self, request, *args, **kwargs):
        handoutlist = self.get_object()
        fileinfo_list = FileInfo.objects.filter(handoutlist_uniquenum=handoutlist.uniquenum)
        templates_dir = os.path.join(settings.BASE_DIR,"templates","docx_templates")
        handoutlist_docxs = os.path.join(settings.MEDIA_ROOT,"handoutlist_docxs")
        handoutlist_docs = os.path.join(settings.MEDIA_ROOT,"handoutlist_docs")
        newhandoutlist = generate_docx(handoutlist, fileinfo_list, templates_dir, handoutlist_docxs, handoutlist_docs)

        serializer = self.get_serializer(newhandoutlist)
        return Response(serializer.data)


