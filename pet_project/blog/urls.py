from django.contrib import admin
from django.urls import path, include
from .views import *


urlpatterns = [
    path('blog/', BlogHome.as_view(), name='home'),
    path('blog/<int:post_id>/', BlogPost.as_view(), name='post'),
    path('blog/category/<int:category_id>/', BlogCategory.as_view(), name='posts_category'),
    path('blog/search/', search_post, name='search_post'),
]
