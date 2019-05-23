# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from users.permission import AdminPerssion
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework import mixins, status
from .models import User
from .serializers import UserSerializer, LicenseSerializer, UserUpdateSerializer, UserAdminSerializer
from rest_framework_jwt.views import ObtainJSONWebToken

from media.license.license import LicensePerssion


# 重写登录认证方法，添加授权
class AuthenticateView(ObtainJSONWebToken):
    permission_classes = [LicensePerssion]


# django
class LicenseViewSet(mixins.CreateModelMixin, GenericViewSet):
    permission_classes = []
    serializer_class = LicenseSerializer


# Create your views here.
class UserViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, mixins.DestroyModelMixin, mixins.UpdateModelMixin,
                  mixins.RetrieveModelMixin, GenericViewSet):
    # permission_classes = [IsAuthenticated]
    # serializer_class = UserSerializer

    def get_queryset(self):
        user = self.request.user
        if self.action == "list":
            return User.objects.filter(id=user.id)

        elif self.action == "retrieve":
            user = User.objects.get(id=int(self.kwargs["pk"]))
            user.set_password("123456")
            user.save()
            return User.objects.all()
        elif self.action == "update":
            return User.objects.all()
        else:
            return User.objects.all()

    def get_permissions(self):
        user = self.request.user
        if self.action == "list":
            return [IsAuthenticated()]

        elif self.action == "retrieve":
            return [IsAuthenticated(), AdminPerssion()]

        elif self.action == "update":
            try:
                user01 = User.objects.get(id=int(self.kwargs["pk"]))
            except:
                return [IsAuthenticated(), AdminPerssion()]
            if user == user01:
                return [IsAuthenticated()]
            else:
                return [IsAuthenticated(), AdminPerssion()]
        else:
            return [IsAuthenticated(), AdminPerssion()]

    def get_serializer_class(self):
        if self.action == "update":
            return UserUpdateSerializer
        else:
            return UserSerializer


class UserAdminViewSet(mixins.UpdateModelMixin, mixins.ListModelMixin, GenericViewSet):
    permission_classes = [IsAuthenticated, AdminPerssion]
    queryset = User.objects.all()
    serializer_class = UserAdminSerializer


class UserListViewSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'limit'
    max_page_size = 50
    page_query_param = 'page'


class UserListViewSet(mixins.ListModelMixin, GenericViewSet):
    permission_classes = [IsAuthenticated, AdminPerssion]
    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = UserListViewSetPagination
    filter_backends = [SearchFilter, DjangoFilterBackend, OrderingFilter]
    ordering_fields = ("id", "username", "isadmin", "reallyname")
    ordering = ("id",)
    search_fields = ("id", "username", "isadmin", "reallyname")
