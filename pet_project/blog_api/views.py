from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from django.forms import model_to_dict
from blog.models import Post, Category
from .serializers import BlogSerializer, CategorySerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class BlogAPIList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = BlogSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class BlogAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = BlogSerializer


class CategoryApiList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class CategoryAPIUpdate(generics.RetrieveUpdateAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


# Create your views here.
