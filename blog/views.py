from django.utils import timezone
from django.shortcuts import render
from .forms import PostForm
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from rest_framework.generics import get_object_or_404, UpdateAPIView

from .models import Post
from django.shortcuts import render
from .pagination import CustomPagination
from blog.models import Post
from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView, UpdateAPIView
from .serializers import ArticleSerializer, ArticlelistSerializer
from .permission import IsOwnerOrReadOnly

# Create your views here.




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



class ArticleViewPut(UpdateAPIView,ListAPIView):
    serializer_class = ArticleSerializer
    queryset = Post.objects.all()
    permission_classes = (IsOwnerOrReadOnly,)
    pagination_class = CustomPagination

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class ArticleViewGet(ListAPIView):
    '''
    get
    '''
    serializer_class = ArticlelistSerializer
    queryset = Post.objects.all()
    permission_classes = (IsOwnerOrReadOnly,)
    pagination_class = CustomPagination

class ArticleViewPost(CreateAPIView,ListAPIView):
    serializer_class = ArticleSerializer
    queryset = Post.objects.all()
    permission_classes = (IsOwnerOrReadOnly,)
    pagination_class = CustomPagination

class ArticleViewDel(DestroyAPIView,ListAPIView):
    serializer_class = ArticleSerializer
    queryset = Post.objects.all()
    permission_classes = (IsOwnerOrReadOnly,)
    #pagination_class = CustomPagination