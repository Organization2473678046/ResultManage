# -*- coding: utf-8 -*-
from rest_framework import serializers
from file.models import ResultFile, HandOutList, FileInfo, FilePath
import logging

logger = logging.getLogger("django_error")


class ResultFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResultFile
        fields = ["id", "filepath", "serverIP", "dirlength", "dirdepth"]


class HandOutListNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = HandOutList
        fields = ["id", "name"]


class HandOutListSerializer(serializers.ModelSerializer):
    class Meta:
        model = HandOutList
        fields = "__all__"
        extra_kwargs = {
            # "name": {"required": True, "allow_null": False, "help_text": u"主任务包名字"},
            "createtime": {"format": '%Y-%m-%d %H:%M:%S'},
            # "updatetime": {"format": '%Y-%m-%d %H:%M:%S'},
            # "owner": {"required": True, "allow_null": False, "help_text": u"作业员"},
            # "mapnums": {"required": True, "write_only": True,
            #             "error_messages": {"required": u"请输入图号"}, "help_text": u"图号"},
        }


class FileInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileInfo
        fields = "__all__"
        extra_kwargs = {
            "createtime": {"format": '%Y-%m-%d %H:%M:%S'},
            "updatetime": {"format": '%Y-%m-%d %H:%M:%S'},
        }

    def validate(self, validated_data):
        handoutlist_name = validated_data.get("handoutlist_name")
        try:
            handoutlist = HandOutList.objects.get(name=handoutlist_name)
        except HandOutList.DoesNotExist as e:
            logger.warning(e)
            raise serializers.ValidationError(u"名称为 {0} 的清单不存在".format(handoutlist_name))

        return validated_data

    # def create(self, validated_data):
    #
    #     pass


class FilePathSerializer(serializers.ModelSerializer):
    class Meta:
        model = FilePath
        fields = "__all__"
        extra_kwargs = {
            "createtime": {"format": '%Y-%m-%d %H:%M:%S'},
            "updatetime": {"format": '%Y-%m-%d %H:%M:%S'},
        }

    def validate(self, validated_data):
        handoutlist_name = validated_data.get("handoutlist_name")
        try:
            handoutlist = HandOutList.objects.get(name=handoutlist_name)
        except HandOutList.DoesNotExist as e:
            logger.warning(e)
            raise serializers.ValidationError(u"名称为 {0} 的清单不存在".format(handoutlist_name))

        fileinfo_name = validated_data.get("fileinfo_name")
        try:
            fileinfo = FileInfo.objects.get(name=fileinfo_name, handoutlist_name=handoutlist.name)
        except FileInfo.DoesNotExist as e:
            logger.warning(e)
            raise serializers.ValidationError(u"清单 {0} 中名称为 '{1} 的成果资料不存在".format(handoutlist_name, fileinfo_name))

        return validated_data
