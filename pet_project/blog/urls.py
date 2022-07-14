from django.contrib import admin
from django.urls import path, include
from .views import *


urlpatterns = [
    path('blog/', BlogHome.as_view(), name='home'),
    path('blog/search/', search_post, name='search_post'),
    path('blog/<slug:post_slug>/', BlogPost.as_view(), name='post'),
    path('blog/category/<slug:category_slug>/', BlogCategory.as_view(), name='posts_category'),
]
