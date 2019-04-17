# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework import serializers
from file.models import HandOutList, FileInfo, FilePath
# from file.models import ResultFile
# from drf_haystack.serializers import HaystackSerializer
# from file.search_indexes import ResultFileIndex
import logging

logger = logging.getLogger("django_error")

"""
class ResultFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResultFile
        fields = ["id", "filepath", "serverIP", "dirlength", "dirdepth"]
"""
'''
class ResultFileIndexSerializer(HaystackSerializer):
    """
    SKU索引结果数据序列化器
    """
    object = ResultFileSerializer(read_only=True)

    class Meta:
        index_classes = [ResultFileIndex]
        fields = ('text', 'object')
'''


class HandOutListNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = HandOutList
        fields = ["id", "name"]


class HandOutListSerializer(serializers.ModelSerializer):
    deliverways = serializers.SerializerMethodField(label=u"所选择的介质类型")

    class Meta:
        model = HandOutList
        fields = "__all__"
        extra_kwargs = {
            # "name": {"required": True, "allow_null": False, "help_text": u"分发单名字"},
            "handovertime": {"format": '%Y-%m-%d %H:%M:%S'},
            "recievetime": {"format": '%Y-%m-%d %H:%M:%S'},
            "createtime": {"format": '%Y-%m-%d %H:%M:%S'},
            "updatetime": {"format": '%Y-%m-%d %H:%M:%S'},
        }

    def get_deliverways(self, obj):
        # 返回清单所选的所有递送方式
        deliverways_list = []
        if obj.selfgetway:
            # deliverways_list.insert(0,u"自取")
            deliverways_list.append(u"自取")
        if obj.postway:
            deliverways_list.append(u"邮寄")
        if obj.networkway:
            deliverways_list.append(u"网络")
        if obj.deliverway:
            deliverways_list.append(u"送往")
        if obj.otherway:
            # deliverways_list.append(u"其他方式:{0}".format(obj.otherwaydetail))
            deliverways_list.append(u"其他")

        return ",".join(deliverways_list)


class FileInfoNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileInfo
        fields = ["id", "name", "handoutlist_name"]


class FileInfoSerializer(serializers.ModelSerializer):
    media = serializers.SerializerMethodField(label=u"所选择的递送方式")

    class Meta:
        model = FileInfo
        fields = "__all__"
        extra_kwargs = {
            "createtime": {"format": '%Y-%m-%d %H:%M:%S'},
            "updatetime": {"format": '%Y-%m-%d %H:%M:%S'},
        }

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

    def validate(self, validated_data):
        handoutlist_name = validated_data.get("handoutlist_name")
        try:
            handoutlist = HandOutList.objects.get(name=handoutlist_name)
        except HandOutList.DoesNotExist as e:
            logger.warning(e)
            raise serializers.ValidationError(u"名称为 {0} 的清单不存在".format(handoutlist_name))

        # 防止同一个分发清单内成果资料名称重复
        name = validated_data.get("name")
        if self.context['view'].action == 'create':
            try:
                fileinfo = FileInfo.objects.get(handoutlist_name=handoutlist_name, name=name)
            except:
                pass
            else:
                raise serializers.ValidationError(u"{0} 中名为 {1} 的成果资料已存在".format(handoutlist_name, name))
        elif self.context['view'].action == 'update':
            id = self.context['view'].kwargs.get('pk')
            fileinfo = FileInfo.objects.get(id=id)
            if name != fileinfo.name:
                try:
                    fileinfo = FileInfo.objects.get(handoutlist_name=handoutlist_name, name=name)
                except:
                    pass
                else:
                    raise serializers.ValidationError(u"{0} 中名为 {1} 的成果资料已存在".format(handoutlist_name, name))

        return validated_data


class FilePathSerializer(serializers.ModelSerializer):
    # filepath_list = serializers.CharField(label=u"成果文件路径列表")
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
            # logger.warning(e)
            raise serializers.ValidationError(u"名称为 {0} 的清单不存在".format(handoutlist_name))
        fileinfo_name = validated_data.get("fileinfo_name")
        try:
            fileinfo = FileInfo.objects.get(name=fileinfo_name, handoutlist_name=handoutlist.name)
        except FileInfo.DoesNotExist as e:
            # logger.warning(e)
            raise serializers.ValidationError(u"清单 {0} 中名称为 '{1} 的成果资料不存在".format(handoutlist_name, fileinfo_name))
        return validated_data
