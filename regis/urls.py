from django.urls import path
from .apiviews import LoginView,UserCreate
from rest_framework.authtoken import views

urlpatterns = [
    path("login/", LoginView.as_view(), name="login"),
    #path("login/", views.obtain_auth_token, name="login"),
    path("users/",UserCreate.as_view(), name="user_create"),

]
