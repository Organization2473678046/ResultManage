# -*- coding: utf-8 -*-
from rest_framework import serializers
from models import User


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
        user.save()

        return user
