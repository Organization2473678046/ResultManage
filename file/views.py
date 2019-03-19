# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.mixins import ListModelMixin, CreateModelMixin
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import GenericViewSet
from file.models import ResultFileSerializer, ResultFile


class ResultFileViewSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'limit'
    max_page_size = 50
    page_query_param = 'page'


class ResultFileViewSet(ListModelMixin, CreateModelMixin, GenericViewSet):

    serializer_class = ResultFileSerializer
    queryset = ResultFile.objects.all()
    pagination_class = ResultFileViewSetPagination
    filter_backends = [SearchFilter, DjangoFilterBackend, OrderingFilter]
    ordering_fields = ("id", "file_path", "server_allow")
    ordering = ("id",)
    search_fields = ('file_path', 'server_allow')

