# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.viewsets import GenericViewSet
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework import mixins
from .models import User
from .serializers import UserSerializer, LicenseSerializer
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
class UserViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, GenericViewSet):
    permission_classes = [IsAuthenticated, IsAdminUser]
    serializer_class = UserSerializer

    def get_queryset(self):
        user = self.request.user
        if self.action == "list":
            return User.objects.filter(id=user.id)
        else:
            return User.objects.all()
