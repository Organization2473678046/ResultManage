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
from django.views.static import serve
from django.conf import settings
from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter
from rest_framework_jwt.views import obtain_jwt_token
from users.views import UserViewSet, AuthenticateView, LicenseViewSet, UserListViewSet,UserAdminViewSet
from results import views

router = DefaultRouter()

router.register(r'users', UserViewSet, base_name='users')
router.register(r'handoutlists', views.HandOutListViewSet, base_name='handoutlists')
router.register(r'exporthandoutlist', views.ExportHandoutlistView, base_name='exporthandoutlist')
router.register(r'echartreceiveunit', views.EchartReceiveUnitViewSet, base_name='echartreceiveunit')
router.register(r'echartreceivetime', views.EchartReceiveTimeViewSet, base_name='echartreceivetime')
router.register(r"exportexcel",views.ExportExcelViewSet,base_name="exportexcel")
router.register(r'license', LicenseViewSet, base_name='license')
router.register(r'uploaddoc', views.UploadDocViewSet, base_name='uploaddoc')
router.register(r'userlist', UserListViewSet, base_name='userlist')
router.register(r'userupdate', UserAdminViewSet, base_name='userupdate')



urlpatterns = [
    # url(r'^v2019.05.17/admin/', admin.site.urls),
    # url(r'^v2019.05.17/login/$', obtain_jwt_token),
    url(r'^v2019.05.17/login/$', AuthenticateView.as_view()),
    url(r'^v2019.05.17/', include(router.urls)),
    url(r'^v2019.05.17/docs/', include_docs_urls(title=u"成果管理系统API")),
    url(r'^v2019.05.17/media/(?P<path>.*)$', serve, {"document_root": settings.MEDIA_ROOT}),
    url(r'^v2019.05.17/api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
