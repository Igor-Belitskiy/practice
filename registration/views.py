from django.shortcuts import render
from registration.serializers import UserCreateSerializers,UserLoginSerializers
from rest_framework import generics


# Create your views here.
class UserCreate(generics.CreateAPIView):
    serializer_class = UserCreateSerializers

class UserLogin(generics.CreateAPIView):
    serializer_class = UserLoginSerializers

