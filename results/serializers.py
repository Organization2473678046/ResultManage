# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework import serializers
from results.models import HandOutList, FileInfo, EchartReceiveunit, EchartReceiveTime
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
        # print(validated_data["sendouttime"])
        # print(type(validated_data["sendouttime"]))
        # print(validated_data["recievetime"])
        sendouttime = validated_data.get("sendouttime")
        recievetime = validated_data.get("recievetime")
        if sendouttime:
            # sendouttime_li = sendouttime.split("T")[0].split("-")
            # sendouttime = sendouttime_li[0] + "年" + sendouttime_li[1] + "月" + sendouttime_li[2] + "日"
            # sendouttime = sendouttime.split("T")[0]
            # validated_data["sendouttime"] = sendouttime


            validated_data["sendouttime"] = sendouttime[:10]
        if recievetime:
            # recievetime_li = recievetime["recievetime"].split("T")[0].split("-")
            # recievetime = recievetime_li[0] + "年" + recievetime_li[1] + "月" + recievetime_li[2] + "日"
            # recievetime = recievetime.split("T")[0]
            # validated_data["recievetime"] = recievetime
            validated_data["recievetime"] = recievetime[:10]

        result_list = validated_data.pop("result_list")
        user = self.context["request"].user
        uniquenum = datetime.now().strftime("%Y%m%d%H%M%S%f") + "%06d" % user.id
        validated_data["uniquenum"] = uniquenum
        handoutlist = HandOutList.objects.create(**validated_data)

        # print(result_list)
        # print(type(result_list))

        # fileinfo_list = json.loads(result_list)
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
            # sendouttime_li = sendouttime.split("T")[0].split("-")
            # sendouttime = sendouttime_li[0] + "年" + sendouttime_li[1] + "月" + sendouttime_li[2] + "日"
            # sendouttime = sendouttime.split("T")[0]
            validated_data["sendouttime"] = sendouttime[:10]
        if recievetime:
            # recievetime_li = recievetime["recievetime"].split("T")[0].split("-")
            # recievetime = recievetime_li[0] + "年" + recievetime_li[1] + "月" + recievetime_li[2] + "日"
            # recievetime = recievetime.split("T")[0]
            validated_data["recievetime"] = recievetime[:10]

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


class EchartReceiveunitSerializer(serializers.ModelSerializer):
    class Meta:
        model = EchartReceiveunit
        fields = ["receiveunit", "count"]


class EchartReceiveTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EchartReceiveTime
        fields = ["sendouttime", "count"]
