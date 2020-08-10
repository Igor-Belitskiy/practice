from rest_framework import generics
from regis.serializers import UserSerializer,UserSerializerlogin
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class LoginView(APIView):

    queryset = User.objects.all()
    serializer_class = UserSerializerlogin
    permission_classes = (IsAuthenticatedOrReadOnly,)
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)
        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({'username': user.username,"token": token.key})
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
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            users = serializer.save()
            token = Token.objects.create(user=users)
            return Response({'username': users.username, 'token': token.key})
        else:
            return Response({"Ошибка ввода": "Неправильные учетные данные"}, status=status.HTTP_400_BAD_REQUEST)










