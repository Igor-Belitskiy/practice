from django.utils import timezone
from rest_framework import serializers
from blog.models import Post


class ArticlelistSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Post
        fields = ('id', 'title', 'text', 'created_date', 'published_date','author')

class ArticleSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Post
        fields = '__all__'
