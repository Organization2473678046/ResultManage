# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os
from django.conf import settings
from rest_framework import serializers
from results.models import HandOutList, FileInfo
from datetime import datetime
from generate_file import generate_docx
import json
import logging


# logger = logging.getLogger("django_error")

class HandOutListSerializer(serializers.ModelSerializer):
    result_list = serializers.ListField(max_length=50000, allow_empty=True, write_only=True,
                                        label=u"创建分发单时对应的成果")

    class Meta:
        model = HandOutList
        fields = "__all__"
        extra_kwargs = {
            # "name": {"required": True, "allow_null": False, "help_text": u"分发单名字"},
            "uniquenum": {"required": False},
            "createtime": {"format": '%Y-%m-%d %H:%M:%S'},
            "updatetime": {"format": '%Y-%m-%d %H:%M:%S'},
        }

    def to_representation(self, instance):
        data = super().to_representation(instance)
        fileinfos = FileInfo.objects.filter(handoutlist_uniquenum=instance.uniquenum)
        serializer = FileInfoSerializer(fileinfos, many=True)
        data["result_list"] = serializer.data
        return data

    def create(self, validated_data):
        # result_list = validated_data.get("result_list")
        # del validated_data["result_list"]
        result_list = validated_data.pop("result_list")
        user = self.context["request"].user
        uniquenum = datetime.now().strftime("%Y%m%d%H%M%S%f") + "%06d" % user.id
        validated_data["uniquenum"] = uniquenum
        handoutlist = HandOutList.objects.create(**validated_data)

        print(result_list)
        print(type(result_list))

        # fileinfo_list = json.loads(result_list)
        for fileinfo_dict in result_list:
            if "key" in fileinfo_dict.keys():
                del fileinfo_dict["key"]
            fileinfo_dict["handoutlist_uniquenum"] = handoutlist.uniquenum
            try:
                FileInfo.objects.get(handoutlist_uniquenum=handoutlist.uniquenum, name=fileinfo_dict["name"])
            except FileInfo.DoesNotExist:
                fileinfo = FileInfo.objects.create(**fileinfo_dict)

        return handoutlist

    def update(self, instance, validated_data):
        result_list = validated_data.pop("result_list")
        handoutlist = super(HandOutListSerializer, self).update(instance, validated_data)
        FileInfo.objects.filter(handoutlist_uniquenum=instance.uniquenum).delete()
        for fileinfo_dict in result_list:
            if "key" in fileinfo_dict.keys():
                del fileinfo_dict["key"]
            fileinfo_dict["handoutlist_uniquenum"] = handoutlist.uniquenum
            try:
                FileInfo.objects.get(handoutlist_uniquenum=handoutlist.uniquenum, name=fileinfo_dict["name"])
            except FileInfo.DoesNotExist:
                fileinfo = FileInfo.objects.create(**fileinfo_dict)

        return handoutlist

# 导出分发单序列化器
# class ExportHandoutlistSerializer(serializers.ModelSerializer):
#     result_list = serializers.ListField(max_length=50000, allow_empty=True, write_only=True,
#                                         label=u"创建分发单时对应的成果")
#     class Meta:
#         model = HandOutList
#         fields = "__all__"
#         # "id", "title", "signer", "name", "uniquenum", "listnum", "auditnum", "secrecyagreementnum", "purpose",
#         #         "sendunit",
#         #         "sendunitaddr", "sendunitpostcode", "receiveunit", "receiveunitaddr", "receiveunitpostcode", "handler",
#         #         "handlerphonenum", "handlermobilephonenum", "receiver",
#         #         "receiverphonenum", "receivermobilephonenum", "sendouttime", "recievetime" "selfgetway",
#         #         "postway", "networkway", "sendtoway", "otherway", "signature", "papermedia", "cdmedia", "diskmedia",
#         #         "networkmedia",
#         #         "othermedia", "medianums", "mapnums", "createtime", "filename", "file",
#         #         "updatetime"
#         extra_kwargs = {
#             # "name": {"required": True, "allow_null": False, "help_text": u"分发单名字"},
#             "uniquenum": {"required": False},
#             "createtime": {"format": '%Y-%m-%d %H:%M:%S'},
#             "updatetime": {"format": '%Y-%m-%d %H:%M:%S'},
#         }
#
#
#     def to_representation(self, instance):
#         data = super().to_representation(instance)
#         fileinfos = FileInfo.objects.filter(handoutlist_uniquenum=instance.uniquenum)
#         serializer = FileInfoSerializer(fileinfos, many=True)
#         data["result_list"] = serializer.data
#         return data
#
#
#     def update(self, instance, validated_data):
#         fileinfo_list = FileInfo.objects.filter(handoutlist_uniquenum=instance.uniquenum)
#         templates_dir = os.path.join(settings.BASE_DIR, "templates", "docx_templates")
#         handoutlist_docxs = os.path.join(settings.MEDIA_ROOT, "handoutlist_docxs")
#         handoutlist_docs = os.path.join(settings.MEDIA_ROOT, "handoutlist_docs")
#         newhandoutlist = generate_docx(instance, fileinfo_list, templates_dir, handoutlist_docxs, handoutlist_docs)
#
#         return newhandoutlist


class FileInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = FileInfo
        fields = "__all__"
        extra_kwargs = {
            "createtime": {"format": '%Y-%m-%d %H:%M:%S'},
            "updatetime": {"format": '%Y-%m-%d %H:%M:%S'},
        }
