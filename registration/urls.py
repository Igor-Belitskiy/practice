from django.contrib import admin
from django.urls import path, include
from registration.views import UserCreate, UserLogin

urlpatterns = [

    path('', UserCreate.as_view()),
    path('login/', UserLogin.as_view()),


]