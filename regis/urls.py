from django.urls import path
from .apiviews import LoginView,UserCreate
from rest_framework.authtoken import views

urlpatterns = [
    #path('login/', views.obtain_auth_token, name='login'),
    path('api-token-reg/',UserCreate.as_view()),
    path('api-token-auth/',LoginView.as_view(),name='api-token-auth/'),
    ]
