# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework.viewsets import GenericViewSet
from rest_framework.filters import OrderingFilter,SearchFilter
from rest_framework import mixins
from .models import User
from .serializers import UserSerializer


# Create your views here.
class UserViewSet(mixins.ListModelMixin,mixins.CreateModelMixin,GenericViewSet):
    permission_classes = [IsAuthenticated,IsAdminUser]
    serializer_class = UserSerializer
    queryset = User.objects.all().order_by("id")
    # filter_backends = [OrderingFilter]

