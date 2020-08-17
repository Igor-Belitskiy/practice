import django_filters
from django.utils import timezone
from rest_framework.permissions import IsAuthenticated
from .forms import PostForm
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from rest_framework.generics import get_object_or_404
from django.shortcuts import render
from .pagination import CustomPagination
from blog.models import Post
from .serializers import ArticleSerializer
from .permission import IsOwnerOrReadOnly
from rest_framework import viewsets
from rest_framework import filters
from django.db.models import Q
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


def post_new(request):
    form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})


def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})


class ArticleViewSet(viewsets.ModelViewSet):
    serializer_class = ArticleSerializer
    queryset = Post.objects.all()
    permission_classes = (IsOwnerOrReadOnly, IsAuthenticated)
    pagination_class = CustomPagination
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['author__username']
    ordering_fields = ['published_date']

    def get_queryset(self):
        user = self.request.user
        return Post.objects.filter(Q(publication=True) | Q(author=user))





