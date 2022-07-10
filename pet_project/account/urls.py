from django.contrib import admin
from django.urls import path, include
from account.views import *


urlpatterns = [
    path('registration/', registration, name='registration'),
    

]
