# -*- coding: utf-8 -*-
from rest_framework import serializers
from file.models import ResultFile


class ResultFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResultFile
        fields = ["id", "filepath", "serverIP","dirlength","dirdepth"]
