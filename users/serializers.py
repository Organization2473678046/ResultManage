# -*- coding: utf-8 -*-
import os

from rest_framework import serializers

from ResultManage import settings
from users.models import User, License


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'reallyname', 'isadmin', 'date_joined']
        extra_kwargs = {'password': {"write_only": True},
                        'reallyname': {"required": True},
                        "date_joined": {"read_only": True, "format": '%Y-%m-%d %H:%M:%S'}
                        }

    # def create(self, validated_data):
    #     user = super(UserSerializer, self).create(validated_data)
    #     if user.isadmin is True:
    #         user.set_password("root12345")
    #     else:
    #         # user.is_staff = False
    #         user.set_password("12345")
    #     user.save()
    #     return user

    def create(self, validated_data):
        user = super(UserSerializer, self).create(validated_data)
        user.set_password(validated_data["password"])
        user.is_superuser = True
        user.is_staff = True
        user.isadmin = True
        user.save()

        return user

class LicenseSerializer(serializers.ModelSerializer):

    class Meta:
        model = License
        fields = ['file']

    def create(self, validated_data):
        mediapath = os.path.join(settings.MEDIA_ROOT)
        filename = validated_data["file"].name.split(".")[0] + ".pyc"
        if os.path.exists(os.path.join(mediapath, "license/", filename)):
            os.remove(os.path.join(mediapath, "license/", filename))

        validated_data["file"].name = filename
        file = super(LicenseSerializer, self).create(validated_data=validated_data)

        return file
