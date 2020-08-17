from django.urls import path 
from . import views
from rest_framework import renderers

article_list = views.ArticleViewSet.as_view({
    #'get': 'list',
    'post': 'create'
})
article_detail = views.ArticleViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})
article_get = views.ArticleViewSet.as_view({
    'get': 'list'
})

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('article/', article_list, name='article-list'),
    path('article/<int:pk>/', article_detail, name='article-detail'),
    path('article/get/', article_get, name='article-highlight'),


]

