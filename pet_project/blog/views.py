from urllib import request
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import Search_Post_Form, ProfileForm
from .models import *
from django import forms 
from .utils import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, FormView
# Create your views here.


class BlogHome(DataMixin, ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'index.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        info = self.get_post_content()
        context = dict(list(context.items()) + list(info.items()))
        return context

    def get_queryset(self):
        return Post.objects.all()
        

class BlogPost(DataMixin, DetailView):
    model = Post
    context_object_name = 'post'
    template_name = 'post.html'
    slug_url_kwarg = 'post_slug'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        info = self.get_post_content()
        context = dict(list(context.items()) + list(info.items()))
        return context

    
class BlogCategory(DataMixin, ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'category_posts.html'
    queryset = Post.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        info = self.get_post_content()
        context = dict(list(context.items()) + list(info.items()))
        return context

    def get_queryset(self):
        category = Category.objects.get(slug=self.kwargs.get('category_slug'))
        return self.queryset.filter(category=category)


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

    
#class SearchPost(DataMixin, FormView):
#    template_name = 'index.html'
#    form_class = Search_Post_Form
#    search_form = Search_Post_Form()
#    success_url = '/blog/'
#    queryset = Post.objects.all()
#    def get_context_data(self, *, object_list=None, **kwargs):
#        context = super().get_context_data(**kwargs)
#        info = self.get_post_content()
#        search_result = self.queryset.filter(title=SearchPost.search_form.cleaned_data['search_post'])
#        if search_result:
#            context = dict(list(context.items()) + list(info.items()))
#            context['posts'] = search_result
#            return context
#        context = dict(list(context.items()) + list(info.items()))
#        return context
#
#    def get_queryset(self):
#        return self.queryset.filter(title=Search_Post_Form.data['search_post'])


#def index(request):
#    queryset = Category.objects.all()
#    posts = Post.objects.all()
#    user = request.user
#
#    return render(request, 'index.html', {'categories': queryset, 'posts': posts, 'user': user, })

#def post(request, post_id):
#    post = Post.objects.get(pk=post_id)
#    queryset = Category.objects.all()
#    images = PhotoPost.objects.filter(post=post)
#    return render(request, 'post.html', {'categories': queryset, 'post': post, 'images': images})

#def show_category_post(request, category_id):
#    queryset = Category.objects.all()
#    posts = Post.objects.filter(category=category_id)
#    return render(request, 'index.html', {'categories': queryset, 'posts': posts})




    
    
