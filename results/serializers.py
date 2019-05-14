# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework import serializers

from celery_app.upload_doc import doc_data_updata
from results.models import HandOutList, FileInfo, UploadDoc
from datetime import datetime


# logger = logging.getLogger("django_error")

class HandOutListSerializer(serializers.ModelSerializer):
    deliverways = serializers.SerializerMethodField(label=u"所选择的介质类型")
    media = serializers.SerializerMethodField(label=u"所选择的递送方式")
    result_list = serializers.ListField(max_length=50000, allow_empty=True, write_only=True,
                                        label=u"创建分发单时对应的成果")

    class Meta:
        model = HandOutList
        fields = "__all__"
        extra_kwargs = {
            # "name": {"required": True, "allow_null": False, "help_text": u"分发单名字"},
            # 前端不需要uniquenum字段
            "uniquenum": {"required": False, "write_only": True},
            "createtime": {"format": '%Y-%m-%d %H:%M:%S'},
            "updatetime": {"format": '%Y-%m-%d %H:%M:%S'},
            "sendouttime": {"format": '%Y-%m-%d'},
            "recievetime": {"format": '%Y-%m-%d'},
            "file": {"required": False, "write_only": True}
        }

    def to_representation(self, instance):
        # data = super().to_representation(instance)
        data = super().to_representation(instance)
        fileinfos = FileInfo.objects.filter(handoutlist_uniquenum=instance.uniquenum)
        serializer = FileInfoSerializer(fileinfos, many=True)
        data["result_list"] = serializer.data
        # 前端不需要uniquenum字段
        # del data["uniquenum"]
        return data

    def get_deliverways(self, obj):
        # 返回清单所选的所有递送方式
        deliverways_list = []
        if obj.selfgetway:
            deliverways_list.append(u"自取")
        if obj.postway:
            deliverways_list.append(u"邮寄")
        if obj.networkway:
            deliverways_list.append(u"网络")
        if obj.sendtoway:
            deliverways_list.append(u"送往")

        return ",".join(deliverways_list)

    def get_media(self, obj):
        # 返回成果所选的所有介质
        media_list = []
        if obj.papermedia:
            media_list.append(u"纸质")
        if obj.cdmedia:
            media_list.append(u"光盘")
        if obj.diskmedia:
            media_list.append(u"硬盘")
        if obj.networkmedia:
            media_list.append(u"网络")
        if obj.othermedia:
            media_list.append(u"其他")

        return ",".join(media_list)

    def create(self, validated_data):
        # result_list = validated_data.get("result_list")
        # del validated_data["result_list"]

        sendouttime = validated_data.get("sendouttime")
        recievetime = validated_data.get("recievetime")
        if sendouttime:
            validated_data["sendouttimec"] = sendouttime.strftime("%Y年%m月%d日")
        if recievetime:
            validated_data["recievetimec"] = recievetime.strftime("%Y年%m月%d日")

        result_list = validated_data.pop("result_list")
        user = self.context["request"].user
        uniquenum = datetime.now().strftime("%Y%m%d%H%M%S%f") + "%06d" % user.id
        validated_data["uniquenum"] = uniquenum
        handoutlist = HandOutList.objects.create(**validated_data)

        for fileinfo_dict in result_list:
            if "key" in fileinfo_dict.keys():
                del fileinfo_dict["key"]
            fileinfo_dict["handoutlist_uniquenum"] = handoutlist.uniquenum
            fileinfo_name = fileinfo_dict.get("name")
            try:
                FileInfo.objects.get(handoutlist_uniquenum=handoutlist.uniquenum, name=fileinfo_name)
            except FileInfo.DoesNotExist:
                fileinfo = FileInfo.objects.create(**fileinfo_dict)

        return handoutlist

    def update(self, instance, validated_data):
        sendouttime = validated_data.get("sendouttime")
        recievetime = validated_data.get("recievetime")
        if sendouttime:
            validated_data["sendouttimec"] = sendouttime.strftime("%Y年%m月%d日")
        if recievetime:
            validated_data["recievetimec"] = recievetime.strftime("%Y年%m月%d日")
        if "file" in validated_data.keys():
            del validated_data["file"]
        result_list = validated_data.pop("result_list")
        handoutlist = super(HandOutListSerializer, self).update(instance, validated_data)
        FileInfo.objects.filter(handoutlist_uniquenum=instance.uniquenum).delete()
        for fileinfo_dict in result_list:
            if "key" in fileinfo_dict.keys():
                del fileinfo_dict["key"]
            fileinfo_dict["handoutlist_uniquenum"] = handoutlist.uniquenum
            fileinfo_name = fileinfo_dict.get("name")
            try:
                FileInfo.objects.get(handoutlist_uniquenum=handoutlist.uniquenum, name=fileinfo_name)
            except FileInfo.DoesNotExist:
                fileinfo = FileInfo.objects.create(**fileinfo_dict)

        return handoutlist


class FileInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileInfo
        fields = "__all__"
        extra_kwargs = {
            "createtime": {"format": '%Y-%m-%d %H:%M:%S'},
            "updatetime": {"format": '%Y-%m-%d %H:%M:%S'},
        }


class ExportHandoutlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = HandOutList
        fields = ["id", "uniquenum", "file", "createtime", "updatetime"]
        extra_kwargs = {
            # "name": {"required": True, "allow_null": False, "help_text": u"分发单名字"},
            # 前端不需要uniquenum字段
            # "uniquenum": {"required": False,"write_only": True},
            "uniquenum": {"required": False, "read_only": True},
            "createtime": {"format": '%Y-%m-%d %H:%M:%S'},
            "updatetime": {"format": '%Y-%m-%d %H:%M:%S'},
        }


class UploadDocSerializer(serializers.ModelSerializer):
    data_id = serializers.CharField(max_length=5000, write_only=True)
    class Meta:
        model = UploadDoc
        fields = ["file", "data_id"]
        extra_kwargs = {
            "file": {"allow_null": False, "help_text": u"分发单文件"},
        }

    def create(self, validated_data):
        data_id = validated_data["data_id"]
        validated_data["file"].name = datetime.now().strftime("%Y%m%d") + ".doc"
        del validated_data["data_id"]
        try:
            uniquenum = HandOutList.objects.get(id=data_id).uniquenum
        except HandOutList.DoesNotExist:
            raise serializers.ValidationError(u"ID:{0}不存在".format(data_id))
        file = super(UploadDocSerializer, self).create(validated_data)
        filepath = file.file.path
        filename = validated_data.get("file").name
        doc_data_updata.delay(filepath, uniquenum, filename)
        return file









"""
class EchartReceiveunitSerializer(serializers.ModelSerializer):
    class Meta:
        model = EchartReceiveunit
        fields = ["receiveunit", "count"]


class EchartReceiveTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EchartReceiveTime
        fields = ["sendouttime", "count"]
"""