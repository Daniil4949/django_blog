from django.contrib import admin
from django.urls import path, include
from account.views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('registration/', registration, name='registration'),
    path('profile/', profile, name='current_user_profile'),
    path('user_profile/<int:user_id>', get_profile, name='get_user_profile')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)