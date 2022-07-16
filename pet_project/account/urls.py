from django.contrib import admin
from django.urls import path, include
from account.views import *


urlpatterns = [
    path('registration/', registration, name='registration'),
    path('profile/', profile, name='current_user_profile'),
    path('user_profile/<int:user_id>', get_profile, name='get_user_profile')
]
