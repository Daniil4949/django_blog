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
    