from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


class UserSerializer(serializers.ModelSerializer):
    PASSWORD = serializers.CharField(write_only=True, style={'input_type': 'password'})

    class Meta:

        model = User
        fields = ('username', 'password', 'PASSWORD')#,
        #extra_kwargs = {'password': {'write_only': True}}
        #extra_kwargs = {'PASSWORD': {'write_only': True}}

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
        fields = ('username', 'password')  # ,'password2'
        extra_kwargs = {'password': {'write_only': True}}
