# -*- coding: utf-8 -*-
"""ResultManage URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter
from rest_framework_jwt.views import obtain_jwt_token
from users.views import UserViewSet
from file.views import ResultFileViewSet

router = DefaultRouter()

router.register(r'user',UserViewSet,base_name='user')
router.register(r'resultfile', ResultFileViewSet, base_name='resultfile')


urlpatterns = [
    url(r'^v0.1/admin/', admin.site.urls),
    url(r'^v0.1/login/$', obtain_jwt_token),
    url(r'^v0.1/', include(router.urls)),
    url(r'^v0.1/docs/', include_docs_urls(title=u"成果管理系统API")),
    url(r'^v0.1/api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
