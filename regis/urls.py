from django.urls import path
from .apiviews import LoginView,UserCreate,LogoutView


urlpatterns = [
    path('api-token-reg/',UserCreate.as_view(),name='api-token-reg'),
    path('api-token-auth/',LoginView.as_view(),name='api-token-auth'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
