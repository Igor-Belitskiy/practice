from rest_framework import serializers, request
from django.contrib.auth.models import User

from rest_framework.permissions import IsAuthenticated




class UserSerializer(serializers.Serializer):
    model = User
    username = serializers.CharField(max_length=100)
    password = serializers.CharField(write_only=True, style={'input_type': 'password'})
    PASSWORD = serializers.CharField(write_only=True, style={'input_type': 'password'})

    permission_classes = (IsAuthenticated,)

    def validate(self, attrs):
        data = super(UserSerializer, self).validate(attrs)
        if data['password'] != data['PASSWORD']:
            raise serializers.ValidationError('Пароли не совподают!')
        del data['PASSWORD']
        return data

    def save(self):
        username=self.validated_data['username']
        password=self.validated_data['password']
        u=User.objects.create_user(username)
        u.set_password(password)
        u.save()









class UserSerializerlogin(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'password')
        extra_kwargs = {'password': {'write_only': True}}
