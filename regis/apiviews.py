
from rest_framework import generics
from regis.serializers import UserSerializer,UserSerializerlogin
from rest_framework import status

from django.contrib.auth.models import User

from rest_framework.response import Response
from rest_framework.views import APIView

from django.contrib.auth import authenticate

class LoginView(APIView):
    queryset = User.objects.all()
    authentication_classes = ()
    permission_classes = ()
    serializer_class = UserSerializerlogin


    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)
        if user:
            return Response({"token": user.auth_token.key})
        else:
            return Response({"Ошибка ввода": "Неправильные учетные данные"}, status=status.HTTP_400_BAD_REQUEST)






class UserCreate(generics.CreateAPIView):
    """
    Создание пользователя
    """
    queryset = User.objects.all()
    authentication_classes = ()
    permission_classes = ()
    serializer_class = UserSerializer


