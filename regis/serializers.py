from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.Serializer):

    username = serializers.CharField(max_length=100)
    password = serializers.CharField(write_only=True, style={'input_type': 'password'})
    password_2 = serializers.CharField(write_only=True, style={'input_type': 'password'})

    def validate(self, data):
        password = data.get('password')
        confirm_password = data.pop('password_2')
        if password != confirm_password:
            raise serializers.ValidationError('Пароли не совподают')
        return data

    def save(self):
        username = self.validated_data['username']
        password = self.validated_data['password']
        user = User.objects.create_user(username)
        user.set_password(password)
        user.save()
        return user


class UserSerializerlogin(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')
        extra_kwargs = {'password': {'write_only': True}}

