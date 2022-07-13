from django.shortcuts import render, redirect
from blog.models import Category, Post, Profile
from account.forms import *
from django.contrib.auth import authenticate, login
from blog.forms import ProfileForm
from django.contrib.auth.decorators import login_required

def registration(request):
    captcha = FormWithCaptcha()
    queryset = Category.objects.all()
    posts = Post.objects.all()
    if request.method == 'POST':
        user_form = RegistrationUserForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password2'])
            new_user.save()
            Profile.objects.create(user=new_user)
            return render(request, 'registration_complete.html', {'categories': queryset, 'posts': posts, 'user_form': user_form})
        return render(request, 'registration.html', {'categories': queryset, 'posts': posts, 'user_form': user_form,})
    user_form = RegistrationUserForm()
    return render(request, 'registration.html', {'categories': queryset,'user_form': user_form,})
    

@login_required
def profile(request):
    if request.method == 'POST':
        profile_from = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if profile_from.is_valid():
            profile_from.save()
    data_user = Profile.objects.get(user=request.user)
    profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'profile.html', {'profile_form': profile_form, 'user': data_user})

    


            