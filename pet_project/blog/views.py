from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from .models import *
# Create your views here.


def index(request):
    queryset = Category.objects.all()
    posts = Post.objects.all()
    return render(request, 'index.html', {'categories': queryset, 'posts': posts})

def post(request, post_id):
    post = Post.objects.get(pk=post_id)
    queryset = Category.objects.all()
    return render(request, 'post.html', {'categories': queryset, 'post': post})

def show_category_post(request, category_id):
    queryset = Category.objects.all()
    posts = Post.objects.filter(category=category_id)
    return render(request, 'index.html', {'categories': queryset, 'posts': posts})