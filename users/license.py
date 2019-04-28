# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.permissions import BasePermission
from datetime import datetime


class LicensePerssion(BasePermission):
    message = u"授权已过期,请联系管理人员更换授权文件"

    def has_permission(self, request, view):
        time_ = datetime.strptime("2019-04-30", "%Y-%m-%d")
        if datetime.now() >= time_:
            return False
        return True
