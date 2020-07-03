from rest_framework import serializers
from registration import models


class UserCreateSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Registration
        fields = '__all__'

class UserLoginSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Login
        fields = '__all__'
