# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os
import re
from django.conf import settings
from django.db.models import Q
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework import mixins
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response
from results.models import HandOutList, FileInfo, UploadDoc, HandoutlistExcel
from results.serializers import HandOutListSerializer, ExportHandoutlistSerializer, UploadDocSerializer, \
    HandoutlistExcelSerializer
from celery_app.generate_file import generate_docx
from celery_app.export_excel import write_excel


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
    permission_classes = [IsAuthenticated]
    queryset = HandOutList.objects.filter(isdelete=False)
    serializer_class = HandOutListSerializer
    pagination_class = HandOutListViewSetPagination
    filter_backends = [SearchFilter, DjangoFilterBackend, OrderingFilter]
    ordering_fields = (
        "id", "title", "signer", "name", "uniquenum", "listnum", "auditnum", "secrecyagreementnum", "purpose",
        "sendunit",
        "sendunitaddr", "sendunitpostcode", "receiveunit", "receiveunitaddr", "receiveunitpostcode", "handler",
        "handlerphonenum", "handlermobilephonenum", "receiver",
        "receiverphonenum", "receivermobilephonenum", "sendouttime", "recievetime", "selfgetway",
        "postway", "networkway", "sendtoway", "signature", "papermedia", "cdmedia", "diskmedia",
        "networkmedia",
        "othermedia", "medianums", "mapnums", "createtime", "filename", "file",
        "updatetime")
    ordering = ("id",)
    search_fields = (
        "id", "title", "signer", "name", "uniquenum", "listnum", "auditnum", "secrecyagreementnum", "purpose",
        "sendunit",
        "sendunitaddr", "sendunitpostcode", "receiveunit", "receiveunitaddr", "receiveunitpostcode", "handler",
        "handlerphonenum", "handlermobilephonenum", "receiver",
        "receiverphonenum", "receivermobilephonenum", "sendouttime", "recievetime", "selfgetway",
        "postway", "networkway", "sendtoway", "signature", "papermedia", "cdmedia", "diskmedia",
        "networkmedia",
        "othermedia", "medianums", "mapnums", "createtime", "filename", "file",
        "updatetime")


class ExportHandoutlistView(mixins.ListModelMixin, mixins.RetrieveModelMixin, GenericViewSet):
    permission_classes = [IsAuthenticated]
    queryset = HandOutList.objects.filter(isdelete=False)
    # serializer_class = HandOutListSerializer
    serializer_class = ExportHandoutlistSerializer

    def retrieve(self, request, *args, **kwargs):
        handoutlist = self.get_object()
        dbname = settings.DATABASES["default"]["NAME"]
        templates_dir = os.path.join(settings.BASE_DIR, "templates", "docx_templates")
        handoutlist_docxs = os.path.join(settings.MEDIA_ROOT, "handoutlist_docxs")
        if not os.path.exists(handoutlist_docxs):
            os.mkdir(handoutlist_docxs)
        # generate_docx.delay(dbname, handoutlist.id, handoutlist.uniquenum, templates_dir,
        #               handoutlist_docxs)
        generate_docx(dbname, handoutlist.id, handoutlist.uniquenum, templates_dir,
                      handoutlist_docxs)
        handoutlist = self.get_object()
        serializer = self.get_serializer(handoutlist)
        return Response(serializer.data)
        # return Response("ok")


class ExportExcelViewSet(mixins.ListModelMixin, GenericViewSet):
    permission_classes = [IsAuthenticated]
    queryset = HandoutlistExcel.objects.all()
    serializer_class = HandoutlistExcelSerializer

    def list(self, request, *args, **kwargs):
        try:
            HandoutlistExcel.objects.get(excelmark="handoutlist")
        except HandoutlistExcel.DoesNotExist:
            HandoutlistExcel.objects.create(excelmark="handoutlist")

        dbname = settings.DATABASES["default"]["NAME"]
        excel_dir = os.path.join(settings.MEDIA_ROOT, "handoutlist_excels")
        if not os.path.exists(excel_dir):
            os.mkdir(excel_dir)

        write_excel(dbname, excel_dir)
        handoutlistexcel = HandoutlistExcel.objects.get(excelmark="handoutlist")
        serializer = self.get_serializer(handoutlistexcel)
        return Response(serializer.data)


