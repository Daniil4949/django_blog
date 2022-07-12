from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import Search_Post_Form, ProfileForm
from .models import *
from django import forms 
# Create your views here.


def index(request):
    queryset = Category.objects.all()
    posts = Post.objects.all()
    user = request.user

    return render(request, 'index.html', {'categories': queryset, 'posts': posts, 'user': user, })

def post(request, post_id):
    post = Post.objects.get(pk=post_id)
    queryset = Category.objects.all()
    images = PhotoPost.objects.filter(post=post)
    return render(request, 'post.html', {'categories': queryset, 'post': post, 'images': images})

def show_category_post(request, category_id):
    queryset = Category.objects.all()
    posts = Post.objects.filter(category=category_id)
    return render(request, 'index.html', {'categories': queryset, 'posts': posts})


def search_post(request):
    queryset = Category.objects.all()
    search_form = Search_Post_Form(request.POST)
    title = search_form.data['search_post']
    try:
        post = Post.objects.filter(title=title)
    except:
        post = ''
    if post:
        return render(request, 'index.html', {'categories': queryset, 'posts': post})
    return render(request, 'not_found.html', {'categories': queryset, 'post': post})

    
    
@login_required
def profile(request):
    if request.method == 'POST':
        profile_from = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if profile_from.is_valid():
            profile_from.save()
    data_user = Profile.objects.get(user=request.user)
    profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'profile.html', {'profile_form': profile_form, 'user': data_user})