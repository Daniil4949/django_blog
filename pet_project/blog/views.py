from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from .models import *
from .forms import *
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

def registration(request):
    queryset = Category.objects.all()
    posts = Post.objects.all()
    if request.method == 'POST':
        user_form = RegistrationUserForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password2'])
            new_user.save()
            return render(request, 'registration_done.html', {'categories': queryset, 'posts': posts, 'user_form': user_form})
        return render(request, 'registration.html', {'categories': queryset, 'posts': posts, 'user_form': user_form})
    user_form = RegistrationUserForm()
    return render(request, 'registration.html', {'categories': queryset, 'posts': posts, 'user_form': user_form})
    
