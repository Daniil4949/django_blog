from urllib import request
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import Search_Post_Form, ProfileForm, CommentForm
from .models import *
from django import forms 
from .utils import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, FormView
# Create your views here.


class BlogHome(DataMixin, ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'blog/index.html'

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
    template_name = 'blog/post.html'
    slug_url_kwarg = 'post_slug'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        info = self.get_post_content()
        post = Post.objects.get(slug=self.kwargs.get('post_slug'))
        context['comments'] = Comment.objects.filter(post=post)
        #context['comments'] = Comment.objects.filter(slug=self.kwargs.get('post_slug'))
        context = dict(list(context.items()) + list(info.items()))
        return context


    
class BlogCategory(DataMixin, ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'blog/category_posts.html'
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
    if request.method == 'POST':
        if search_form.is_valid():
            title = search_form.cleaned_data['title']
            post = Post.objects.filter(title__contains=str(title))
            return render(request, 'blog/index.html', {'categories': queryset, 'posts': post})
        return render(request, 'blog/not_found.html', {'categories': queryset, 'post': ''})
    return redirect('home')

def add_comment(request, post_slug):
    queryset = Category.objects.all()
    comment_form = CommentForm(request.POST)
    if request.method == 'POST':
        if comment_form.is_valid():
            post = Post.objects.get(slug=post_slug)
            content = comment_form.cleaned_data['content']
            comments = Comment.objects.filter(post=post)
            Comment.objects.create(user=request.user, post=post, content=content)
            return redirect('post', post_slug=post_slug)
        return redirect('post', post_slug=post_slug)
    return redirect('post', post_slug=post_slug)



    
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




    
    
