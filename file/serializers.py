# -*- coding: utf-8 -*-
from rest_framework import serializers
from file.models import ResultFile, HandOutList, FileInfo, FilePath


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


class FileInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileInfo
        fields = "__all__"

class FilePathSerializer(serializers.ModelSerializer):
    class Meta:
        model = FilePath
        fields = "__all__"
