# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from .search_filter import SearchFilter
from rest_framework import mixins
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response
from file.models import ResultFile
from file.serializers import ResultFileSerializer


class ResultFileViewSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'limit'
    max_page_size = 50
    page_query_param = 'page'


class ResultFileViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, GenericViewSet):
    serializer_class = ResultFileSerializer
    queryset = ResultFile.objects.all()
    # pagination_class = ResultFileViewSetPagination
    # filter_backends = [SearchFilter, DjangoFilterBackend, OrderingFilter]
    filter_backends = [SearchFilter]
    # ordering_fields = ("id", "filepath", "serverIP")
    # ordering = ("id",)

    search_fields = ('filepath', 'serverIP')

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        # page = self.paginate_queryset(queryset)
        # if page is not None:
        #     serializer = self.get_serializer(page, many=True)
        #     return self.get_paginated_response(serializer.data)
        #
        # serializer = self.get_serializer(queryset, many=True)
        return Response(queryset)