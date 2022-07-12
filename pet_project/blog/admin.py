from django.contrib import admin
from .models import *

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'category', 'time_created')
    list_filter = ('time_created', 'title', )


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', )
    list_filter = ('name',)

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user',)
    list_filter = ('biography', )

class PhotoPostAdmin(admin.ModelAdmin):
    list_display = ('post', 'image')


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(PhotoPost, PhotoPostAdmin)


# Register your models here.
