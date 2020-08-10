from django.urls import path 
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('blogget/', views.ArticleViewGet.as_view()),
    path('blogpost/', views.ArticleViewPost.as_view()),
    path('blogdel/<int:pk>/', views.ArticleViewDel.as_view()),
    #path('blogpost/<int:pk>/', views.ArticleViewPost.as_view()),
    #path('blogput/<int:pk>/', views.ArticleViewPut.as_view()),

]

