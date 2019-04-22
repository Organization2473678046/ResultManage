# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    reallyname = models.CharField(max_length=1000,null=True, verbose_name=u"真实姓名")
    isadmin = models.BooleanField(default=True, verbose_name=u"是否管理员")

    class Meta:
        verbose_name = u"用户"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username
