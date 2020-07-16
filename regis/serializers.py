from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, style={'input_type': 'password'})
    PASSWORD = serializers.CharField(write_only=True, style={'input_type': 'password'})

    class Meta:

        model = User
        fields = ('username', 'password', 'PASSWORD')#


        def validate(self, attrs):
            data = super(UserSerializer, self).validate(attrs)
            if data['password'] != data['PASSWORD']:
                raise serializers.ValidationError('Пароли не совподают!')
            del data['PASSWORD']
            return data

        def create(self, validated_data):
            user = User(
                username=validated_data['username']
            )
            user.set_password(validated_data['password'])
            user.save()
            Token.objects.create(user=user)
            return user

class UserSerializerlogin(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'password')
        extra_kwargs = {'password': {'write_only': True}}
