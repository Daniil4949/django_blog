from django.views.decorators.cache import cache_page
from django.urls import path, include
from .views import *


urlpatterns = [
    path('blog/', cache_page(60)(BlogHome.as_view()), name='home'),
    path('blog/search/', search_post, name='search_post'),
    path('blog/<slug:post_slug>/', cache_page(60)(BlogPost.as_view()), name='post'),
    path('blog/<slug:post_slug>/add_comment/', add_comment, name='add_comment'),
    path('blog/category/<slug:category_slug>/', cache_page(60)(BlogCategory.as_view()), name='posts_category'),
]
