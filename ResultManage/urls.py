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
from file.views import HandOutListNameViewSet, HandOutListViewSet, FileInfoNameViewSet, \
    FileInfoViewSet, FilePathViewSet
# from file.views import ResultFileSearchViewSet

router = DefaultRouter()

router.register(r'users', UserViewSet, base_name='users')
# router.register(r'resultfile', ResultFileViewSet, base_name='resultfile')
# router.register('resultfilesearch', ResultFileSearchViewSet, base_name='resultfile_search')
router.register(r'handoutlistnames', HandOutListNameViewSet, base_name='handoutlistnames')
router.register(r'handoutlists', HandOutListViewSet, base_name='handoutlists')
router.register(r'fileinfonames', FileInfoNameViewSet, base_name='fileinfonames')
router.register(r'fileinfos', FileInfoViewSet, base_name='fileinfos')
router.register(r'filepaths', FilePathViewSet, base_name='filepaths')

urlpatterns = [
    # url(r'^v0.2/admin/', admin.site.urls),
    url(r'^v0.2/login/$', obtain_jwt_token),
    url(r'^v0.2/', include(router.urls)),
    url(r'^v0.2/docs/', include_docs_urls(title=u"成果管理系统API")),
    url(r'^v0.2/api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
