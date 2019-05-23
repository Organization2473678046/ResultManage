# -*- coding: utf-8 -*-
import os
from rest_framework import serializers
from ResultManage import settings
from users.models import User, License


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'reallyname', 'isadmin', 'date_joined']
        extra_kwargs = {
                        'reallyname': {"required": True},
                        'password': {
                            'write_only': True,
                            'min_length': 6,
                            'max_length': 16,
                            'error_messages': {
                                'min_length': '仅允许6-16个字符的密码',
                                'max_length': '仅允许6-16个字符的密码',
                            }
                        },
                        'date_joined': {"format": '%Y-%m-%d %H:%M:%S'},
                        }


    def create(self, validated_data):

        try:
            password = validated_data.get("password")
            if password == "":
                password = "123456"
        except:
            password = "123456"
        validated_data["password"] = password
        user = super(UserSerializer, self).create(validated_data)
        user.set_password(validated_data["password"])

        user.save()
        return user


class UserUpdateSerializer(serializers.ModelSerializer):
    new_password = serializers.CharField(label='新密码', allow_null=True, allow_blank=True, min_length=6, max_length=16, write_only=True)
    enter_password = serializers.CharField(label='确认密码', min_length=6, max_length=16, write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'password', "new_password", "enter_password"]
        extra_kwargs = {
                        'password': {
                            'write_only': True,
                            'min_length': 6,
                            'max_length': 16,
                            'error_messages': {
                                'min_length': '仅允许6-16个字符的密码',
                                'max_length': '仅允许6-16个字符的密码',
                            }
                        },
                        'new_password': {
                            'write_only': True,
                            'min_length': 6,
                            'max_length': 16,
                            'error_messages': {
                                'min_length': '仅允许6-16个字符的密码',
                                'max_length': '仅允许6-16个字符的密码',
                            }
                        }
                        }

    def validate(self, attrs):

        password = attrs.get('new_password')
        enter_password = attrs.get('enter_password')

        if password != enter_password:
            raise serializers.ValidationError('密码不一致')

        return attrs


    def update(self, instance, validated_data):
        if instance.check_password(validated_data.get("password")):
            instance.set_password(validated_data.get("new_password"))
            instance.save()
        else:
            raise serializers.ValidationError('密码错误')
        return instance



class UserAdminSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username', 'isadmin', 'reallyname']






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