class EchartReceiveUnitViewSet(mixins.ListModelMixin, GenericViewSet):
    permission_classes = [IsAuthenticated]
    queryset = HandOutList.objects.filter(isdelete=False)
    serializer_class = HandOutListSerializer

    def list(self, request, *args, **kwargs):
        """
        receiveunit_list = list(
            set([item[value] for item in HandOutList.objects.filter(~Q(receiveunit="")).values("receiveunit") for value in item]))
        for receiveunit in receiveunit_list:
            count = HandOutList.objects.filter(receiveunit=receiveunit).count()
            try:
                echartreceiveunit = EchartReceiveunit.objects.get(receiveunit=receiveunit)
            except EchartReceiveunit.DoesNotExist:
                EchartReceiveunit.objects.create(receiveunit=receiveunit, count=count)
            else:
                echartreceiveunit.count = count
                echartreceiveunit.save()

        receiveunits = self.get_queryset()
        serializer = self.get_serializer(receiveunits, many=True)
        return Response(serializer.data)
        """
        try:
            year = request.query_params["year"]
        except:
            year = ""

        data_list = []
        receiveunit_list = list(
            set([item[value] for item in
                 HandOutList.objects.filter(~Q(receiveunit=""), listnum__startswith=year, isdelete=False).values(
                     "receiveunit") for
                 value in item]))
        for receiveunit in receiveunit_list:
            data_dict = {}
            count = HandOutList.objects.filter(receiveunit=receiveunit, isdelete=False).count()
            data_dict["receiveunit"] = receiveunit
            data_dict["count"] = count
            data_list.append(data_dict)
        return Response(data_list)


class EchartReceiveTimeViewSet(mixins.ListModelMixin, GenericViewSet):
    permission_classes = [IsAuthenticated]
    queryset = HandOutList.objects.filter(isdelete=False)
    serializer_class = HandOutListSerializer

    def list(self, request, *args, **kwargs):
        """
        data_list = []
        data_dict = {"2017": 0, "2018": 0, "2019": 0}

        sendouttime_list = HandOutList.objects.filter(~Q(sendouttime="")).values_list("sendouttime")
        for sendouttime in sendouttime_list:
            if sendouttime[0] == None:
                continue
            else:
                year = sendouttime[0].split("年")[0]
                time = re.findall("\d+", year)[0]
                data_dict[time] = data_dict[time] + 1

        for key, value in data_dict.items():
            print(key, value)

            try:
                Echartreceivetime = EchartReceiveTime.objects.get(sendouttime=key)
            except EchartReceiveTime.DoesNotExist:
                EchartReceiveTime.objects.create(sendouttime=key, count=value)
            else:
                Echartreceivetime.count = value
                Echartreceivetime.save()

        sendouttime = self.get_queryset()
        serializer = self.get_serializer(sendouttime, many=True)

        return Response(serializer.data)
        """
        data_list = []
        data_dict_ = {}

        sendouttime_list = HandOutList.objects.filter(~Q(sendouttimec=""), isdelete=False).values_list("sendouttimec")
        for sendouttime in sendouttime_list:
            if sendouttime[0] == None:
                continue
            else:
                year = sendouttime[0].split("年")[0]
                time = re.findall("\d+", year)[0]
                try:
                    data_dict_[time] = data_dict_[time] + 1
                except:
                    data_dict_[time] = 1

        for key, value in data_dict_.items():
            data_dict = {}
            data_dict["sendouttime"] = key
            data_dict["count"] = value
            data_list.append(data_dict)

        return Response(data_list)


class UploadDocViewSet(mixins.CreateModelMixin, GenericViewSet):
    serializer_class = UploadDocSerializer
    queryset = UploadDoc.objects.all()
    permission_classes = [IsAuthenticated]
