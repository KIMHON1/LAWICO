from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post

# Create your views here.


class PostListView(ListView):

    def get_queryset(self):
        return Post.objects.order_by('-created_at')[:5]


class PostDetailView(DetailView):
    model = Post

    

# class ArticleDetailView(DetailView):
#     model = Post
#     template_name = 'blog/detail.html'