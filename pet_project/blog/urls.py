from django.contrib import admin
from django.urls import path, include
from .views import *


urlpatterns = [
    path('blog/', index, name='home'),
    path('blog/<int:post_id>/', post, name='post'),
    path('blog/category/<int:category_id>/', show_category_post, name='posts_category')
]
