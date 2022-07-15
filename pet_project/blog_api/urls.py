from django.urls import path, include, re_path
from .views import BlogAPIList, BlogAPIUpdate, CategoryApiList, CategoryAPIUpdate

urlpatterns = [
   path('posts/', BlogAPIList.as_view()),
   path('posts/<int:pk>/', BlogAPIUpdate.as_view()),
   path('categories/', CategoryApiList.as_view()),
   path('categories/<int:pk>/', CategoryAPIUpdate.as_view()),
   path('auth/', include('djoser.urls')),
   re_path(r'^auth/', include('djoser.urls.authtoken')),

]

