from django.core.exceptions import ObjectDoesNotExist
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, BasicAuthentication,TokenAuthentication
from regis.serializers import UserSerializer,UserSerializerlogin
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from django.contrib.auth import logout


class LoginView(APIView):

    queryset = User.objects.all()
    serializer_class = UserSerializerlogin
    permission_classes = ()
    authentication_classes = ()
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)
        if user:
            #'username': user.username,
            token, created = Token.objects.get_or_create(user=user)
            return Response({"token": token.key})
        else:
            return Response({"Ошибка ввода": "Неправильные учетные данные"}, status=status.HTTP_400_BAD_REQUEST)

class UserCreate(generics.CreateAPIView):
    """
    Создание пользователя
    """
    queryset = User.objects.all()
    permission_classes = ()
    serializer_class = UserSerializer
    def post(self, request):
        try:
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid():
                users = serializer.save()
                token = Token.objects.create(user=users)
                #'username': users.username,
                return Response({ 'token': token.key})
            else:
                return Response({"Ошибка ввода": "Неправильные учетные данные"}, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response("Пользователь существует")

class Logout(APIView):
    #permission_classes = (IsAuthenticated,)
    def get(self, request, format=None):
        try:
            logout(request)
            request.user.auth_token.delete()
            return Response(status=status.HTTP_200_OK)
        except:
            return Response('Токен уже удалён')

