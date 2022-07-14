from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import BlogAPIList, BlogAPIUpdate, CategoryApiList, CategoryAPIUpdate

urlpatterns = [
   path('posts/', BlogAPIList.as_view()),
   path('posts/<int:pk>/', BlogAPIUpdate.as_view()),
   path('categories/', CategoryApiList.as_view()),
   path('categories/<int:pk>/', CategoryAPIUpdate.as_view()),

]

